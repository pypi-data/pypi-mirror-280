import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from .embending import PosEmbedding, RotaryEmbedding
import pytorch_lightning as pl
import torchmetrics

activations = [nn.ReLU(), nn.SELU(), nn.LeakyReLU(), nn.GELU(), nn.SiLU()]

def create_linear(in_channels, out_channels, bn=False):
    """
    Creates a linear layer with optional batch normalization.

    Parameters:
        in_channels (int): Number of input channels.
        out_channels (int): Number of output channels.
        bn (bool, optional): If True, adds batch normalization. Defaults to False.

    Returns:
        nn.Module: Linear layer with optional batch normalization.
    """
    # Create a linear layer
    m = nn.Linear(in_channels, out_channels)

    # Initialize the weights using Kaiming normal initialization with a ReLU nonlinearity
    nn.init.kaiming_normal_(m.weight, nonlinearity='relu')

    # Initialize the bias to zero if present
    if m.bias is not None:
        torch.nn.init.constant_(m.bias, 0)

    # Add batch normalization if requested
    if bn:
        # Create a batch normalization layer
        bn_layer = nn.BatchNorm1d(out_channels)

        # Combine the linear layer and batch normalization into a sequential module
        m = nn.Sequential(m, bn_layer)

    return m

def FeedForward(dim, expansion_factor=2, dropout=0.0, activation=nn.GELU(), bn=True):
    """
    Creates a feedforward block composed of linear layers, activation function, and dropout.

    Parameters:
        dim (int): Dimensionality of the input.
        expansion_factor (int, optional): Expansion factor for the intermediate hidden layer. Defaults to 2.
        dropout (float, optional): Dropout probability. Defaults to 0.0 (no dropout).
        activation (torch.nn.Module, optional): Activation function. Defaults to GELU().
        bn (bool, optional): If True, adds batch normalization. Defaults to True.

    Returns:
        nn.Sequential: Feedforward block.
    """
    # Create a sequential block with linear layer, activation, and dropout
    block = nn.Sequential(
        create_linear(dim, dim * expansion_factor, bn),
        activation,
        nn.Dropout(dropout),
        create_linear(dim * expansion_factor, dim, bn),
        nn.Dropout(dropout)
    )

    return block


class MLPBlock(nn.Module):
    def __init__(self, in_size=1, latent_dim=32, features_start=16, num_layers=4, context_size=96, activation=nn.ReLU(), bn=True):
        """
        Multi-Layer Perceptron (MLP) block with configurable layers and options.

        Parameters:
            in_size (int, optional): Size of the input. Defaults to 1.
            latent_dim (int, optional): Dimensionality of the latent space. Defaults to 32.
            features_start (int, optional): Number of features in the initial layer. Defaults to 16.
            num_layers (int, optional): Number of layers in the MLP. Defaults to 4.
            context_size (int, optional): Size of the context. Defaults to 96.
            activation (torch.nn.Module, optional): Activation function. Defaults to ReLU().
            bn (bool, optional): If True, adds batch normalization. Defaults to True.
        """
        super().__init__()

        # Calculate the size of the input after flattening
        self.in_size = in_size * context_size
        self.context_size = context_size

        # Initialize a list to store the layers of the MLP
        layers = [nn.Sequential(create_linear(self.in_size, features_start, bn=False), activation)]
        feats = features_start

        # Create the specified number of layers in the MLP
        for i in range(num_layers - 1):
            layers.append(nn.Sequential(create_linear(feats, feats * 2, bn=bn), activation))
            feats = feats * 2

        # Add the final layer with latent_dim and activation, without batch normalization
        layers.append(nn.Sequential(create_linear(feats, latent_dim, bn=False), activation))

        # Create a ModuleList to store the layers
        self.mlp_network = nn.ModuleList(layers)

    def forward(self, x):
        """
        Forward pass of the MLP block.

        Parameters:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor after passing through the MLP block.
        """
        # Flatten the input along dimensions 1 and 2
        x = x.flatten(1, 2)

        # Pass the input through each layer in the MLP
        for m in self.mlp_network:
            x = m(x)

        return x



class PastEncoder(nn.Module):
    def __init__(self, 
                 targets,
                 emb_size=28,
                 embed_type=None,
                 latent_size=64,
                 depth=2,
                 window_size=96,
                 activation=nn.ReLU(),
                 dropout=0.25,
                 n_channels=1):
        """
        Encoder module for processing past sequences.

        Parameters:
            targets (List): List of target variables.
            emb_size (int, optional): Dimensionality of the embedding space. Defaults to 28.
            embed_type (String, optional): Type of embedding to use. Defaults to None. Either -> 'PosEmb', 'RotaryEmb', 'CombinedEmb'
            latent_size: (int, optional): Dimensionality of the latent space. Defaults to 64.
            depth (int, optional): Number of layers in the MLP. Defaults to 2.
            window_size (int, optional): Size of the input window. Defaults to 96.
            activation (torch.nn.Module, optional): Activation function. Defaults to ReLU().
            dropout (float, optional): Dropout probability. Defaults to 0.25.
            n_channels (int, optional): Number of input channels. Defaults to 1.
        """
        super().__init__()

        # Calculate the number of output targets
        self.n_out = len(targets)

        # Initialize the MLP block for encoding
        self.encoder = MLPBlock(
            in_size = emb_size if embed_type != None else n_channels,
            latent_dim = latent_size,
            features_start = latent_size,
            num_layers=depth,
            context_size=window_size,
            activation=activation
        )

        # Normalize the input using LayerNorm
        self.norm = nn.LayerNorm(n_channels)

        # Apply dropout to the input
        self.dropout = nn.Dropout(dropout)

        # Store hyperparameters
        self.embed_type = embed_type

        # Embedding based on the specified type
        if embed_type == 'PosEmb':
            self.emb = PosEmbedding(n_channels, emb_size, window_size=window_size)
        elif embed_type == 'RotaryEmb':
            self.emb = RotaryEmbedding(emb_size)
        elif embed_type == 'CombinedEmb':
            self.pos_emb = self.emb = PosEmbedding(n_channels, emb_size, window_size=window_size)
            self.rotary_emb = RotaryEmbedding(emb_size)

    def forward(self, x):
        """
        Forward pass of the PastEncoder module.

        Parameters:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor after processing through the encoder.
        """
        # Normalize the input
        x = self.norm(x)

        # Apply embedding based on the specified type
        if self.embed_type != None:
            if self.embed_type == 'CombinedEmb':
                x = self.pos_emb(x) + self.rotary_emb(x)
               
            else:
                x = self.emb(x)
                
            # Apply dropout to the embedded input
            x = self.dropout(x)

        # Pass the input through the encoder
        x = self.encoder(x)

        return x
    
    

class FutureEncoder(nn.Module):
    def __init__(self, 
                 targets,
                 emb_size=28,
                 embed_type=None,
                 latent_size=64,
                 depth=2,
                 horizon=48,
                 activation=nn.ReLU(),
                 dropout=0.25, 
                 n_channels=1):
        """
        Encoder module for processing future sequences.

        Parameters:
            targets (List): List of target variables.
            emb_size (int, optional): Dimensionality of the embedding space. Defaults to 28.
            embed_type (String, optional): Type of embedding to use. Defaults to None. Either -> 'PosEmb', 'RotaryEmb', 'CombinedEmb'
            latent_size: (int, optional): Dimensionality of the latent space. Defaults to 64.
            depth (int, optional): Number of layers in the MLP. Defaults to 2.
            horizon (int, optional): Number of future time steps to forecast. Defaults to 48.
            activation (torch.nn.Module, optional): Activation function. Defaults to ReLU().
            dropout (float, optional): Dropout probability. Defaults to 0.25.
            n_channels (int, optional): Number of input channels. Defaults to 1.
        """
        super().__init__()

        # Calculate the number of output targets
        self.n_out = len(targets)

        # Initialize the MLP block for encoding
        self.encoder = MLPBlock(
            in_size=emb_size if embed_type != None else n_channels,
            latent_dim=latent_size,
            features_start=latent_size,
            num_layers=depth,
            context_size=horizon,
            activation=activation
        )

        # Normalize the input using LayerNorm
        self.norm = nn.LayerNorm(n_channels)

        # Apply dropout to the input
        self.dropout = nn.Dropout(dropout)

        # Store hyperparameters
        self.embed_type = embed_type

        # Embedding based on the specified type
        if embed_type == 'PosEmb':
            self.emb = PosEmbedding(n_channels, emb_size, window_size=horizon)
        elif embed_type == 'RotaryEmb':
            self.emb = RotaryEmbedding(emb_size)
        elif embed_type == 'CombinedEmb':
            self.pos_emb = self.emb = PosEmbedding(n_channels, emb_size, window_size=horizon)
            self.rotary_emb = RotaryEmbedding(emb_size)
        

    def forward(self, x):
        """
        Forward pass of the FutureEncoder module.

        Parameters:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor after processing through the encoder.
        """
        # Normalize the input
        x = self.norm(x)

        # Apply embedding based on the specified type
        
        if self.embed_type == 'CombinedEmb':
            x = self.pos_emb(x) + self.rotary_emb(x)
            # Apply dropout to the embedded input
            x = self.dropout(x)
            
        elif self.embed_type in ['PosEmb', 'RotaryEmb']:
           
            x = self.emb(x)
            # Apply dropout to the embedded input
            x = self.dropout(x)

        # Pass the input through the encoder
        x = self.encoder(x)

        return x
    
    
    
class MLPForecastNetwork(nn.Module):
    def __init__(self, 
                 targets,
                 time_varying_unknown_feature=[],
                 time_varying_known_categorical_feature=[],
                 time_varying_known_feature=[],
                 emb_size=28,
                 embed_type=None,
                 comb_type='attn-comb',
                 latent_size=64,
                 depth=2,
                 horizon=48,
                 window_size=96,
                 activation=nn.ReLU(),
                 dropout=0.25,
                 num_head=4,
                 alpha=0.01):
        """
        Multilayer Perceptron (MLP) Forecast Network for time series forecasting.

        Parameters:
            targets (List): List of target variables.
            time_varying_unknown_feature (List, optional): List of unknown time-varying features. Defaults to [].
            time_varying_known_categorical_feature (List, optional): List of known categorical time-varying features. Defaults to [].
            time_varying_known_feature (List, optional): List of known time-varying features. Defaults to [].
            emb_size (int, optional): Dimensionality of the embedding space. Defaults to 28.
            embed_type (String, optional): Type of embedding to use. Defaults to None. Either -> 'PosEmb', 'RotaryEmb', 'CombinedEmb'
            latent_size: (int, optional): Dimensionality of the latent space. Defaults to 64.
            depth (int, optional): Number of layers in the MLP. Defaults to 2.
            horizon (int, optional): Number of future time steps to forecast. Defaults to 48.
            activation (torch.nn.Module, optional): Activation function. Defaults to ReLU().
            dropout (float, optional): Dropout probability. Defaults to 0.25.
            num_head (int, optional): Number of heads in the multi-head attention. Defaults to 4.
            alpha (float, optional): Alpha parameter for the loss. Defaults to 0.01.
            window_size (int, optional): Size of the input window. Defaults to 96.
            comb_type (String, optional): Type of combination to use. Defaults to 'attn-comb'. Either -> 'attn-comb', 'weighted-comb', 'addition-comb'
        """
        super().__init__()

        # Calculate the number of output targets, unknown features, and covariates
        self.n_out = len(targets)
        self.n_unknown = len(time_varying_unknown_feature) + self.n_out
        self.n_covariates = 2 * len(time_varying_known_categorical_feature) + len(time_varying_known_feature)
        self.n_channels = self.n_unknown + self.n_covariates

        # Initialize PastEncoder for processing past sequences
        self.encoder = PastEncoder(targets,
                        emb_size=emb_size,
                        embed_type=embed_type,
                        latent_size=latent_size,
                        depth=depth,
                        window_size=window_size,
                        activation=activation,
                        dropout=dropout, 
                        n_channels=self.n_channels)

        # Initialize FutureEncoder for processing future sequences
        self.horizon = FutureEncoder(targets,
                        emb_size=emb_size,
                        embed_type=embed_type,
                        latent_size=latent_size,
                        depth=depth,
                        horizon=horizon,
                        activation=activation,
                        dropout=dropout,
                        n_channels=self.n_covariates)

        # Hyperparameters and components for decoding
        self.window_size = window_size
        self.comb_type = comb_type
        self.alpha = alpha

        if comb_type == 'attn-comb':
            self.attention = nn.MultiheadAttention(latent_size, num_head, dropout= dropout)
            
        if comb_type == 'weighted-comb':
             self.gate = nn.Linear(2 * latent_size, latent_size)
            
        self.decoder = nn.Sequential(
            FeedForward(latent_size, expansion_factor=1, dropout=dropout,
                        activation=activation, bn=True)
        )
        self.activation = activation
        self.mu = nn.Linear(latent_size, self.n_out * horizon)


    def forecast(self, x):
        """
        Generates forecasts for the input sequences.

        Parameters:
            x (torch.Tensor): Input tensor.

        Returns:
            dict: Dictionary containing the forecast predictions.
        """
        with torch.no_grad():
            pred = self(x)

        return dict(pred=pred)

    def forward(self, x):
        """
        Forward pass of the MLPForecastNetwork.

        Parameters:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor after processing through the network.
        """
        B = x.size(0)

        # Process past sequences with the encoder
        f = self.encoder(x[:, :self.window_size, :])

        # Process future sequences with the horizon encoder
        h = self.horizon(x[:, self.window_size:, self.n_unknown:])
        if self.comb_type == 'attn-comb':
            ph_hf = self.attention(h.unsqueeze(0), f.unsqueeze(0), f.unsqueeze(0))[0].squeeze(0)
        elif self.comb_type == 'weighted-comb':
            # Compute the gate mechanism
            gate = self.gate(torch.cat((h, f), -1)).sigmoid()
            # Combine past and future information using the gate mechanism
            ph_hf = (1 - gate) * f + gate * h
        else:
            ph_hf = h + f
        
        # Decode the combined information
        z = self.decoder(ph_hf)
        # Compute the final output
        loc = self.mu(z).reshape(B, -1, self.n_out)

        return loc


    def step(self, batch, metric_fn):
        """
        Training step for the MLPForecastNetwork.

        Parameters:
            batch (tuple): Tuple containing input and target tensors.
            metric_fn (callable): Metric function to evaluate.

        Returns:
            tuple: Tuple containing the loss and computed metric.
        """
        x, y = batch
        B = x.size(0)

        # Forward pass to obtain predictions
        y_pred = self(x)

        # Calculate the loss
        loss = self.alpha * F.mse_loss(y_pred, y) + (1 - self.alpha) * F.l1_loss(y_pred, y)

        # Compute the specified metric
        metric = metric_fn(y_pred, y)

        return loss, metric
    

class MLPForecastModel(pl.LightningModule):
    
    def __init__(self,  
                 targets,
                 time_varying_unknown_feature=[],
                 time_varying_known_categorical_feature=[],
                 time_varying_known_feature=[],
                 emb_size=28,
                 embed_type=None,
                 comb_type='attn-comb',
                 latent_size=64,
                 depth=2,
                 horizon=48,
                 window_size=96,
                 activation=nn.ReLU(),
                 dropout=0.25,
                 num_head=4,
                 alpha=0.01,
                 learning_rate=0.001,
                 weight_decay=1e-6,
                 max_epochs=50):
        """
        Multilayer Perceptron (MLP) Forecast Model for time series forecasting.

        Parameters:
            targets (List): List of target variables.
            time_varying_unknown_feature (List, optional): List of unknown time-varying features. Defaults to [].
            time_varying_known_categorical_feature (List, optional): List of known categorical time-varying features. Defaults to [].
            time_varying_known_feature (List, optional): List of known time-varying features. Defaults to [].
            emb_size (int, optional): Dimensionality of the embedding space. Defaults to 28.
            embed_type (String, optional): Type of embedding to use. Defaults to None. Either -> 'PosEmb', 'RotaryEmb', 'CombinedEmb'
            comb_type (String, optional): Type of combination to use. Defaults to 'attn-comb'. Either -> 'attn-comb', 'weighted-comb', 'addition-comb'
            latent_size: (int, optional): Dimensionality of the latent space. Defaults to 64.
            depth (int, optional): Number of layers in the MLP. Defaults to 2.
            horizon (int, optional): Number of future time steps to forecast. Defaults to 48.
            window_size (int, optional): Size of the input window. Defaults to 96.
            activation (torch.nn.Module, optional): Activation function. Defaults to ReLU().
            dropout (float, optional): Dropout probability. Defaults to 0.25.
            num_head (int, optional): Number of heads in the multi-head attention. Defaults to 4.
            alpha (float, optional): Alpha parameter for the loss. Defaults to 0.01.
            learning_rate (float, optional): Learning rate for the optimizer. Defaults to 0.001.
            weight_decay (float, optional): Weight decay for the optimizer. Defaults to 1e-6.
            max_epochs (int, optional): Maximum number of epochs for training. Defaults to 50.
        """
        
        super().__init__()
        
        assert targets, 'Please specify the target variables List'
        assert embed_type in [None, 'PosEmb', 'RotaryEmb', 'CombinedEmb'], 'Invalid embedding type, choose from -> None, \'PosEmb\', \'RotaryEmb\', \'CombinedEmb\''

        self.model = MLPForecastNetwork(targets,
                                time_varying_unknown_feature=time_varying_unknown_feature,
                                time_varying_known_categorical_feature=time_varying_known_categorical_feature,
                                time_varying_known_feature=time_varying_known_feature,
                                emb_size=emb_size,
                                embed_type=embed_type,
                                comb_type=comb_type,
                                latent_size=latent_size,
                                depth=depth,
                                horizon=horizon,
                                window_size=window_size,
                                activation=activation,
                                dropout=dropout,
                                num_head=num_head,
                                alpha=alpha)
        param_size = 0
        for param in self.model.parameters():
            param_size += param.nelement() * param.element_size()
        buffer_size = 0
        for buffer in self.model.buffers():
            buffer_size += buffer.nelement() * buffer.element_size()

        self.size = (param_size + buffer_size) / 1024**2
        print('model size: {:.3f}MB'.format(self.size))
        
        self.tra_metric_fcn=torchmetrics.MeanAbsoluteError()
        self.val_metric_fcn=torchmetrics.MeanAbsoluteError()

        self.save_hyperparameters()

        self.max_epochs = max_epochs
        self.learning_rate = learning_rate
        self.weight_decay = weight_decay

        
    def forecast(self, x):
        return self.model.forecast(x)
    
    
    def training_step(self, batch, batch_idx):
        loss, metric = self.model.step(batch, self.tra_metric_fcn)
        self.log("train_loss",loss, prog_bar=True, logger=True)
        self.log("train_mae",metric, prog_bar=True, logger=True)
        return loss
            
    
    def validation_step(self, batch, batch_idx):
        loss, metric = self.model.step(batch, self.val_metric_fcn) 
        self.log("val_loss",loss, prog_bar=True, logger=True)
        self.log("val_mae",metric, prog_bar=True, logger=True)


    def configure_optimizers(self):
        p1 = int(0.75 * self.max_epochs)
        p2 = int(0.9 * self.max_epochs)
        params  = list(self.parameters())
        optim = torch.optim.Adam(self.parameters(), lr=self.learning_rate,  weight_decay=self.weight_decay)
        scheduler  = torch.optim.lr_scheduler.MultiStepLR(optim, milestones=[p1, p2], gamma=0.1)
        return [optim], [scheduler]
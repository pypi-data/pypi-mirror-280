import tensorflow as tf 

class BandSplitLayer(tf.keras.layers.Layer):
    def __init__(self,  input_freq_dim=257, sr=16000, sub_band_feature_dim=128, **kwargs):
        super(BandSplitLayer, self).__init__(**kwargs)
        
        nyquist_freq = sr/2 #By default: 8000 Hz
        self.input_freq_dim = input_freq_dim
        self.freq_resolution = nyquist_freq/(input_freq_dim-1) #By default: 31.25 Hz/bin

        # For freq. below 1 kHz -> band size = 100 Hz
        self.first_band_in_bins = 1000/self.freq_resolution #By default: 32 bins of bandwidth (0, 1000) Hz
        self.suband_size_first_band = 125 #hZ -> Different from paper in order to cover all the 32 bins from the original spectrogram (with 100Hz it skips 2 bins from 30 to 32)
        self.suband_size_first_band_bins = int(self.suband_size_first_band / self.freq_resolution) #By default: 4 (If 100Hz it would be 3.2)
        self.num_sub_bands_first_band = int(self.first_band_in_bins / self.suband_size_first_band_bins) #By default: 8 sub bands

        # For freq. between 1 kHz and 4kHz -> band size = 250 Hz
        self.second_band_in_bins = (4000/self.freq_resolution) - (1000/self.freq_resolution) #By default: 96 bins of bandwidth (1000, 4000) Hz
        self.suband_size_second_band = 250 #hZ
        self.suband_size_second_band_bins = int(self.suband_size_second_band / self.freq_resolution) #By default:8 bins per sub band
        self.num_sub_bands_second_band = int(self.second_band_in_bins / self.suband_size_second_band_bins) #By default:12 sub bands

        # For freq. between 4 kHz and 8kHz -> band size = 500 Hz
        self.third_band_in_bins = (8000/self.freq_resolution) - (4000/self.freq_resolution) #By default: 128 bins of bandwidth (4000, 8000) Hz
        self.suband_size_third_band = 500 #hZ
        self.suband_size_third_band_bins = int(self.suband_size_third_band  /self.freq_resolution) #By default: 16 bins per sub band
        self.num_sub_bands_third_band  = int(self.third_band_in_bins / self.suband_size_third_band_bins) #By default: 8 sub bands

        total_num_sub_bands = self.num_sub_bands_first_band + self.num_sub_bands_second_band + self.num_sub_bands_third_band

        # Create a Norm + dense layer per sub band
        self.band_dense_layers = []
        self.layer_norm_layers = []
        for i in range(total_num_sub_bands):
          layer_norm = tf.keras.layers.LayerNormalization(axis=-1) #Assuming input shape: (batch_samples, time_dim, freq_dim)
          self.layer_norm_layers.append(layer_norm)
          dense_layer = tf.keras.layers.Dense(sub_band_feature_dim) # Output shape: (batch_samples, time_dim, sub_band_feature_dim)
          self.band_dense_layers.append(dense_layer)

    def call(self, inputs):

        # Initialize a list to store subbands
        embedded_subbands = []
        
        for i in range(self.num_sub_bands_first_band):
              start = int(i * self.suband_size_first_band_bins)
              end = int(start + self.suband_size_first_band_bins)
              subband = inputs[:, :, start:end] # shape: (batch_size, time_steps, sub_band_width)
              
              subband = tf.keras.layers.Reshape((-1, self.suband_size_first_band_bins))(subband) # Reshape the input tensor to combine time_dim and freq_dim (required because time_dim during training is None and layernorm breaks)
              norm_layer = self.layer_norm_layers[i]
              norm_subband = norm_layer(subband) # shape: (batch_size, time_steps, sub_band_width)
              norm_subband = tf.keras.layers.Reshape((-1, self.suband_size_first_band_bins))(norm_subband) # Reshape back to the original dimensions (required because time_dim during training is None and layernorm breaks)
              
              dense_layer = self.band_dense_layers[i]
              embedded_subband = dense_layer(norm_subband) # shape: (batch_size, time_steps, sub_band_feature_dim)
              
              embedded_subbands.append(embedded_subband)

        for i in range(self.num_sub_bands_second_band):
              start = int(self.first_band_in_bins + i * self.suband_size_second_band_bins)
              end = int(start + self.suband_size_second_band_bins)
              subband = inputs[:, :, start:end] # shape: (batch_size, time_steps, sub_band_width)
              
              subband = tf.keras.layers.Reshape((-1, self.suband_size_second_band_bins))(subband) # Reshape the input tensor to combine time_dim and freq_dim (required because time_dim during training is None and layernorm breaks)
              norm_layer = self.layer_norm_layers[i+self.num_sub_bands_first_band]
              norm_subband = norm_layer(subband) # shape: (batch_size, time_steps, sub_band_width)
              norm_subband = tf.keras.layers.Reshape((-1, self.suband_size_second_band_bins))(norm_subband) # Reshape back to the original dimensions (required because time_dim during training is None and layernorm breaks)
              
              dense_layer = self.band_dense_layers[i+self.num_sub_bands_first_band]
              embedded_subband = dense_layer(norm_subband) # shape: (batch_size, time_steps, sub_band_feature_dim)
              
              embedded_subbands.append(embedded_subband)

        for i in range(self.num_sub_bands_third_band):
              start = int(int(4000/self.freq_resolution) + i * self.suband_size_third_band_bins)
              end = int(start + self.suband_size_third_band_bins)
              subband = inputs[:, :, start:end] # shape: (batch_size, time_steps, sub_band_width)
              
              subband = tf.keras.layers.Reshape((-1, self.suband_size_third_band_bins))(subband) # Reshape the input tensor to combine time_dim and freq_dim (required because time_dim during training is None and layernorm breaks)
              norm_layer = self.layer_norm_layers[i+self.num_sub_bands_first_band+self.num_sub_bands_second_band]
              norm_subband = norm_layer(subband) # shape: (batch_size, time_steps, sub_band_width)
              norm_subband = tf.keras.layers.Reshape((-1, self.suband_size_third_band_bins))(norm_subband) # Reshape back to the original dimensions (required because time_dim during training is None and layernorm breaks)
              
              dense_layer = self.band_dense_layers[i+self.num_sub_bands_first_band+self.num_sub_bands_second_band]
              embedded_subband = dense_layer(norm_subband) # shape: (batch_size, time_steps, sub_band_feature_dim)
              
              embedded_subbands.append(embedded_subband)

        # Stack the subbands along a new axis
        subband_spectrogram = tf.stack(embedded_subbands, axis=2) # shape: (batch_size, time_steps, total_num_sub_bands, sub_band_feature_dim)

        return subband_spectrogram
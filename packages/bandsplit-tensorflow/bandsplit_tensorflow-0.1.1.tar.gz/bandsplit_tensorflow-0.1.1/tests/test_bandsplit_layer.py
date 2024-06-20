import tensorflow as tf
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bandsplit_tensorflow import BandSplitLayer

# Test the implementation
def simple_test():
    # Parameters
    input_time_dim = 100
    input_freq_dim = 257
    batch_size = 100
    sub_band_feature_dim = 128
    sr = 16000
    
    spectrogram = tf.random.normal((batch_size, input_time_dim, input_freq_dim))

    band_split_layer = BandSplitLayer(input_freq_dim=input_freq_dim, sr=sr, sub_band_feature_dim=sub_band_feature_dim)
    
    output = band_split_layer(spectrogram)
    
    assert output.shape == (batch_size, input_time_dim, 28, sub_band_feature_dim) #30 equals the total number of sub bands (define in paper)
    
    print("\n\n##########################\nTest passed. Output shape:", output.shape, "\n##########################")
    
simple_test()
# Non-official BandSplit implementation as a TF 2.0 layer 

Implementation of the BandSplit technique used in ["Music Source Separation with Band-split RNN"](https://arxiv.org/abs/2209.15174).

## Installlation
```bash
pip install bandsplit_tensorflow
```
## Usage
```python
import tensorflow as tf 
from bandsplit_tensorflow import BandSplitLayer

# Input parameters
input_time_dim = 100
input_freq_dim = 257
batch_size = 100
sr = 16000
# Hyperparameters
sub_band_feature_dim = 128

# Define layer
band_split_layer = BandSplitLayer(input_freq_dim=input_freq_dim, sr=sr, sub_band_feature_dim=sub_band_feature_dim)

# Use layer
random_spectrogram = tf.random.normal((batch_size, input_time_dim, input_freq_dim))
result = band_split_layer(random_spectrogram)
print(result)
```

## Notes:
* The implementation is only designed for a sample rate of 16 kHz

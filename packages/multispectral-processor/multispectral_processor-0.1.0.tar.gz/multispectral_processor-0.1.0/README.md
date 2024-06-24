# multispectral_processor

A package to process multispectral images.

## Installation

 ```bash
    pip install multispectral_processor
```

## Usage

```python
from multispectral_processor import process_multispectral_data

base_dir = '/path/to/Spectral_Images'
channels = ['Red_Edge_Channel', 'Red_Channel', 'Green_Channel', 'Near_Infrared_Channel']
train_images = '/path/to/train_images'
test_images = '/path/to/test_images'

process_multispectral_data(base_dir, channels, train_images, test_images)
'''
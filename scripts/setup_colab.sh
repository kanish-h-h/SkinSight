#!/bin/bash

# Mount Google Drive and symlink data
from google.colab import drive
drive.mount('/content/drive')
!ln -s /content/drive/MyDrive/SkinSight/data ./data

# Install dependencies
pip install -r requirements.txt

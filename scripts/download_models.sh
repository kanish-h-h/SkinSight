"""
  Download model of unet and srgan from hugging face via CLI

  author: @kanish-h-h
"""

huggingface-cli download SkinSight/unet --local-dir models/unet
huggingface-cli download SkinSight/srgan --local-dir models/srgan

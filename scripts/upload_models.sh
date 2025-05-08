"""
  Upload model to huggingface via CLI

  Author: kanish-h-h
"""

huggingface-cli upload SkinSight/unet models/unet/ --commit-message "Update U-Net"
huggingface-cli upload SkinSight/srgan models/srgan --commit-message "Update SRGAN"

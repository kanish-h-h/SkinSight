"""
    seperate scripts for preprocessing the data of skin/srgan
    before populating the database.

    Author: @kanish-h-h
"""

import os
import cv2
from src.data_loader import preprocess_skin_image, prepare_srgan_data

# Process segmentation data
raw_seg_dir = "/content/drive/MyDrive/Skin-Sight/data/raw/segmentation/skin"
proc_seg_dir = "/content/drive/MyDrive/Skin-Sight/data/processed/segementation"
os.makedirs(proc_seg_dir, exist_ok=True)

for img_name in os.listdir(raw_seg_dir):
    if "ISIC_" in img_name:  # ISIC naming convention
        img_path = os.path.join(raw_seg_dir, img_name)
        proc_image = preprocess_skin_image(img_path)
        cv2.imwrite(f"{proc_seg_dir}/images/{img_name}", proc_image * 255)

# Process SRGAN data
raw_srgan_dir = "/content/drive/MyDrive/Skin-Sight/data/raw/srgan/DIV2K_train_HR"
proc_srgan_dir = "/content/drive/MyDrive/Skin-Sight/data/processed/srgan"
os.makedirs(proc_srgan_dir, exist_ok=True)

for hr_img in os.listdir(raw_srgan_dir):
    hr_path = os.path.join(raw_srgan_dir, hr_img)
    lr, hr = prepare_srgan_data(hr_path)
    cv2.imwrite(f"{proc_srgan_dir}/train/HR/{hr_img}", hr)
    cv2.imwrite(f"{proc_srgan_dir}/train/LR/{hr_img}", lr)

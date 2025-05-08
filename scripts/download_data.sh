#!/bin/bash
# ISIC 2018 Segmentation Dataset
mkdir -p data/raw/segmentation
wget -P data/raw/segmentation "https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task1-2_Training_Input.zip"
unzip data/raw/segmentation/ISIC2018_Task1-2_Training_Input.zip -d data/raw/segmentation/

# DIV2K SRGAN Dataset (HR images)
mkdir -p data/raw/srgan
wget -P data/raw/srgan "https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip"
unzip data/raw/srgan/DIV2K_train_HR.zip -d data/raw/srgan/

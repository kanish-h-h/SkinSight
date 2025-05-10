import cv2
import numpy as np
from skimage import exposure
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# UNET Pipeline


def preprocess_skin_image(image_path: str, target_size=(256, 256)):
    """Applies CLAHE normalization and resizing for skin images."""
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # CLAHE Contrast Enhancement (Critical for low-contrast lesions)
    lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, titleGridSize=(8, 8))
    l_clahe = clahe.apply(l)
    lab_clahe = cv2.merge((l_clahe, a, b))
    image_clahe = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2RGB)

    # Resize and normalize
    image_resized = cv2.resize(image_clahe, target_size)
    return image_resized / 255.0


def create_binary_mask(mask_path: str, target_size=(256, 256)):
    """Converts grayscale mask to binary (0 or 1)."""
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    mask_resized = cv2.resize(mask, target_size)
    return (mask_resized > 127).astype(np.float32)  # Threshold at 50%


# SRGAN Pipeline


def prepare_srgan_data(hr_image_path: str, scale_factor=4):
    """Generates LR-HR pairs for SRGAN training."""
    hr_image = cv2.imread(hr_image_path, cv2.IMREAD_COLOR)
    hr_image = cv2.cvtColor(hr_image, cv2.COLOR_BGR2RGB)

    # Downsampling using bicubic interpolation
    lr_width = hr_image.shape[1] // scale_factor
    lr_height = hr_image.shape[0] // scale_factor
    lr_image = cv2.resize(hr_image, (lr_width, lr_height),
                          interpolation=cv2.INTER_CUBIC)

    return lr_image, hr_image


def get_augmenter():
    return ImageDataGenerator(
        rotation_range=15,
        horizontal_flip=True,
        vertical_flip=True,
        brightness_range=[0.8, 1.2]
    )

import sqlite3
from sqlite3 import Error
from pathlib import Path
import random


def populate_segmentation_data(db_path="data/metadata.db",
                               data_dir="/content/drive/MyDrive/Skin-Sight/data/processed/segmentation"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 80-10-10 train-val-test split
    splits = ['train'] * 80 + ['val'] * 10 + ['test'] * 10

    for img_path in Path(data_dir).glob('images/*.jpg'):
        mask_path = Path(data_dir) / "masks" / img_path.name
        split = random.choice(splits)

        cursor.execute("""
            INSERT INTO images (id, image_path, mask_path, split_group)
            VALUES (?, ?, ?, ?)
            """, (img_path.stem, str(img_path), str(mask_path), split))

    conn.commit()
    conn.close()

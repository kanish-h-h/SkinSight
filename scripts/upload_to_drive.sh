#!/bin/bash
# Uploads processed data to Google Drive (run in Colab)

# Config
DRIVE_PATH="/content/drive/MyDrive/Skin-Sight/data"
LOCAL_DATA_DIR="data/"

# Check if Drive is mounted
if [ ! -d "$DRIVE_PATH" ]; then
  echo "Mounting Google Drive..."
  python -c "from google.colab import drive; drive.mount('/content/drive')"
fi

# Sync processed data
echo "Uploading data to Google Drive..."
rsync -avz --progress "$LOCAL_DATA_DIR/" "$DRIVE_PATH/processed/"

# Verify
if [ $? -eq 0 ]; then
  echo "✅ Data uploaded to: $DRIVE_PATH/processed/"
else
  echo "❌ Upload failed!"
  exit 1
fi

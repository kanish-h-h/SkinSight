# Skin-Sight Documentation  
<hr>

## Workflow  
<hr>
1. **Data Flow**:  
   Raw Image → Preprocessing → U-Net Segmentation → SRGAN Upscaling → Final Output  
2. **CLI Usage**:  
   ```bash
   bash scripts/run_inference.sh --input_path "path/to/image.jpg"

## DataSet
<hr>

1. Segmentation: ISIC 2018 (CC-BY license).
2. SRGAN Training: DIV2K (non-commercial).


## Hugging Face Hub Setup  
<hr>

1. Install HF CLI: `pip install huggingface_hub`  
2. Login: `huggingface-cli login` (paste API token)  
3. Download models: `bash scripts/download_models.sh`  

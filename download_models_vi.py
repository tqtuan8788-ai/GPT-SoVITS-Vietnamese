from huggingface_hub import snapshot_download
import os

def download_models():
    print("Downloading GPT-SoVITS V2 Pretrained Models...")
    
    # Base directory
    base_dir = "GPT_SoVITS/pretrained_models"
    os.makedirs(base_dir, exist_ok=True)

    # 1. Chinese-Hubert-Base (SSL)
    print("Downloading Chinese-Hubert-Base...")
    snapshot_download(
        repo_id="TencentGameMate/chinese-hubert-base",
        local_dir=f"{base_dir}/chinese-hubert-base",
        local_dir_use_symlinks=False
    )

    # 2. Chinese-Roberta-WWM-Ext-Large (BERT)
    print("Downloading Chinese-Roberta-WWM-Ext-Large...")
    snapshot_download(
        repo_id="hfl/chinese-roberta-wwm-ext-large",
        local_dir=f"{base_dir}/chinese-roberta-wwm-ext-large",
        local_dir_use_symlinks=False
    )

    # 3. GPT-SoVITS V2 Base Models
    print("Downloading GPT-SoVITS V2 Base Models...")
    v2_dir = f"{base_dir}/gsv-v2final-pretrained"
    os.makedirs(v2_dir, exist_ok=True)
    
    snapshot_download(
        repo_id="lj1995/GPT-SoVITS",
        local_dir=v2_dir,
        allow_patterns=[
            "gsv-v2final-pretrained/s1bert25hz-5kh-longer-epoch=12-step=369668.ckpt",
            "gsv-v2final-pretrained/s2G2333k.pth",
            "gsv-v2final-pretrained/s2D2333k.pth",
        ],
        local_dir_use_symlinks=False
    )
    
    # Move files from subdirectory if necessary (snapshot_download preserves structure)
    # The structure from lj1995/GPT-SoVITS inside v2_dir will be gsv-v2final-pretrained/...
    # But we want them directly in v2_dir or handled correctly. 
    # Actually snapshot_download with allow_patterns keeps the folder structure.
    # We need to ensure config.py points to the right place. 
    # Config says: "GPT_SoVITS/pretrained_models/gsv-v2final-pretrained/s2G2333k.pth"
    # So if we download to base_dir, it will create the folder gsv-v2final-pretrained. Perfect.

    snapshot_download(
        repo_id="lj1995/GPT-SoVITS",
        local_dir=base_dir,
        allow_patterns=[
            "gsv-v2final-pretrained/s1bert25hz-5kh-longer-epoch=12-step=369668.ckpt",
            "gsv-v2final-pretrained/s2G2333k.pth",
            "gsv-v2final-pretrained/s2D2333k.pth",
        ],
        local_dir_use_symlinks=False
    )

    print("Download Complete!")

if __name__ == "__main__":
    download_models()

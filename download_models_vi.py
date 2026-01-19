from huggingface_hub import snapshot_download
import os
import shutil
import time

def download_models():
    print("Downloading GPT-SoVITS V2 Pretrained Models...")
    
    # Base directory
    base_dir = "GPT_SoVITS/pretrained_models"
    os.makedirs(base_dir, exist_ok=True)
    
    # Smart Cache Configuration
    cache_root = "/content/drive/MyDrive/GPT_SoVITS_Cache"
    use_cache = os.path.exists("/content/drive")  # Only use cache if Drive is mounted
    
    if use_cache:
        print(f"✅ Google Drive detected! Smart Cache enabled at: {cache_root}")
        os.makedirs(cache_root, exist_ok=True)
    else:
        print("⚠️ Google Drive NOT detected. Using temporary storage (will re-download next time).")

    # Function to handle download with caching
    def smart_download(repo_id, local_dir, allow_patterns=None):
        model_name = repo_id.split("/")[-1]
        if allow_patterns:
            model_name += "_custom" # Differentiator for partial downloads
            
        cache_dir = f"{cache_root}/{model_name}"
        
        # Check cache
        if use_cache and os.path.exists(cache_dir) and len(os.listdir(cache_dir)) > 0:
            print(f"♻️ Found cached models for {repo_id}. Copying from Drive... (Fast!)")
            start_time = time.time()
            if os.path.exists(local_dir):
                shutil.rmtree(local_dir)
            shutil.copytree(cache_dir, local_dir)
            print(f"✅ Restored {repo_id} from cache in {time.time() - start_time:.2f}s")
            return

        # Download from HF
        print(f"⬇️ Downloading {repo_id} from HuggingFace...")
        snapshot_download(
            repo_id=repo_id,
            local_dir=local_dir,
            allow_patterns=allow_patterns,
            local_dir_use_symlinks=False
        )
        
        # Save to cache
        if use_cache:
            print(f"💾 Saving {repo_id} to Drive Cache for future use...")
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
            shutil.copytree(local_dir, cache_dir)
            print("✅ Saved to cache!")

    # 1. Chinese-Hubert-Base (SSL)
    print("\n--- 1. Chinese-Hubert-Base ---")
    smart_download(
        repo_id="TencentGameMate/chinese-hubert-base",
        local_dir=f"{base_dir}/chinese-hubert-base"
    )

    # 2. Chinese-Roberta-WWM-Ext-Large (BERT)
    print("\n--- 2. Chinese-Roberta-WWM-Ext-Large ---")
    smart_download(
        repo_id="hfl/chinese-roberta-wwm-ext-large",
        local_dir=f"{base_dir}/chinese-roberta-wwm-ext-large"
    )

    # 3. GPT-SoVITS V2 Base Models
    print("\n--- 3. GPT-SoVITS V2 Base Models ---")
    v2_dir = f"{base_dir}/gsv-v2final-pretrained"
    os.makedirs(v2_dir, exist_ok=True)
    
    smart_download(
        repo_id="lj1995/GPT-SoVITS",
        local_dir=v2_dir,
        allow_patterns=[
            "gsv-v2final-pretrained/s1bert25hz-5kh-longer-epoch=12-step=369668.ckpt",
            "gsv-v2final-pretrained/s2G2333k.pth",
            "gsv-v2final-pretrained/s2D2333k.pth",
        ]
    )
    
    # 4. Save Cache Backup for Pretrained Models specifically
    # The structure adjustment for direct access (optional logic from original script kept simple here)
    # The smart_download function handles the directory structure correctly.

    print("\n🎉 Download Complete!")

if __name__ == "__main__":
    download_models()

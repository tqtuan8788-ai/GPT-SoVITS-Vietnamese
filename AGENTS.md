# AGENTS.md - Developer Guide & Rules

This document provides instructions for AI agents and developers working on the `GPT-SoVITS-Vietnamese` repository.

## 1. Repository Overview

This project is a Vietnamese localization and optimization of the GPT-SoVITS voice cloning system. It is primarily designed to run on Google Colab (using Jupyter Notebooks) but also contains a Gradio-based WebUI (`webui.py`).

**Key Components:**
*   `GPT_SoVITS_Colab_VI.ipynb`: The main entry point for Colab users. It handles environment setup, data processing, and launching the WebUI.
*   `webui.py`: The core Gradio application for training and inference.
*   `tools/`: Helper scripts for audio slicing (`slice_audio.py`), ASR (`fasterwhisper_asr.py`), and more.
*   `GPT_SoVITS/`: Core model logic (training, inference, model definitions).

## 2. Build, Lint, and Test Commands

This project is script-based and does not use a traditional build system like Make or CMake.

### Testing
There is no formal test suite (e.g., `pytest`) configured in the root. Testing is primarily **manual verification** by running the scripts or the notebook cells.

*   **Single Script Test:** To test a specific tool (e.g., ASR), run it via Python with appropriate arguments:
    ```bash
    python tools/asr/fasterwhisper_asr.py -i "path/to/input" -o "output/dir" -s large-v3 -l vi -p float16
    ```
*   **WebUI Test:** To test the UI launch (ensure environment variables are set):
    ```bash
    python webui.py --share
    ```

### Linting
No explicit linter config (`.flake8`, `pyproject.toml`) is present. Follow PEP 8 standards where possible, but prioritize consistency with the existing codebase (which uses mixed styles due to upstream forks).

## 3. Code Style & Conventions

*   **Language:** Python 3.10+.
*   **Formatting:**
    *   Use 4 spaces for indentation.
    *   Preserve existing imports.
    *   Avoid reordering imports unless necessary for functionality (e.g., setting env vars before importing torch).
*   **Path Handling:**
    *   **CRITICAL:** Always use absolute paths or paths relative to the project root.
    *   **Colab Compatibility:** When modifying `tools/my_utils.py` or similar, ensure paths to binaries (like `ffmpeg`) are not hardcoded to Windows/Local paths. Use general commands (e.g., `ffmpeg` instead of `C:\...\ffmpeg.exe`).
*   **Environment Variables:**
    *   The system relies heavily on `os.environ` to pass state between the Notebook and `webui.py`.
    *   Key vars: `is_share`, `is_half`, `exp_name`, `LD_LIBRARY_PATH`.

## 4. Critical Operational Rules (Context: Colab & H100)

Agents operating here must be aware of the specific deployment environment (Google Colab, often on NVIDIA T4 or H100 GPUs).

### H100 / A100 Support
*   **Library Conflict:** `faster-whisper` and `ctranslate2` often fail to find cuDNN/cuBLAS on Colab H100 instances.
*   **Required Fix:** You MUST ensure `LD_LIBRARY_PATH` includes the nvidia library paths before running inference scripts.
    ```python
    import os
    nvidia_libs = "/usr/local/lib/python3.10/dist-packages/nvidia/cudnn/lib:/usr/local/lib/python3.10/dist-packages/nvidia/cublas/lib"
    os.environ['LD_LIBRARY_PATH'] = nvidia_libs + ":" + os.environ.get('LD_LIBRARY_PATH', '')
    ```
*   **Precision:** Always use `float16` for ASR on GPU. `float32` is significantly slower on Tensor Core GPUs.

### File System
*   **Input Data:** Typically located in `/content/dataset/{exp_name}`.
*   **Output:** typically `output/`.
*   **Model Weights:** `GPT_SoVITS/pretrained_models` (base) and `GPT_weights`/`SoVITS_weights` (finetuned).

### Notebook vs. WebUI
*   **Uploads:** Do NOT attempt to implement large file uploads inside `webui.py` for Colab users. Use the Notebook's direct upload cells (Cell 3) as they are faster and more stable than tunneling through Gradio.
*   **Automation:** Complex setups (Slicing + ASR + Formatting) are often orchestrated in Notebook cells (Cell 4) rather than the WebUI to allow for auto-fixing environment issues (like the ffmpeg patch) that are hard to inject into the pre-made WebUI process.

## 5. Agent Behavior Guidelines

*   **Plan First:** Before modifying the Notebook or `webui.py`, analyze the flow of data (paths, env vars).
*   **Do Not Break Upstream:** Avoid heavily modifying `webui.py` logic if a wrapper script or Notebook cell change can achieve the same goal. This makes merging upstream updates easier.
*   **User Communication:** When the user asks for a UI feature (e.g., "Add upload to UI"), evaluate the technical trade-offs (Performance vs. Convenience) and explain them clearly.
*   **Error Handling:** When running subprocesses (ASR, Slicing), check for empty outputs (`len(files) == 0`) and raise visible errors immediately.

## 6. Known Issues
*   **FFmpeg Path:** `tools/my_utils.py` contains a hardcoded Windows path for FFmpeg. Always apply the `sed` patch in Colab notebooks to fix this.
*   **ASR Speed:** If ASR is slow (>10 mins for short audio), it means it fell back to CPU. Check CUDA drivers and `LD_LIBRARY_PATH`.

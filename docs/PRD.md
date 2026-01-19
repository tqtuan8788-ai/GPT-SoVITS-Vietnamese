# GPT-SoVITS Vietnamese - Product Requirements Document (PRD)

## 1. Tổng quan dự án

### 1.1 Mục tiêu
Tối ưu hóa GPT-SoVITS để tạo công cụ clone giọng nói tiếng Việt đơn giản, ổn định, chạy trên Google Colab.

### 1.2 Vấn đề cần giải quyết
| Vấn đề | Mô tả |
|--------|-------|
| **Lỗi format file** | File `.list` không đúng định dạng 4 trường |
| **Quy trình phức tạp** | Cell 3 chạy liên tục, không thể chạy Cell 4 |
| **Thừa module** | Chứa nhiều ngôn ngữ và tính năng không cần |
| **Thiếu tài liệu** | Hướng dẫn tiếng Anh/Trung, khó cho người Việt |

### 1.3 Giải pháp đề xuất
Fork và tùy chỉnh repo GPT-SoVITS với:
- Loại bỏ module không cần
- Sửa các bug đã phát hiện
- Tối ưu cho tiếng Việt
- Notebook đơn giản 3-4 cell

---

## 2. Phạm vi dự án

### 2.1 Trong phạm vi (In Scope)
- ✅ Vietnamese TTS training pipeline
- ✅ Vietnamese ASR (Whisper)
- ✅ Audio slicing
- ✅ SoVITS + GPT training
- ✅ Inference (tạo giọng nói)
- ✅ Google Colab support (T4/A100)
- ✅ Google Drive integration

### 2.2 Ngoài phạm vi (Out of Scope)
- ❌ Voice Changer (chưa hoàn thiện)
- ❌ Multi-language support (Trung, Nhật, Hàn, Anh)
- ❌ Local GPU training (chỉ focus Colab)
- ❌ Real-time inference

---

## 3. Kiến trúc kỹ thuật

### 3.1 Cấu trúc repo sau khi tối ưu
```
GPT-SoVITS-Vietnamese/
├── GPT_SoVITS/              # Core models
│   ├── pretrained_models/   # Pre-trained weights
│   └── configs/             # Vietnamese configs
├── tools/
│   ├── slice_audio.py       # Audio slicing
│   └── asr/
│       └── faster_whisper_asr.py  # Vietnamese ASR
├── webui.py                 # Simplified WebUI
├── requirements.txt         # Dependencies
├── colab_notebook.ipynb     # Main notebook
└── README_VI.md             # Vietnamese docs
```

### 3.2 Workflow đơn giản hóa

```mermaid
flowchart LR
    A[Upload Audio] --> B[Slice Audio]
    B --> C[ASR Vietnamese]
    C --> D[Format Data]
    D --> E[Train SoVITS]
    E --> F[Train GPT]
    F --> G[Inference]
```

### 3.3 Notebook structure (3-4 cells)
| Cell | Chức năng | Thời gian |
|------|-----------|-----------|
| 1 | Setup + Install | 5-7 min |
| 2 | Upload + Slice + ASR | 5-15 min |
| 3 | WebUI (Training + Inference) | Liên tục |

---

## 4. Chi tiết kỹ thuật các thay đổi

### 4.1 Bug Fixes

#### Fix 1: File `.list` format
**File:** `tools/asr/faster_whisper_asr.py`
```python
# Hiện tại output:
text_content

# Cần sửa thành:
absolute_path|speaker_name|vi|text_content
```

#### Fix 2: Variable passing
**File:** `webui.py`, `tools/my_utils.py`
- Thêm validation cho input paths
- Truyền `exp_name` qua environment variable

#### Fix 3: Path synchronization
**Files:** Multiple
- Đồng bộ `output/slicer_opt` giữa slicing và ASR
- Auto-detect output folder names

### 4.2 Module Removal

| Module | Files cần xóa/sửa | Lý do |
|--------|-------------------|-------|
| Voice Changer | `tools/vc_*.py` | Chưa hoàn thiện |
| Chinese G2PW | `GPT_SoVITS/text/G2PWModel/` | Không cần cho tiếng Việt |
| Multi-lang TTS | `i18n/` (giữ lại `vi_VN.json`) | Chỉ cần tiếng Việt |

### 4.3 Vietnamese Defaults
```python
# configs/vietnamese_defaults.py
DEFAULT_CONFIG = {
    "asr_model": "large-v3",
    "asr_language": "vi",
    "asr_precision": "float32",
    "sovits_epochs": 8,
    "gpt_epochs": 15,
    "batch_size_t4": 8,
    "batch_size_a100": 32
}
```

---

## 5. Kế hoạch triển khai

### 5.1 Timeline
| Phase | Công việc | Thời gian |
|-------|-----------|-----------|
| 1 | Setup & Research | 30 phút |
| 2 | Bug Fixes | 1 giờ |
| 3 | Optimization | 1 giờ |
| 4 | Colab Integration | 30 phút |
| 5 | Documentation | 30 phút |
| 6 | Testing | 30 phút |
| **Tổng** | | **~4 giờ** |

### 5.2 Deliverables
1. **GitHub Repository:** `GPT-SoVITS-Vietnamese`
2. **Colab Notebook:** Optimized 3-cell notebook
3. **Documentation:** README tiếng Việt + Troubleshooting guide
4. **Pre-trained models:** Hosted on Google Drive/Hugging Face

---

## 6. Tiêu chí hoàn thành (Definition of Done)

- [ ] Notebook chạy end-to-end trên Colab T4 không lỗi
- [ ] Notebook chạy end-to-end trên Colab A100 không lỗi
- [ ] Training hoàn tất trong < 30 phút với 5 phút audio
- [ ] Inference tạo giọng chất lượng tốt
- [ ] Hướng dẫn tiếng Việt hoàn chỉnh
- [ ] Không có lỗi format file `.list`

---

## 7. Rủi ro và giảm thiểu

| Rủi ro | Mức độ | Giảm thiểu |
|--------|--------|------------|
| Upstream GPT-SoVITS update | Thấp | Pin version cụ thể |
| Colab runtime timeout | Trung bình | Checkpoint saving to Drive |
| Model quality | Thấp | Test với nhiều loại giọng |

---

## User Review Required

> [!IMPORTANT]
> Vui lòng review và cho biết:
> 1. PRD này đã đầy đủ chưa?
> 2. Bạn muốn thêm/bớt feature nào?
> 3. Có muốn tôi bắt đầu thực hiện Phase 1 không?

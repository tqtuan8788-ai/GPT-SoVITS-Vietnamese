# 🇻🇳 GPT-SoVITS Vietnamese

Phiên bản tối ưu của [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) dành cho **clone giọng nói tiếng Việt** trên Google Colab.

## ✨ Tính năng

- 🎯 Tối ưu cho tiếng Việt (Whisper large-v3 + ASR)
- 🚀 Notebook đơn giản 4 cell
- 📱 Chạy trên Google Colab (T4/A100)
- 💾 Tích hợp Google Drive backup

## 🚀 Bắt đầu nhanh

### Bước 1: Mở Notebook trên Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tqtuan8788-ai/GPT-SoVITS-Vietnamese/blob/main/GPT_SoVITS_Colab_VI.ipynb)

### Bước 2: Chạy theo thứ tự

| Cell | Chức năng | Thời gian |
|------|-----------|-----------|
| 1️⃣ | Cài đặt & Tải Model | 5-7 phút |
| 2️⃣ | WebUI Tiếng Việt (Full features) | Liên tục |
| 3️⃣ | Sao lưu Drive | 1 phút |

## 📋 Yêu cầu

- Tài khoản Google (để dùng Colab)
- File audio giọng nói (tối thiểu 1-3 phút, khuyến nghị 5-10 phút)
- Định dạng: `.mp3`, `.wav`, `.flac`

## 📖 Hướng dẫn chi tiết

Xem file [HUONG_DAN_SU_DUNG.md](./HUONG_DAN_SU_DUNG.md)

## 🔧 Khắc phục lỗi

### Lỗi: `ValueError: not enough values to unpack`
→ File `.list` sai định dạng. Chạy lại Cell 2.

### Lỗi: `IsADirectoryError`
→ Điền đường dẫn file `.list`, không phải folder.

### Lỗi: `Warning: No Such Model v2Pro`
→ Chọn Model Version: v2 thay vì v2Pro.

## 📄 License

MIT License - Xem file [LICENSE](./LICENSE)

## 🙏 Credits

- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - Dự án gốc
- [OpenAI Whisper](https://github.com/openai/whisper) - ASR model

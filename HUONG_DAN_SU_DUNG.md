# HƯỚNG DẪN CHI TIẾT SỬ DỤNG GPT-SoVITS v2 (PHIÊN BẢN ĐÃ SỬA)

Tài liệu này hướng dẫn bạn từng bước để tạo giọng nói nhân tạo (AI Voice) chất lượng cao bằng Google Colab.

> **✅ ĐÃ SỬA:** Notebook đã được tái cấu trúc để quy trình chạy hợp lý hơn.

---

## CẤU TRÚC NOTEBOOK MỚI

| Cell | Tên | Trạng thái | Mục đích |
|------|-----|------------|----------|
| **1** | Cài đặt môi trường | Chạy xong dừng | Cài thư viện, tải models |
| **2** | Tải dữ liệu | Chạy xong dừng | Upload file âm thanh |
| **3** | Cắt Audio + ASR | Chạy xong dừng | Cắt + tạo phụ đề tiếng Việt |
| **4** | Khởi động WebUI | **Chạy liên tục** | Mở giao diện làm việc |
| **5** | Lưu model | Chạy xong dừng | Backup về Google Drive |

---

## GIAI ĐOẠN 1: CHUẨN BỊ (Cell 1-2)

### Cell 1: Cài đặt môi trường
1. Bấm nút "Play" ở Cell 1
2. Chờ 5-7 phút đến khi thấy `✅ Cài đặt hoàn tất!`

### Cell 2: Tải dữ liệu
1. **source_type:** Chọn `Direct Upload` hoặc `Google Drive`
2. **exp_name:** Đặt tên (VD: `Giong_Doc_Sach_01`) - **Nhớ kỹ tên này!**
3. Bấm "Play" và upload file âm thanh (.mp3/.wav)

---

## GIAI ĐOẠN 2: CẮT AUDIO + ASR (Cell 3)

> **💡 Đây là cell quan trọng nhất - chuẩn bị toàn bộ dữ liệu trước khi mở WebUI**

### Cell 3: Cắt Audio + Tạo Phụ Đề Tiếng Việt
1. **exp_name:** Điền đúng tên bạn đặt ở Cell 2
2. Bấm "Play"
3. Chờ quá trình hoàn tất (5-15 phút)

**Cell 3 sẽ tự động:**
- 🔪 Cắt audio dài thành các đoạn ngắn 3-10 giây
- 🎤 Chạy Whisper large-v3 để nhận dạng tiếng Việt
- 📄 Tạo file `.list` với định dạng chuẩn

**Kết quả mong đợi:**
```
✅ ĐÃ TẠO FILE .LIST THÀNH CÔNG!
📄 Đường dẫn: /content/GPT-SoVITS/output/Giong_Doc_Sach_01.list
📝 Tổng số dòng: 50
```

**👉 COPY đường dẫn file .list hiển thị ở cuối Cell 3!**

---

## GIAI ĐOẠN 3: WEBUI - TRAINING (Cell 4)

### Cell 4: Khởi động WebUI
1. Bấm "Play" 
2. Chờ 1-2 phút đến khi thấy link `gradio.live`
3. Bấm vào link đó để mở WebUI

> ⚠️ **Cell 4 sẽ chạy liên tục.** Đừng tắt nó!

---

### Trên WebUI: Tab 1 → 1A - Format Data

1. **Tên thử nghiệm/mô hình:** Điền `Giong_Doc_Sach_01` (tên bạn đặt)
2. **Đường dẫn tệp văn bản nhãn:** PASTE đường dẫn file `.list` từ Cell 3
   ```
   /content/GPT-SoVITS/output/Giong_Doc_Sach_01.list
   ```
3. Bấm **"Mở bộ dữ liệu huấn luyện, định dạng chỉ bằng một cú nhấp chuột"**
4. Chờ thông báo "Success"

---

### Trên WebUI: Tab 1 → 1B - Training

#### Train SoVITS (Học chất giọng)
| Thông số | GPU T4 (Free) | GPU A100 (Pro) |
|----------|---------------|----------------|
| Batch size | 8 | 32-39 |
| Total epochs | 8 | 8 |

Bấm **"Khóa đào tạo Open SoVITS"** → Chờ hoàn tất

#### Train GPT (Học ngữ điệu)
| Thông số | GPU T4 (Free) | GPU A100 (Pro) |
|----------|---------------|----------------|
| Batch size | 8 | 32-39 |
| Total epochs | 15 | 15 |

Bấm **"Đào tạo GPT mở"** → Chờ hoàn tất (bước này lâu nhất)

---

## GIAI ĐOẠN 4: SỬ DỤNG (Tab 1C)

### Tab 1 → 1C - Inference
1. Bấm **"làm mới các đường dẫn mô hình"**
2. **GPT Model:** Chọn file `.ckpt` (chọn số e lớn nhất, VD: `e15`)
3. **SoVITS Model:** Chọn file `.pth` (chọn số e lớn nhất, VD: `e8`)
4. Bấm **"Mở giao diện web TTS Inference"**

### Tạo giọng nói:
1. **Upload Reference Audio:** File .wav ngắn 3-10s từ giọng gốc
2. **Reference Text:** Nội dung file mẫu đang nói
3. **Inference Text:** Nội dung muốn AI đọc
4. **Language:** Chọn Tiếng Việt
5. Bấm **Start Inference**

---

## GIAI ĐOẠN 5: LƯU MODEL (Cell 5)

Sau khi train xong, quay lại Colab chạy **Cell 5** để lưu model về Google Drive.

---

## XỬ LÝ LỖI THƯỜNG GẶP

### Lỗi: `ValueError: not enough values to unpack (expected 4, got 1)`
**Nguyên nhân:** File `.list` sai định dạng
**Cách sửa:** Chạy lại Cell 3 để tạo file `.list` đúng định dạng

### Lỗi: `IsADirectoryError: Is a directory`
**Nguyên nhân:** Ô "Text Label File" chứa đường dẫn folder thay vì file
**Cách sửa:** Điền đường dẫn đến file `.list`, không phải folder

### Lỗi: `FileNotFoundError: logs/xxx/...`
**Nguyên nhân:** Chưa chạy Cell 3 hoặc điền sai đường dẫn
**Cách sửa:** Chạy lại Cell 3, copy đúng đường dẫn file `.list`

### Lỗi: `Warning: No Such Model v2Pro`
**Cách sửa:** Chọn **Model Version: v2** thay vì v2Pro

---

**🎉 Chúc mừng! Bạn đã hoàn thành việc tạo bản sao giọng nói tiếng Việt.**

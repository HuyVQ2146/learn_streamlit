# Hướng Dẫn Môi Trường Conda & Vận Hành Streamlit

Tài liệu tóm tắt quy trình thiết lập, quản lý môi trường ảo Conda và các thao tác vận hành ứng dụng Streamlit.

---

## 1. Quản lý Môi trường ảo (Conda Environment)

### Kích hoạt môi trường (Activate)
Để kích hoạt môi trường làm việc `streamlit_env`, chạy lệnh sau trong **Anaconda Prompt**, **PowerShell** hoặc **Terminal tích hợp (VS Code)**:

```bash
conda activate streamlit_env
```

**Ghi chú:** Sau khi kích hoạt thành công, tiền tố `(streamlit_env)` sẽ xuất hiện ở đầu dòng lệnh.

### Thoát khỏi môi trường (Deactivate)
Khi hoàn tất công việc và muốn quay về môi trường gốc (`base`):

```bash
conda deactivate
```

---

## 2. Khởi chạy Ứng dụng Streamlit

### Lệnh chạy file
Di chuyển vào thư mục chứa mã nguồn (ví dụ: `C:\Code\AIO\2027\Warm up 1\Week 5`) và thực thi:

```bash
streamlit run main.py
```

### Kết quả hiển thị (Output mẫu)
```text
(streamlit_env) C:\Code\AIO\2027\Warm up 1\Week 5>streamlit run main.py
2026-10-21 14:30:17.903 Uvicorn server started on :::8502

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8502
  Network URL: http://192.168.1.126:8502

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.
```

### Giải thích các thông số:
* **Local URL (`http://localhost:8502`):** Địa chỉ truy cập ứng dụng trực tiếp trên chính máy tính của bạn thông qua trình duyệt web.
* **Network URL (`http://192.168.1.126:8502`):** Địa chỉ IP nội bộ, cho phép các thiết bị khác (điện thoại, máy tính khác) cùng kết nối chung mạng Wi-Fi/LAN truy cập thử nghiệm giao diện.
* **Cổng (Port 8502):** Streamlit mặc định dùng cổng `8501`. Nếu cổng `8501` đang bận hoặc có tiến trình khác đang chạy, Streamlit sẽ tự động chuyển sang `8502`.

---

## 3. Bảo Mật & Tùy Chọn Khởi Chạy (Local vs Network URL)

### Network URL có an toàn không?

* **Phạm vi truy cập:** Chỉ các thiết bị kết nối **chung một mạng Wi-Fi hoặc mạng LAN** mới truy cập được. Người ngoài Internet (dùng 4G/5G hoặc mạng khác) **không thể** truy cập.
* **Wi-Fi gia đình:** An toàn và rất tiện lợi để dùng điện thoại tự kiểm tra giao diện responsive.
* **Wi-Fi công cộng (quán cafe, trường học, ký túc xá):** Tiềm ẩn nguy cơ người lạ trong cùng mạng quét IP và truy cập xem giao diện ứng dụng hoặc dữ liệu đang hiển thị trên web.

### Cách tắt Network URL (Khóa chỉ cho phép máy nội bộ truy cập)

Khi làm việc tại môi trường mạng công cộng, để bảo mật tuyệt đối, hãy thêm cờ `--server.address localhost`:

```bash
streamlit run main.py --server.address localhost
```

**Tác dụng:** Streamlit sẽ chỉ lắng nghe trên `localhost` (127.0.0.1) và không hiển thị `Network URL`, ngăn chặn hoàn toàn các thiết bị khác trong cùng mạng truy cập.

---

## 4. Cách dừng Server Streamlit

Để tắt ứng dụng và giải phóng terminal:

* Nhấp chuột vào cửa sổ terminal đang chạy server.
* Nhấn tổ hợp phím **`Ctrl + C`**.

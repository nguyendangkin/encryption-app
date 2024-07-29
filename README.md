Dưới đây là mẫu README cho ứng dụng mã hóa và giải mã của bạn. Bạn có thể điều chỉnh nội dung để phù hợp với yêu cầu cụ thể và thông tin về ứng dụng của bạn.

````markdown
# Ứng Dụng Mã Hóa/Giải Mã

Ứng dụng Mã hóa/Giải mã sử dụng Python và Tkinter để mã hóa và giải mã nội dung văn bản. Ứng dụng này hỗ trợ nhập và lưu key từ file, mã hóa và giải mã văn bản, và sao chép kết quả vào clipboard hoặc lưu vào file.

## Các Tính Năng

-   **Nhập Key**: Nhập key trực tiếp hoặc từ file.
-   **Nhập Nội Dung**: Nhập nội dung cần mã hóa/giải mã hoặc tải từ file.
-   **Mã Hóa**: Mã hóa nội dung với key đã cung cấp.
-   **Giải Mã**: Giải mã nội dung mã hóa với key đã cung cấp.
-   **Sao Chép Kết Quả**: Sao chép kết quả mã hóa/giải mã vào clipboard.
-   **Lưu Kết Quả**: Lưu kết quả vào file.

## Yêu Cầu

-   Python 3.8 hoặc phiên bản mới hơn
-   Tkinter
-   Cryptography

## Cài Đặt

1. **Cài đặt Python 3.8 hoặc phiên bản mới hơn**

    ```sh
    sudo apt update
    sudo apt install python3 python3-pip
    ```
````

2. **Cài đặt các thư viện cần thiết**

    ```sh
    pip3 install cryptography
    ```

3. **Tải mã nguồn của ứng dụng**

    Tải mã nguồn từ kho lưu trữ hoặc sao chép tệp `encryption_app.py` vào thư mục làm việc của bạn.

## Cách Sử Dụng

1. **Chạy ứng dụng**

    ```sh
    python3 encryption_app.py
    ```

2. **Nhập Key**

    - Nhập key vào trường văn bản hoặc nhấp vào nút "Chọn file key" để tải key từ file.

3. **Nhập Nội Dung**

    - Nhập nội dung cần mã hóa/giải mã vào trường văn bản hoặc nhấp vào nút "Tải lên file nội dung" để tải nội dung từ file.

4. **Mã Hóa**

    - Nhấp vào nút "Mã hóa" để mã hóa nội dung.

5. **Giải Mã**

    - Nhấp vào nút "Giải mã" để giải mã nội dung đã mã hóa.

6. **Sao Chép Kết Quả**

    - Nhấp vào nút "Copy kết quả" để sao chép kết quả vào clipboard.

7. **Lưu Kết Quả**
    - Nhấp vào nút "Tải về file kết quả" để lưu kết quả vào file.

## Đóng Gói Ứng Dụng

Để đóng gói ứng dụng thành tệp thực thi, hãy sử dụng PyInstaller:

1. **Cài đặt PyInstaller**

    ```sh
    pip3 install pyinstaller
    ```

2. **Đóng gói ứng dụng**

    ```sh
    pyinstaller --onefile --windowed encryption_app.py
    ```

3. **Tìm tệp thực thi**

    Tệp thực thi sẽ được tạo trong thư mục `dist`.

## Giới Thiệu

Ứng dụng này được phát triển để cung cấp một công cụ đơn giản cho việc mã hóa và giải mã văn bản bằng cách sử dụng thư viện `cryptography` trong Python. Đối tượng người dùng có thể dễ dàng nhập, mã hóa, giải mã và lưu trữ nội dung văn bản.

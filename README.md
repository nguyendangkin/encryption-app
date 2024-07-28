### Ứng dụng Mã hóa/Giải mã

Ứng dụng PyQt6 này cho phép người dùng mã hóa và giải mã văn bản bằng cách sử dụng thuật toán Fernet. Fernet là một phương pháp mã hóa đối xứng cung cấp tính toàn vẹn và bảo mật của dữ liệu. Ứng dụng hỗ trợ việc nhập thủ công hoặc tải lên file chứa key và nội dung cần mã hóa/giải mã, cũng như sao chép hoặc lưu kết quả vào file.

#### Các tính năng chính:

1. **Nhập key và nội dung**:

    - Người dùng có thể nhập key thủ công hoặc chọn từ một file key có sẵn.
    - Nội dung cần mã hóa hoặc giải mã cũng có thể được nhập thủ công hoặc tải từ một file văn bản.

2. **Mã hóa và giải mã**:

    - Ứng dụng cho phép mã hóa văn bản sử dụng key nhập vào.
    - Giải mã văn bản đã mã hóa bằng cách sử dụng cùng key.
    - Kết quả mã hóa/giải mã được hiển thị trong ứng dụng và có thể sao chép hoặc lưu vào file.

3. **Sao chép và lưu kết quả**:
    - Kết quả mã hóa hoặc giải mã có thể được sao chép vào clipboard để sử dụng nhanh chóng.
    - Kết quả cũng có thể được lưu vào file văn bản để sử dụng sau.

#### Tính bảo mật và kháng tấn công:

1. **Fernet**:

    - Fernet là một phương pháp mã hóa đối xứng thuộc họ mã hóa AES (Advanced Encryption Standard), sử dụng khóa 256-bit.
    - Fernet cung cấp tính toàn vẹn và bảo mật của dữ liệu bằng cách kết hợp mã hóa và xác thực, ngăn chặn việc giả mạo và thay đổi dữ liệu.

2. **Khả năng kháng tấn công của key**:

    - Ứng dụng sử dụng PBKDF2 (Password-Based Key Derivation Function 2) với SHA-256 để tạo ra key mã hóa từ mật khẩu người dùng nhập vào.
    - PBKDF2 sử dụng một salt ngẫu nhiên và thực hiện nhiều lần lặp (iterations) để tăng độ phức tạp của quá trình tạo key, làm chậm lại các cuộc tấn công brute force.

3. **Độ phức tạp của key và khả năng tấn công brute force**:
    - Key có độ phức tạp cao như "Xj9#mK2$pL7@qR4^vF6\*bN8&zC3" sử dụng các ký tự đặc biệt, chữ cái viết hoa và viết thường, cũng như chữ số, làm tăng đáng kể độ phức tạp của key.
    - Với key 256-bit, số lượng các key có thể là \(2^{256}\) (khoảng \(1.15 \times 10^{77}\) key khác nhau).
    - Giả sử một hacker sử dụng máy tính mạnh nhất hiện nay (có thể thử \(10^{12}\) key mỗi giây), thì thời gian để thử hết tất cả các key sẽ là \(1.15 \times 10^{65}\) giây.
    - Với tốc độ này, hacker sẽ mất khoảng \(3.65 \times 10^{57}\) năm để thử hết tất cả các key có thể, vượt quá tuổi của vũ trụ (khoảng 13.8 tỷ năm).
    - Key như "Xj9#mK2$pL7@qR4^vF6\*bN8&zC3" có độ dài 32 ký tự và bao gồm nhiều loại ký tự khác nhau, khiến việc dự đoán hoặc brute force key trở nên cực kỳ khó khăn, ngay cả với các hệ thống tấn công tiên tiến.

#### Tổng kết:

Ứng dụng mã hóa/giải mã này cung cấp một công cụ mạnh mẽ và an toàn để bảo vệ thông tin của người dùng. Bằng cách sử dụng các thuật toán mã hóa hiện đại và phương pháp tạo key an toàn, ứng dụng đảm bảo rằng dữ liệu của người dùng được bảo vệ khỏi các cuộc tấn công mã hóa. Khả năng mã hóa và giải mã văn bản một cách linh hoạt và dễ dàng cũng giúp người dùng quản lý và bảo vệ thông tin của mình hiệu quả hơn. Các key phức tạp như "Xj9#mK2$pL7@qR4^vF6\*bN8&zC3" mang lại một mức độ bảo mật rất cao, làm cho việc tấn công brute force trở nên không thực tế đối với các hacker.

## Chức năng chính

-   **Nhập key**: Người dùng có thể nhập key thủ công hoặc chọn file key từ hệ thống.
-   **Nhập nội dung**: Người dùng có thể nhập nội dung cần mã hóa/giải mã thủ công hoặc tải lên file nội dung từ hệ thống.
-   **Mã hóa**: Mã hóa nội dung với key đã nhập.
-   **Giải mã**: Giải mã nội dung với key đã nhập.
-   **Copy kết quả**: Sao chép kết quả mã hóa/giải mã vào clipboard.
-   **Lưu kết quả**: Lưu kết quả mã hóa/giải mã vào file văn bản.

## Yêu cầu

-   Python 3.x
-   PyQt6
-   cryptography

## Cài đặt và chạy từ source

1. Cài đặt các thư viện cần thiết:

    ```bash
    pip install PyQt6 cryptography
    ```

2. Chạy ứng dụng:
    ```bash
    python your_script_name.py
    ```

## Chạy ứng dụng từ file thực thi (exe)

1. Tải file thực thi từ phần phát hành (release).
2. Giải nén file nếu cần.
3. Chạy file thực thi (`.exe`).

## Sử dụng

### Nhập key

-   Người dùng có thể nhập key vào ô nhập hoặc nhấn nút "Chọn file key" để chọn file chứa key từ hệ thống.

### Nhập nội dung

-   Người dùng có thể nhập nội dung vào ô nhập hoặc nhấn nút "Tải lên file nội dung" để chọn file chứa nội dung từ hệ thống.

### Mã hóa

-   Nhập key và nội dung cần mã hóa.
-   Nhấn nút "Mã hóa".
-   Kết quả mã hóa sẽ được hiển thị trong ô kết quả.

### Giải mã

-   Nhập key và nội dung đã mã hóa.
-   Nhấn nút "Giải mã".
-   Kết quả giải mã sẽ được hiển thị trong ô kết quả.

### Copy kết quả

-   Nhấn nút "Copy kết quả" để sao chép kết quả mã hóa/giải mã vào clipboard.

### Lưu kết quả

-   Nhấn nút "Tải về file kết quả" để lưu kết quả mã hóa/giải mã vào file văn bản.

## Định dạng key yêu cầu

Để đảm bảo tính an toàn, key nên chứa các ký tự đặc biệt và có độ phức tạp cao. Ví dụ về key an toàn: `Xj9#mK2$pL7@qR4^vF6*bN8&zC3`.

## Ví dụ key

-   `Xj9#mK2$pL7@qR4^vF6*bN8&zC3`

### Thông tin chi tiết

-   **Độ dài**: 28 ký tự
-   **Chữ cái in hoa**: 6 ký tự
-   **Chữ cái in thường**: 8 ký tự
-   **Số**: 6 ký tự
-   **Ký tự đặc biệt**: 8 ký tự

## Lưu ý

-   Đảm bảo rằng key và nội dung được nhập đúng định dạng để tránh lỗi trong quá trình mã hóa/giải mã.
-   Luôn lưu trữ key một cách an toàn và không chia sẻ nó công khai.

Chúc các bạn sử dụng ứng dụng thành công!

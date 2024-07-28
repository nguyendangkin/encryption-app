import sys
import base64
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLabel, QFileDialog, QMessageBox
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ứng dụng Mã hóa/Giải mã')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Key input
        key_layout = QHBoxLayout()
        self.key_input = QTextEdit()
        self.key_input.setPlaceholderText("Nhập key hoặc chọn file key")
        key_layout.addWidget(self.key_input)
        key_file_btn = QPushButton("Chọn file key")
        key_file_btn.clicked.connect(self.load_key_file)
        key_layout.addWidget(key_file_btn)
        layout.addLayout(key_layout)

        # Message input
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Nhập nội dung cần mã hóa/giải mã hoặc chọn file")
        layout.addWidget(self.message_input)

        # Buttons
        btn_layout = QHBoxLayout()
        encrypt_btn = QPushButton("Mã hóa")
        encrypt_btn.clicked.connect(self.encrypt)
        btn_layout.addWidget(encrypt_btn)

        decrypt_btn = QPushButton("Giải mã")
        decrypt_btn.clicked.connect(self.decrypt)
        btn_layout.addWidget(decrypt_btn)

        load_file_btn = QPushButton("Tải file nội dung")
        load_file_btn.clicked.connect(self.load_content_file)
        btn_layout.addWidget(load_file_btn)

        layout.addLayout(btn_layout)

        # Result output
        result_layout = QHBoxLayout()
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)
        result_layout.addWidget(self.result_output)

        copy_btn = QPushButton("Copy kết quả")
        copy_btn.clicked.connect(self.copy_result)
        result_layout.addWidget(copy_btn)

        layout.addLayout(result_layout)

        self.setLayout(layout)

    def generate_key(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def encrypt_message(self, message, key):
        f = Fernet(key)
        encrypted_message = f.encrypt(message.encode('utf-8'))
        return encrypted_message

    def decrypt_message(self, encrypted_message, key):
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message).decode('utf-8')
        return decrypted_message

    def load_key_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Chọn file key")
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.key_input.setPlainText(file.read().strip())

    def load_content_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Chọn file nội dung")
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.message_input.setPlainText(file.read().strip())

    def encrypt(self):
        password = self.key_input.toPlainText().strip().encode('utf-8')
        message = self.message_input.toPlainText().strip()
        
        if not password or not message:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập cả key và nội dung.")
            return

        salt = os.urandom(16)
        key = self.generate_key(password, salt)
        encrypted = self.encrypt_message(message, key)
        result = base64.urlsafe_b64encode(salt + encrypted).decode()
        self.result_output.setPlainText(result)

    def decrypt(self):
        password = self.key_input.toPlainText().strip().encode('utf-8')
        encrypted_input = self.message_input.toPlainText().strip()

        if not password or not encrypted_input:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập cả key và nội dung đã mã hóa.")
            return

        try:
            decoded = base64.urlsafe_b64decode(encrypted_input)
            salt = decoded[:16]
            encrypted = decoded[16:]
            key = self.generate_key(password, salt)
            decrypted = self.decrypt_message(encrypted, key)
            self.result_output.setPlainText(decrypted)
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi giải mã: {str(e)}")

    def copy_result(self):
        result = self.result_output.toPlainText()
        if result:
            clipboard = QApplication.clipboard()
            clipboard.setText(result)
            QMessageBox.information(self, "Thông báo", "Đã sao chép kết quả vào clipboard!")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Không có kết quả để sao chép!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EncryptionApp()
    ex.show()
    sys.exit(app.exec())
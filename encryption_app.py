import sys
import base64
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

class EncryptionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ứng dụng Mã hóa/Giải mã")
        self.geometry("1500x1000")
        
        # Key input
        key_frame = tk.Frame(self)
        key_frame.pack(fill=tk.X)
        
        self.key_input = ScrolledText(key_frame, height=4)
        self.key_input.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        key_file_btn = tk.Button(key_frame, text="Chọn file key", command=self.load_key_file)
        key_file_btn.pack(side=tk.RIGHT)
        
        # Message input
        self.message_input = ScrolledText(self, height=10)
        self.message_input.pack(fill=tk.BOTH, expand=True)
        
        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X)
        
        encrypt_btn = tk.Button(btn_frame, text="Mã hóa", command=self.encrypt)
        encrypt_btn.pack(side=tk.LEFT)
        
        decrypt_btn = tk.Button(btn_frame, text="Giải mã", command=self.decrypt)
        decrypt_btn.pack(side=tk.LEFT)
        
        load_file_btn = tk.Button(btn_frame, text="Tải lên file nội dung/ mã hóa", command=self.load_content_file)
        load_file_btn.pack(side=tk.LEFT)
        
        # Result output
        self.result_output = ScrolledText(self, height=10, state=tk.DISABLED)
        self.result_output.pack(fill=tk.BOTH, expand=True)
        
        result_btn_frame = tk.Frame(self)
        result_btn_frame.pack(fill=tk.X)
        
        copy_btn = tk.Button(result_btn_frame, text="Copy kết quả", command=self.copy_result)
        copy_btn.pack(side=tk.LEFT)
        
        save_btn = tk.Button(result_btn_frame, text="Tải về file kết quả", command=self.save_result_to_file)
        save_btn.pack(side=tk.LEFT)

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
        file_name = filedialog.askopenfilename(title="Chọn file key", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.key_input.delete(1.0, tk.END)
                self.key_input.insert(tk.END, file.read().strip())

    def load_content_file(self):
        file_name = filedialog.askopenfilename(title="Chọn file nội dung", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.message_input.delete(1.0, tk.END)
                self.message_input.insert(tk.END, file.read().strip())

    def encrypt(self):
        password = self.key_input.get(1.0, tk.END).strip().encode('utf-8')
        message = self.message_input.get(1.0, tk.END).strip()
        
        if not password or not message:
            messagebox.showwarning("Lỗi", "Vui lòng nhập cả key và nội dung.")
            return

        salt = os.urandom(16)
        key = self.generate_key(password, salt)
        encrypted = self.encrypt_message(message, key)
        result = base64.urlsafe_b64encode(salt + encrypted).decode()
        
        self.result_output.config(state=tk.NORMAL)
        self.result_output.delete(1.0, tk.END)
        self.result_output.insert(tk.END, result)
        self.result_output.config(state=tk.DISABLED)

    def decrypt(self):
        password = self.key_input.get(1.0, tk.END).strip().encode('utf-8')
        encrypted_input = self.message_input.get(1.0, tk.END).strip()

        if not password or not encrypted_input:
            messagebox.showwarning("Lỗi", "Vui lòng nhập cả key và nội dung đã mã hóa.")
            return

        try:
            decoded = base64.urlsafe_b64decode(encrypted_input)
            salt = decoded[:16]
            encrypted = decoded[16:]
            key = self.generate_key(password, salt)
            decrypted = self.decrypt_message(encrypted, key)
            
            self.result_output.config(state=tk.NORMAL)
            self.result_output.delete(1.0, tk.END)
            self.result_output.insert(tk.END, decrypted)
            self.result_output.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi giải mã: {str(e)}")

    def copy_result(self):
        result = self.result_output.get(1.0, tk.END).strip()
        if result:
            self.clipboard_clear()
            self.clipboard_append(result)
            messagebox.showinfo("Thông báo", "Đã sao chép kết quả vào clipboard!")
        else:
            messagebox.showwarning("Cảnh báo", "Không có kết quả để sao chép!")

    def save_result_to_file(self):
        result = self.result_output.get(1.0, tk.END).strip()
        if result:
            file_name = filedialog.asksaveasfilename(title="Lưu kết quả", defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
            if file_name:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(result)
                messagebox.showinfo("Thông báo", "Đã lưu kết quả vào file!")
        else:
            messagebox.showwarning("Cảnh báo", "Không có kết quả để lưu!")

if __name__ == "__main__":
    app = EncryptionApp()
    app.mainloop()

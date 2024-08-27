import os
import base64
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog, messagebox
from getpass import getpass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend


# Derive a strong key from the password
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


# Encrypt data using AES
def encrypt_data(data: bytes, key: bytes) -> bytes:
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv + ciphertext  # Combine IV with the ciphertext


# Decrypt data using AES
def decrypt_data(data: bytes, key: bytes) -> bytes:
    iv = data[:16]  # Extract the IV
    encrypted_data = data[16:]  # The actual encrypted data

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    return unpadder.update(padded_data) + unpadder.finalize()


# Encrypt a single file
def encrypt_file(file_path: str, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt)

    with open(file_path, 'rb') as file:
        file_data = file.read()

    encrypted_data = encrypt_data(file_data, key)

    with open(file_path + '.enc', 'wb') as file:
        file.write(base64.b64encode(salt + encrypted_data))

    os.remove(file_path)  # Remove the original file


# Decrypt a single file
def decrypt_file(file_path: str, password: str, master_password: str):
    with open(file_path, 'rb') as file:
        encrypted_data = base64.b64decode(file.read())

    salt = encrypted_data[:16]
    key = derive_key(password, salt)

    try:
        decrypted_data = decrypt_data(encrypted_data[16:], key)
    except Exception:
        # If decryption fails, try the master key
        key = derive_key(master_password, salt)
        decrypted_data = decrypt_data(encrypted_data[16:], key)

    with open(file_path[:-4], 'wb') as file:  # Remove '.enc' from the filename
        file.write(decrypted_data)

    os.remove(file_path)  # Remove the encrypted file


# Encrypt a directory recursively
def encrypt_directory(directory_path: str, password: str):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, password)


# Decrypt a directory recursively
def decrypt_directory(directory_path: str, password: str, master_password: str):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.enc'):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, password, master_password)


# GUI Application with Color
class EncryptionApp:
    def __init__(self, master):
        self.master = master
        master.title("Encryption Tool")

        # Colors
        self.bg_color = "#1f1f1f"  # Dark background color
        self.fg_color = "#ffffff"  # White text color
        self.button_color = "#007acc"  # Blue button color
        self.entry_bg_color = "#2c2c2c"  # Darker background for entry
        self.entry_fg_color = "#ffffff"  # White text color for entry

        master.configure(bg=self.bg_color)

        self.label = Label(master, text="Select a file or directory to encrypt/decrypt:", bg=self.bg_color, fg=self.fg_color)
        self.label.pack(pady=10)

        self.path_entry = Entry(master, width=50, bg=self.entry_bg_color, fg=self.entry_fg_color, insertbackground=self.fg_color)
        self.path_entry.pack(pady=5)

        self.browse_button = Button(master, text="Browse", command=self.browse, bg=self.button_color, fg=self.fg_color)
        self.browse_button.pack(pady=5)

        self.password_label = Label(master, text="Enter Password:", bg=self.bg_color, fg=self.fg_color)
        self.password_label.pack(pady=10)

        self.password_entry = Entry(master, show='*', bg=self.entry_bg_color, fg=self.entry_fg_color, insertbackground=self.fg_color)
        self.password_entry.pack(pady=5)

        self.master_password_label = Label(master, text="Enter Master Password (for decryption):", bg=self.bg_color, fg=self.fg_color)
        self.master_password_label.pack(pady=10)

        self.master_password_entry = Entry(master, show='*', bg=self.entry_bg_color, fg=self.entry_fg_color, insertbackground=self.fg_color)
        self.master_password_entry.pack(pady=5)

        self.encrypt_button = Button(master, text="Encrypt", command=self.encrypt, bg=self.button_color, fg=self.fg_color)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = Button(master, text="Decrypt", command=self.decrypt, bg=self.button_color, fg=self.fg_color)
        self.decrypt_button.pack(pady=10)

    def browse(self):
        file_or_directory = filedialog.askopenfilename() or filedialog.askdirectory()
        self.path_entry.delete(0, 'end')
        self.path_entry.insert(0, file_or_directory)

    def encrypt(self):
        path = self.path_entry.get()
        password = self.password_entry.get()

        if not path or not password:
            messagebox.showerror("Error", "Please select a file/directory and enter a password.")
            return

        if os.path.isdir(path):
            encrypt_directory(path, password)
            messagebox.showinfo("Success", f"Directory {path} encrypted successfully.")
        elif os.path.isfile(path):
            encrypt_file(path, password)
            messagebox.showinfo("Success", f"File {path} encrypted successfully.")
        else:
            messagebox.showerror("Error", "Invalid path provided.")

    def decrypt(self):
        path = self.path_entry.get()
        password = self.password_entry.get()
        master_password = self.master_password_entry.get()

        if not path or not password or not master_password:
            messagebox.showerror("Error", "Please select a file/directory and enter both passwords.")
            return

        if os.path.isdir(path):
            decrypt_directory(path, password, master_password)
            messagebox.showinfo("Success", f"Directory {path} decrypted successfully.")
        elif os.path.isfile(path) and path.endswith('.enc'):
            decrypt_file(path, password, master_password)
            messagebox.showinfo("Success", f"File {path} decrypted successfully.")
        else:
            messagebox.showerror("Error", "Invalid path or file provided for decryption.")


if __name__ == "__main__":
    root = Tk()
    encryption_app = EncryptionApp(root)
    root.mainloop()

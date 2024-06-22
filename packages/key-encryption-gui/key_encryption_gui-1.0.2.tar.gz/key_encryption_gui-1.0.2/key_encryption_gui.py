import os
import base64
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

def create_unique_filename(base_directory, desired_name):
    if not os.path.isfile(os.path.join(base_directory, desired_name + ".key")):
        return desired_name + ".key"
    i = 1
    while os.path.isfile(os.path.join(base_directory, f"{desired_name}_{i}.key")):
        i += 1
    return f"{desired_name}_{i}.key"

def encrypt_key(key_to_encrypt, password_provided, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_provided.encode()))
    f = Fernet(key)
    encrypted_key = f.encrypt(key_to_encrypt.encode())
    return encrypted_key

def create_keys():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    try:
        number_of_keys = int(num_keys_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of keys.")
        return

    keys_directory = directory_entry.get()
    if not keys_directory:
        messagebox.showerror("Error", "Please select a directory.")
        return

    os.makedirs(keys_directory, exist_ok=True)
    messages = []

    for i in range(number_of_keys):
        salt = os.urandom(16)
        private_key = private_key_entries[i].get()
        if not private_key:
            messagebox.showerror("Error", f"Please enter private key #{i+1}.")
            return
        desired_name = key_name_entries[i].get()
        if not desired_name:
            messagebox.showerror("Error", f"Please enter a name for private key #{i+1}.")
            return

        file_name = create_unique_filename(keys_directory, desired_name)
        full_path = os.path.join(keys_directory, file_name)

        encrypted_key = encrypt_key(private_key, password, salt)

        with open(full_path, 'wb') as f:
            f.write(salt + encrypted_key)

        messages.append(f'Encrypted key #{i+1} saved to "{full_path}".')

    messagebox.showinfo("Success", "\n".join(messages))

    # Clear input fields after successful encryption
    password_entry.delete(0, tk.END)
    num_keys_entry.delete(0, tk.END)
    directory_entry.delete(0, tk.END)
    update_key_entries()

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

def update_key_entries():
    try:
        number_of_keys = int(num_keys_entry.get())
    except ValueError:
        return

    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    private_key_entries.clear()
    key_name_entries.clear()

    for i in range(number_of_keys):
        private_key_label = tk.Label(scrollable_frame, text=f"Private Key #{i+1}:", bg='black', fg='white')
        private_key_label.grid(row=i, column=0, padx=5, pady=5, sticky='e')
        private_key_entry = tk.Entry(scrollable_frame, show='*', width=50, bg='black', fg='white', insertbackground='white')
        private_key_entry.grid(row=i, column=1, padx=5, pady=5)
        private_key_entries.append(private_key_entry)

        key_name_label = tk.Label(scrollable_frame, text=f"Key Name #{i+1}:", bg='black', fg='white')
        key_name_label.grid(row=i, column=2, padx=5, pady=5, sticky='e')
        key_name_entry = tk.Entry(scrollable_frame, width=30, bg='black', fg='white', insertbackground='white')
        key_name_entry.grid(row=i, column=3, padx=5, pady=5)
        key_name_entries.append(key_name_entry)

def main_entry():
    global password_entry, num_keys_entry, directory_entry, private_key_entries, key_name_entries, scrollable_frame

    root = tk.Tk()
    root.title("Encrypt Private Keys")
    root.geometry("800x600")
    root.configure(bg='black')

    tk.Label(root, text="Password:", bg='black', fg='white').grid(row=0, column=0, padx=5, pady=5, sticky='e')
    password_entry = tk.Entry(root, show='*', width=50, bg='black', fg='white', insertbackground='white')
    password_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Number of Keys:", bg='black', fg='white').grid(row=1, column=0, padx=5, pady=5, sticky='e')
    num_keys_entry = tk.Entry(root, width=50, bg='black', fg='white', insertbackground='white')
    num_keys_entry.grid(row=1, column=1, padx=5, pady=5)
    num_keys_entry.bind("<KeyRelease>", lambda event: update_key_entries())

    tk.Label(root, text="Save Directory:", bg='black', fg='white').grid(row=2, column=0, padx=5, pady=5, sticky='e')
    directory_entry = tk.Entry(root, width=50, bg='black', fg='white', insertbackground='white')
    directory_entry.grid(row=2, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=select_directory, bg='black', fg='white').grid(row=2, column=2, padx=5, pady=5)

    frame = tk.Frame(root, bg='black')
    frame.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

    canvas = tk.Canvas(frame, bg='black', highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='black')

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    private_key_entries = []
    key_name_entries = []

    tk.Button(root, text="Create Keys", command=create_keys, bg='black', fg='white').grid(row=3, column=1, padx=5, pady=20)

    root.grid_rowconfigure(4, weight=1)
    root.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    canvas.pack_propagate(False)

    root.mainloop()

if __name__ == "__main__":
    main_entry()
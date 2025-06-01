import tkinter
import os
from cryptography.fernet import Fernet

from main2 import fernet

my_screen = tkinter.Tk()
my_screen.title("Secret Notes")
my_screen.minsize(width=400,height=730)


#functions

#save to file function
def save_file():
    title_to_save = note_title_entry.get()
    text_to_save = secret_text.get("1.0",tkinter.END)

    my_key = fernet.generate_key()
    my_fernet = Fernet(my_key)

    my_cipher_text = my_fernet.encrypt(text_to_save.encode())

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir,"my_secret.txt")

    if not title_to_save.strip() or not text_to_save.strip():
        result_label.config(text="Please fill both title and text.")
    else:
        try:
            with open(file_path,"a") as file:
                file.write(title_to_save.strip() + ":\n")
                file.write(str(my_cipher_text.strip()) + "\n")
                result_label.config(text="File saved successfully.")

            secret_text.delete("1.0",tkinter.END)
            secret_text.insert("1.0",my_cipher_text.decode())

        except Exception as e:
            result_label.config(text=f"Error: {e}\nFile could not be saved.")

#ui objects
try:
    icon = tkinter.PhotoImage(file="incognito.png",)
    smaller_icon = icon.subsample(4,"")
    icon_label = tkinter.Label(image=smaller_icon)
    icon_label.pack()
except:
    pass

note_title_label = tkinter.Label(text="Enter your title")
note_title_label.pack(padx=5,pady=5)

note_title_entry = tkinter.Entry()
note_title_entry.pack(padx=5,pady=5)

secret_label = tkinter.Label(text="Enter your secret")
secret_label.pack(padx=5,pady=5)

secret_text = tkinter.Text(width=50,height=20)
secret_text.pack(padx=5,pady=5,)

password_label = tkinter.Label(text="Enter your password")
password_label.pack(padx=5,pady=5)

password_entry = tkinter.Entry()
password_entry.pack(padx=5,pady=5)

encrypt_button = tkinter.Button(text="Save & Encrypt",command=save_file)
encrypt_button.pack(padx=10,pady=10)

decrypt_button = tkinter.Button(text="Decrypt")
decrypt_button.pack(padx=10,pady=10)

result_label = tkinter.Label(text="")
result_label.pack(padx=10,pady=10)

tkinter.mainloop()
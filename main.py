import tkinter

my_screen = tkinter.Tk()
my_screen.title("Secret Notes")
my_screen.minsize(width=400,height=500)


#ui objects

icon = tkinter.PhotoImage(file="incognito.png",)
smaller_icon = icon.subsample(4,"")

icon_label = tkinter.Label(image=smaller_icon)
icon_label.pack()

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

tkinter.mainloop()
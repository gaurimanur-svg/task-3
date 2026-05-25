import random 
import string 
import tkinter as tk

def generate():
    length=int(entry.get())
    chars=string.ascii_letters+string.digits+string.punctuation
    password="".join(random.choice(chars)for i in range(length))
    result.config(text=password)

root=tk.Tk()
root.title("Password Generator")
root.geometry("500x300")

tk.Label(root,text="Enter Length",font=("Arial",14)).pack(pady=10)

entry=tk.Entry(root,font=("Arial",14))
entry.pack(pady=10)

tk.Button(root, text="Generate", font=("Arial", 14), command=generate).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 16))
result.pack(pady=20)

root.mainloop()
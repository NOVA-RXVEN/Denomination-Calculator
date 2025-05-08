from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.title("Length Converter App")

def check_strength():
    password = entry.get()
    length = len(password)
    
    if length <= 5:
        strength = "Weak"
        color = "red"
        
    elif length <= 10:
        strength = "Medium"
        color = "cyan"
        
    elif length <= 15:
        strength = "Strong"
        color = "light green"
        
    else:
        strength = "Very Strong"
        color = "dark green"
    
    result_label.config(text=f"Password Strength: {strength}", fg=color)

label = Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=20)

entry = Entry(root, show='*', width=30)
entry.pack(pady=10)

check_button = Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
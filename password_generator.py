import random 
import tkinter as tk

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),'

# function to generate password 
def generate_password(length):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)

    # deletes any text that might be in textbox 
    textbox.delete("1.0", "end")  
    # inserts new password in textbox 
    textbox.insert(tk.END, passwords)

# create window 
window = tk.Tk()

window.geometry("500x250")
window.title("Password Generator App")

label = tk.Label(window, text="Generate a password", font=('Arial',18))
label.pack(padx=20, pady=5)

# textbox to hold generated password 
textbox = tk.Text(window, height=1, font=('Arial', 16))
textbox.pack(padx=10, pady=5)

label = tk.Label(window, text="Select password length", font=('Arial',14))
label.pack(padx=20)

# slider to determine password length 
slider = tk.Scale(from_=8, to=50, orient='horizontal')
password_length = slider.get()
slider.pack()

button = tk.Button(window, text="Generate", font=('Arial', 18), command=lambda: generate_password(slider.get()))
button.pack(padx=10, pady=20)

new_password = generate_password(password_length)
window.mainloop()

 
import tkinter as tk
from tkinter import messagebox

def register_user():
    """Handles registration logic."""
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    
    if username and password and email:
        # You can add code here to save the user details to a database or file
        messagebox.showinfo("Success", "Registration Successful!")
        # Clear the fields
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Create the main application window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x300")

# Labels and Entry Fields
label_title = tk.Label(root, text="Register Here", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

label_username = tk.Label(root, text="Username:")
label_username.pack(anchor="w", padx=20)
entry_username = tk.Entry(root, width=30)
entry_username.pack(padx=20, pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(anchor="w", padx=20)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(padx=20, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(anchor="w", padx=20)
entry_email = tk.Entry(root, width=30)
entry_email.pack(padx=20, pady=5)

# Submit Button
btn_register = tk.Button(root, text="Register", command=register_user, bg="blue", fg="white")
btn_register.pack(pady=20)

# Run the application
root.mainloop()

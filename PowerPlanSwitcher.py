import customtkinter as ctk
import subprocess

# Standard Windows Power Plan GUIDs
PLANS = {
    "Ultimate": "14588082-df42-404e-8beb-5965d942d01f",
    "Performance": "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c",
    "Balanced": "381b4222-f694-41f0-9685-ff5bb260df2e",
    "Power Saver": "a1841308-3541-4fab-bc81-f71556f20b4a"
}

def set_plan(plan_name):
    guid = PLANS[plan_name]
    # Execute only the setactive command
    result = subprocess.run(f"powercfg /setactive {guid}", capture_output=True, shell=True)
    
    if result.returncode == 0:
        status_label.configure(text=f"Active: {plan_name}", text_color="#57bb8a")
    else:
        status_label.configure(text="Plan not found or Access Denied", text_color="#ff5555")

# GUI Configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Power Switch")
app.geometry("300x420")

# Title
title_label = ctk.CTkLabel(app, text="Power Control", font=("Segoe UI", 24, "bold"))
title_label.pack(pady=(30, 10))

# Status indicator
status_label = ctk.CTkLabel(app, text="Select a mode", font=("Segoe UI", 14))
status_label.pack(pady=(0, 20))

# Button Generator
for name in PLANS.keys():
    button = ctk.CTkButton(
        app, 
        text=name, 
        command=lambda n=name: set_plan(n),
        corner_radius=20,
        height=45,
        font=("Segoe UI", 13, "bold")
    )
    button.pack(pady=10, padx=40, fill="x")

app.mainloop()

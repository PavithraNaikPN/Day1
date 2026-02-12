import customtkinter as ctk
import random
from tkinter import messagebox

# ---- App Theme ----
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def start_simulation():
    name = entry_name.get()
    distance = entry_distance.get()
    obstacle = obstacle_var.get()

    if not name or not distance:
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        distance = int(distance)
    except ValueError:
        messagebox.showerror("Error", "Distance must be a number")
        return

    # ---- Decision Logic ----
    if obstacle == "Yes":
        if distance > 50:
            speed = 2
            movement = "Slow movement (Obstacle detected)"
        else:
            speed = 1
            movement = "Crawling carefully"
    else:
        if distance > 100:
            speed = 5
            movement = "Fast movement"
        elif distance > 50:
            speed = 3
            movement = "Medium speed"
        else:
            speed = 2
            movement = "Approaching slowly"

    # ---- Simulation ----
    checkpoints = ["Start"]
    travelled = 0

    while travelled < distance:
        step = random.randint(5, 15)
        travelled += step
        direction = random.choice(["Left", "Right", "Straight"])
        checkpoints.append(f"{travelled}m → {direction}")

    # ---- Output ----
    output_box.delete("0.0", "end")
    output_box.insert("end", f"🚀 ROBOT TRIP SUMMARY\n\n")
    output_box.insert("end", f"🤖 Name      : {name}\n")
    output_box.insert("end", f"📏 Distance  : {distance} m\n")
    output_box.insert("end", f"🚧 Obstacle  : {obstacle}\n")
    output_box.insert("end", f"⚙️ Speed     : {speed}\n")
    output_box.insert("end", f"🧭 Movement  : {movement}\n\n")
    output_box.insert("end", "📍 Checkpoints:\n")

    for cp in checkpoints:
        output_box.insert("end", f" • {cp}\n")

# ---- Main Window ----
app = ctk.CTk()
app.title("Robot Controller 2.0")
app.geometry("600x550")

# ---- Title ----
title = ctk.CTkLabel(app, text="🤖 Robot Controller Dashboard",
                     font=ctk.CTkFont(size=22, weight="bold"))
title.pack(pady=15)

# ---- Input Frame ----
frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=20, fill="x")

entry_name = ctk.CTkEntry(frame, placeholder_text="Robot Name")
entry_name.pack(pady=8, padx=10, fill="x")

entry_distance = ctk.CTkEntry(frame, placeholder_text="Distance to Target (meters)")
entry_distance.pack(pady=8, padx=10, fill="x")

obstacle_var = ctk.StringVar(value="No")
obstacle_menu = ctk.CTkOptionMenu(frame, values=["Yes", "No"], variable=obstacle_var)
obstacle_menu.pack(pady=8)

start_btn = ctk.CTkButton(frame, text="▶ Start Simulation", command=start_simulation)
start_btn.pack(pady=12)

# ---- Output Box ----
output_box = ctk.CTkTextbox(app, height=220)
output_box.pack(padx=20, pady=10, fill="both")

app.mainloop()

import random
import tkinter as tk
from tkinter import ttk, messagebox
from enum import Enum
from dataclasses import dataclass
from typing import Tuple

# -------------------- Core Logic --------------------

class ObstacleType(Enum):
    NONE = "No obstacle"
    HUMAN = "Human"
    WALL = "Wall"
    VEHICLE = "Vehicle"

class Direction(Enum):
    LEFT = "Left"
    RIGHT = "Right"
    STRAIGHT = "Straight"
    U_TURN = "U-Turn"
    PAUSE = "Pause"

@dataclass
class Bot:
    name: str
    total_distance: float = 0.0
    target_distance: float = 0.0
    current_direction: Direction = Direction.STRAIGHT
    position: Tuple[float, float] = (0, 0)

class NavigationSystem:
    def _init_(self):
        self.detection_range = 50
        self.speed = 2.0

    def check_obstacle_within_range(self, obstacle_distance):
        return 0 <= obstacle_distance <= self.detection_range

    def calculate_travel_time(self, distance):
        if self.speed <= 0:
            return 0
        return distance / self.speed

    def handle_obstacle(self, bot, obstacle_type, obstacle_distance, log):
        log("=" * 50)

        if obstacle_type == ObstacleType.HUMAN:
            log(f"🚨 Human detected at {obstacle_distance:.1f}m")
            log("⏸️ Action: STOP + ALERT")
            return Direction.PAUSE

        elif obstacle_type == ObstacleType.WALL:
            log(f"🚧 Wall detected at {obstacle_distance:.1f}m")
            if obstacle_distance < 10:
                log("↪️ Action: U-Turn")
                return Direction.U_TURN
            elif obstacle_distance < 25:
                log("↩️ Action: Turn Left")
                return Direction.LEFT
            else:
                log("↪️ Action: Turn Right")
                return Direction.RIGHT

        elif obstacle_type == ObstacleType.VEHICLE:
            log(f"🚗 Vehicle detected at {obstacle_distance:.1f}m")
            log("🐢 Action: Slow Down")
            self.speed = max(1, self.speed - 1)
            return bot.current_direction

        else:
            log("✅ No obstacle: Continue straight")
            return Direction.STRAIGHT

    def update_bot_position(self, bot, distance):
        bot.total_distance += distance
        x, y = bot.position

        if bot.current_direction == Direction.STRAIGHT:
            bot.position = (x + distance, y)
        elif bot.current_direction == Direction.LEFT:
            bot.position = (x, y + distance)
        elif bot.current_direction == Direction.RIGHT:
            bot.position = (x, y - distance)
        elif bot.current_direction == Direction.U_TURN:
            bot.position = (x - distance, y)

# -------------------- Tkinter GUI --------------------

class BotApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Bot Navigation System")
        self.root.geometry("800x600")

        self.nav = NavigationSystem()
        self.obstacles = []

        # ---- Input Frame ----
        input_frame = tk.Frame(root, padx=10, pady=10)
        input_frame.pack(fill="x")

        tk.Label(input_frame, text="Bot Name:").grid(row=0, column=0)
        self.bot_name_entry = tk.Entry(input_frame)
        self.bot_name_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Target Distance:").grid(row=0, column=2)
        self.target_entry = tk.Entry(input_frame)
        self.target_entry.grid(row=0, column=3)

        tk.Label(input_frame, text="Speed:").grid(row=1, column=0)
        self.speed_var = tk.IntVar(value=2)
        self.speed_slider = tk.Scale(input_frame, from_=1, to=5, orient="horizontal", variable=self.speed_var)
        self.speed_slider.grid(row=1, column=1, columnspan=2)

        # ---- Obstacle Input ----
        tk.Label(input_frame, text="Obstacle Type:").grid(row=2, column=0)
        self.obstacle_type_combo = ttk.Combobox(input_frame, values=["Human", "Wall", "Vehicle", "No obstacle"], state="readonly")
        self.obstacle_type_combo.current(0)
        self.obstacle_type_combo.grid(row=2, column=1)

        tk.Label(input_frame, text="Distance:").grid(row=2, column=2)
        self.obstacle_dist_entry = tk.Entry(input_frame)
        self.obstacle_dist_entry.grid(row=2, column=3)

        tk.Button(input_frame, text="Add Obstacle", command=self.add_obstacle).grid(row=2, column=4)

        # ---- Buttons ----
        btn_frame = tk.Frame(root, pady=10)
        btn_frame.pack(fill="x")

        self.step_mode = tk.BooleanVar()
        tk.Checkbutton(btn_frame, text="Step-by-Step Mode", variable=self.step_mode).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Start Simulation", command=self.start_simulation).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Generate Random Obstacles", command=self.generate_random).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear_all).pack(side="left", padx=5)

        # ---- Listbox ----
        self.listbox = tk.Listbox(root, height=6)
        self.listbox.pack(fill="x", padx=10)

        # ---- Output ----
        self.output_text = tk.Text(root)
        self.output_text.pack(fill="both", expand=True, padx=10, pady=10)

    def log(self, text):
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END)

    def add_obstacle(self):
        try:
            dist = float(self.obstacle_dist_entry.get())
        except:
            messagebox.showerror("Error", "Invalid distance")
            return

        t = self.obstacle_type_combo.get()
        if t == "Human":
            otype = ObstacleType.HUMAN
        elif t == "Wall":
            otype = ObstacleType.WALL
        elif t == "Vehicle":
            otype = ObstacleType.VEHICLE
        else:
            otype = ObstacleType.NONE

        self.obstacles.append((otype, dist))
        self.listbox.insert(tk.END, f"{otype.value} at {dist} m")

    def generate_random(self):
        self.clear_all()
        for _ in range(random.randint(3, 7)):
            otype = random.choice(list(ObstacleType))
            dist = random.randint(5, 100)
            self.obstacles.append((otype, dist))
            self.listbox.insert(tk.END, f"{otype.value} at {dist} m")
        self.log("🎲 Random obstacles generated!")

    def clear_all(self):
        self.obstacles.clear()
        self.listbox.delete(0, tk.END)
        self.output_text.delete("1.0", tk.END)

    def start_simulation(self):
        self.output_text.delete("1.0", tk.END)

        name = self.bot_name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Enter bot name")
            return

        try:
            target = float(self.target_entry.get())
        except:
            messagebox.showerror("Error", "Invalid target distance")
            return

        self.nav.speed = self.speed_var.get()
        bot = Bot(name=name, target_distance=target)

        self.log("🚀 Starting simulation...")
        self.log(f"🤖 Bot: {bot.name}")
        self.log(f"⚡ Speed: {self.nav.speed} m/s")

        obstacles = sorted(self.obstacles, key=lambda x: x[1])
        current = 0.0

        for otype, odist in obstacles:
            travel = odist - current
            if travel > 0:
                self.nav.update_bot_position(bot, travel)
                current = odist

            self.log(f"🔍 Obstacle at {odist} m → {otype.value}")
            new_dir = self.nav.handle_obstacle(bot, otype, odist, self.log)
            bot.current_direction = new_dir

        remaining = target - current
        if remaining > 0:
            self.nav.update_bot_position(bot, remaining)

        self.log("📊 Journey Complete!")
        self.log(f"📏 Distance: {bot.total_distance:.1f} m")
        self.log(f"📍 Final Position: {bot.position}")
        self.log(f"⏱️ Time: {self.nav.calculate_travel_time(bot.total_distance):.1f} s")

# -------------------- Run --------------------

if _name_ == "_main_":
    root = tk.Tk()
    app = BotApp(root)
    root.mainloop()
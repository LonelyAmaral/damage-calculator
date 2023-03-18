import tkinter as tk

root = tk.Tk()

attacker_status = {
    "enraged": tk.BooleanVar(),
    "bleeding": tk.BooleanVar(),
    "poisoned": tk.BooleanVar(),
    "burned": tk.BooleanVar(),
    "stunned": tk.BooleanVar(),
    "confused": tk.BooleanVar(),
    "disarmed": tk.BooleanVar()
}

defender_status = {
    "shielded": tk.BooleanVar(),
    "armored": tk.BooleanVar(),
    "regenerating": tk.BooleanVar(),
    "slowed": tk.BooleanVar(),
    "confused": tk.BooleanVar(),
    "disarmed": tk.BooleanVar()
}


def calculate_bonus():
    status_effect_damage_bonus = 0
    if attacker_status["enraged"].get():
        status_effect_damage_bonus += 0.2
    if attacker_status["bleeding"].get():
        status_effect_damage_bonus += 0.1
    if attacker_status["poisoned"].get():
        status_effect_damage_bonus += 0.1
    if attacker_status["burned"].get():
        status_effect_damage_bonus += 0.1
    if attacker_status["stunned"].get():
        status_effect_damage_bonus += 0.05
    if attacker_status["confused"].get():
        status_effect_damage_bonus += 0.05
    if attacker_status["disarmed"].get():
        status_effect_damage_bonus -= 0.2

    status_effect_defense_penalty = 0
    if defender_status["shielded"].get():
        status_effect_defense_penalty += 0.2
    if defender_status["armored"].get():
        status_effect_defense_penalty += 0.1
    if defender_status["regenerating"].get():
        status_effect_defense_penalty -= 0.1
    if defender_status["slowed"].get():
        status_effect_defense_penalty -= 0.05
    if defender_status["confused"].get():
        status_effect_defense_penalty -= 0.05
    if defender_status["disarmed"].get():
        status_effect_defense_penalty += 0.2
    var_1.set(f"Damage Bonus: {status_effect_damage_bonus:.2f}")
    var_2.set(f"Defense Penalty: {status_effect_defense_penalty:.2f}")
    lbl_1.configure(text=var_1.get())
    lbl_2.configure(text=var_2.get())


attacker_frame = tk.LabelFrame(root, text="Attacker Status")
defender_frame = tk.LabelFrame(root, text="Defender Status")
calculations = tk.LabelFrame(root, text="Calculations")

for i, status in enumerate(attacker_status.keys()):
    cb = tk.Checkbutton(attacker_frame, text=status, variable=attacker_status[status])
    cb.grid(row=i, column=0, sticky="w")

for i, status in enumerate(defender_status.keys()):
    cb = tk.Checkbutton(defender_frame, text=status, variable=defender_status[status])
    cb.grid(row=i, column=1, sticky="w")

var_1 = tk.StringVar()
var_2 = tk.StringVar()
var_1.set("Damage Bonus: 0.00")
var_2.set("Defense Penalty: 0.00")
calculate_button = tk.Button(calculations, text="Calculate", command=calculate_bonus)
calculate_button.grid(row=1, column=2, sticky="w")
lbl_1 = tk.Label(calculations, text=var_1.get())
lbl_1.grid(row=2, column=2, sticky="w")
lbl_2 = tk.Label(calculations, text=var_2.get())
lbl_2.grid(row=3, column=2, sticky="w")

attacker_frame.pack(side="left", padx=10, pady=10)
defender_frame.pack(side="left", padx=10, pady=10)
calculations.pack(side="left", padx=10, pady=10)

root.mainloop()

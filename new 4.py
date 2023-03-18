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

defender_status = dict ( shielded=tk.BooleanVar () , armored=tk.BooleanVar () , regenerating=tk.BooleanVar () ,
                         slowed=tk.BooleanVar () , confused=tk.BooleanVar () , disarmed=tk.BooleanVar () )


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

    print("Status Effect Damage Bonus:", status_effect_damage_bonus)
    print("Status Effect Defense Penalty:", status_effect_defense_penalty)


attacker_frame = tk.LabelFrame(root, text="Attacker Status")
defender_frame = tk.LabelFrame(root, text="Defender Status")

for i, status in enumerate(attacker_status.keys()):
    cb = tk.Checkbutton(attacker_frame, text=status, variable=attacker_status[status])
    cb.grid(row=i, column=0, sticky="w")

for i, status in enumerate(defender_status.keys()):
    cb = tk.Checkbutton(defender_frame, text=status, variable=defender_status[status])
    cb.grid(row=i, column=0, sticky="w")

attacker_frame.pack(side="left", padx=10, pady=10)
defender_frame.pack(side="left", padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Bonus", command=calculate_bonus)
calculate_button.pack(pady=10)

root.mainloop()
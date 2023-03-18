import math
import random


class Attacker:
    def __init__(attacker):
        print("Enter Attacker Attributes:")
        attacker.level = input("level: ")
        attacker.strength = input("strength: ")
        attacker.intelligence = input("intelligence: ")
        attacker.dexterity = input("dexterity: ")
        attacker.agility = input("agility: ")
        attacker.stamina = input("stamina: ")
        attacker.willpower = input("willpower: ")
        attacker.perception = input("perception: ")
        attacker.focus = input("focus: ")
        attacker.luck = input("luck: ")
        attacker.charisma = input("charisma: ")
        attacker.wisdom = input("wisdom: ")


class Defender:
    def __init__(defender, level, defense, resistance, agility):
        defender.level = input("defender.level")
        defender.defense = input("defender.defense")
        defender.resistance = input("defender.resistance")
        defender.agility = input("defender.agility")


class Weapon:
    def __init__(weapon, damage, critical_chance, critical_damage, max_range):
        weapon.damage = input("weapon.damage")
        weapon.critical_chance = input("weapon.critical_chance")
        weapon.critical_damage = input("weapon.critical_damage")
        weapon.max_range = input("max_range")


class Spell:
    def __init__(spell, damage, critical_chance, critical_damage):
        spell.damage = input("spell.damage")
        spell.critical_chance = input("spell.critical_chance")
        spell.critical_damage = input("spell.critical_damage")


class Environment:
    def __init__(environment, weather, terrain, obstacle):
        environment.weather = input("weather.condition_bonus")
        environment.terrain = input("terrain_bonus")
        environment.obstacle = input("obstacle_penalty")


def calculate_base_damage(attacker, defender, weapon, spell, environment, distance, attacker_status, defender_status,
                          attacker_weakness_chance, defender_weakness_resistance,
                          randomize=random.uniform(0, 0.1)) -> object:
    attacker_level = int(attacker.level)
    attacker_strength: int = int(attacker.strength)
    attacker_intelligence = int(attacker.intelligence)
    attacker_dexterity = int(attacker.dexterity)
    attacker_agility = int(attacker.agility)
    attacker_stamina = int(attacker.stamina)
    attacker_willpower = int(attacker.willpower)
    attacker_perception = int(attacker.perception)
    attacker_focus = int(attacker.focus)
    attacker_luck = int(attacker.luck)
    attacker_charisma = int(attacker.charisma)
    attacker_wisdom = int(attacker.wisdom)

    defender_level = int(defender.level)
    defender_defense = int(defender.defense)
    defender_resistance = int(defender.resistance)
    defender_agility = int(defender.agility)

    # Weapon and spell stats
    weapon_damage: int = int(weapon.damage)
    weapon_critical_chance = int(weapon.critical_chance)
    weapon_critical_damage = int(weapon.critical_damage)
    spell_damage = int(spell.damage)
    spell_critical_chance = int(spell.critical_chance)
    spell_critical_damage = int(spell.critical_damage)

    # Environmental factors
    weather_condition_bonus = int(environment.weather)
    terrain_bonus = int(environment.terrain)
    obstacle_penalty = int(environment.obstacle)

    # Range and distance
    distance_penalty = -0.5 * math.pow((distance - weapon.max_range), 2) * (1 + randomize)

    # Movement
    agility_bonus = attacker_agility - defender_agility
    agility_multiplier = 1 + (0.05 * agility_bonus)

    # Attacker status effects
    status_effect_damage_bonus = 0
    if "enraged" in attacker_status:
        status_effect_damage_bonus += 0.2
    if "bleeding" in attacker_status:
        status_effect_damage_bonus += 0.1
    if "poisoned" in attacker_status:
        status_effect_damage_bonus += 0.1
    if "burned" in attacker_status:
        status_effect_damage_bonus += 0.1
    if "stunned" in attacker_status:
        status_effect_damage_bonus += 0.05
    if "confused" in attacker_status:
        status_effect_damage_bonus += 0.05
    if "disarmed" in attacker_status:
        status_effect_damage_bonus -= 0.2

    # Defender status effects
    status_effect_defense_penalty = 0
    if "shielded" in defender_status:
        status_effect_defense_penalty += 0.2
    if "armored" in defender_status:
        status_effect_defense_penalty += 0.1
    if "regenerating" in defender_status:
        status_effect_defense_penalty -= 0.1
    if "slowed" in defender_status:
        status_effect_defense_penalty -= 0.05
    if "confused" in defender_status:
        status_effect_defense_penalty -= 0.05
    if "disarmed" in defender_status:
        status_effect_defense_penalty += 0.2

    # Weakness chance and resistance
    attacker_weakness_chance /= 100
    defender_weakness_resistance /= 100

    # Calculate base damage
    physical_base_damage = ((attacker_strength * weapon_damage) / (defender_defense + 100))
    magical_base_damage = ((attacker_intelligence * spell_damage) / (defender_resistance + 100))

    # Apply critical hit
    physical_critical_hit = False
    magical_critical_hit = False
    if weapon_critical_chance > randomize.random():
        physical_base_damage *= weapon_critical_damage
        physical_critical_hit = True
    if randomize.random() < spell_critical_chance:
        magical_base_damage *= spell_critical_damage
        magical_critical_hit = True

    # Apply environmental bonuses and penalties
    physical_base_damage *= (1 + weather_condition_bonus + terrain_bonus)
    magical_base_damage *= (1 + weather_condition_bonus + terrain_bonus)

    # Apply distance penalty
    physical_base_damage *= (1 + distance_penalty)
    magical_base_damage *= (1 + distance_penalty)

    # Apply movement agility bonus
    physical_base_damage *= agility_multiplier
    magical_base_damage *= agility_multiplier

    # Apply status effects bonuses and penalties
    physical_base_damage *= (1 + status_effect_damage_bonus)
    magical_base_damage *= (1 + status_effect_damage_bonus)
    defender_defense *= (1 - status_effect_defense_penalty)
    defender_resistance *= (1 - status_effect_defense_penalty)

    # Apply weakness and resistance effects
    if randomize.random() < attacker_weakness_chance:
        physical_base_damage *= 1.5
        magical_base_damage *= 1.5
    if randomize.random() < defender_weakness_resistance:
        physical_base_damage *= 0.5
        magical_base_damage *= 0.5

    # Return total damage
    total_damage = round(physical_base_damage + magical_base_damage)

    print(total_damage)

    # Return information about the attack
    return {
        "total_damage": total_damage,
        "physical_base_damage": round(physical_base_damage),
        "magical_base_damage": round(magical_base_damage),
        "physical_critical_hit": physical_critical_hit,
        "magical_critical_hit": magical_critical_hit,
    }


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
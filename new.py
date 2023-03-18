import random

# range and distance
from builtins import object

import distance as distance

Distance2 = random.uniform ( 1 , 10 )
weapon_min_range = random.uniform ( 1 , 5 )
weapon_max_range = random.uniform ( 6 , 10 )

# attacker and defender status effects
attacker_status = [ "enraged" , "bleeding" , "poisoned" , "burned" ]
defender_status = [ "shielded" , "armored" , "regenerating" , "slowed" ]
attacker_weakness_chance = random.uniform ( 0 , 10 )
defender_weakness_resistance = random.uniform ( 0 , 10 )


# call the function with the random variables
class Attacker:
    attacker_level = random.randint(1, 10)
    attacker_strength = random.randint(1, 10)
    attacker_intelligence = random.randint(1, 10)
    attacker_dexterity = random.randint(1, 10)
    attacker_agility = random.randint(1, 10)
    attacker_stamina = random.randint(1, 10)
    attacker_willpower = random.randint(1, 10)
    attacker_perception = random.randint(1, 10)
    attacker_focus = random.randint(1, 10)
    attacker_luck = random.randint(1, 10)
    attacker_charisma = random.randint(1, 10)
    attacker_wisdom = random.randint(1, 10)

    def __init__(self, level, strength, intelligence, dexterity, agility, stamina, willpower, perception, focus, luck, charisma, wisdom):
        self.level = level
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.agility = agility
        self.stamina = stamina
        self.willpower = willpower
        self.perception = perception
        self.focus = focus
        self.luck = luck
        self.charisma = charisma
        self.wisdom = wisdom


class Defender:
    defender_level = random.randint(1, 10)
    defender_defense = random.randint(1, 10)
    defender_resistance = random.randint(1, 10)
    defender_agility = random.randint(1, 10)

    def __init__(self, level, defense, resistance, agility):
        self.level = level
        self.defense = defense
        self.resistance = resistance
        self.agility = agility


class Weapon:
    weapon_damage: int = random.randint ( 1 , 10 )
    weapon_critical_chance = random.uniform ( 0 , 0.1 )
    weapon_critical_damage = random.uniform ( 1 , 2 )
    def __init__(self, damage, critical_chance, critical_damage):
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage

class Spell:
    spell_damage = random.randint ( 1 , 10 )
    spell_critical_chance = random.uniform ( 0 , 0.1 )
    spell_critical_damage = random.uniform ( 1 , 2 )
    def __init__(self, damage, critical_chance, critical_damage):
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage

class Environment:
    weather_condition_bonus = random.uniform ( 0 , 0.1 )
    terrain_bonus = random.uniform ( 0 , 0.1 )
    obstacle_penalty = random.uniform ( 0 , 0.1 )
    def __init__(self, weather_condition_bonus, terrain_bonus, obstacle_penalty):
        self.weather_condition_bonus = weather_condition_bonus
        self.terrain_bonus = terrain_bonus
        self.obstacle_penalty = obstacle_penalty


def calculate_base_damage ( attacker_strength, Weapon: object , attacker_status: object , defender_status: object , attacker_weakness_chance: object ,
                          defender_weakness_resistance: object , defender_agility: object = 0 ,
                        Defender.defender_defense: object = None) -> object:
    """

    :rtype: object
    """
    # Movement
    agility_bonus = Attacker - defender_agility
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
    physical_base_damage = ((Attacker.attacker_strength * Weapon.weapon_damage) / (Defender.defender_defense + 100))
    magical_base_damage = ((Attacker.attacker_intelligence * Spell.spell_damage) / (Defender.defender_resistance + 100))

    # Apply critical hit
    physical_critical_hit = False
    magical_critical_hit = False
    if Weapon.weapon_critical_chance > random.random ():
        physical_base_damage *= Weapon.weapon_critical_damage
        physical_critical_hit = True
    if random.random () < Spell.spell_critical_chance:
        magical_base_damage *= Spell.spell_critical_damage
        magical_critical_hit = True

    # Apply environmental bonuses and penalties
    physical_base_damage *= (1 + Environment.weather_condition_bonus + Environment.terrain_bonus)
    magical_base_damage *= (1 + Environment.weather_condition_bonus + Environment.terrain_bonus)

    # Apply distance penalty
    physical_base_damage *= (1 + distance)
    magical_base_damage *= (1 + distance)

    # Apply movement agility bonus
    physical_base_damage *= agility_multiplier
    magical_base_damage *= agility_multiplier

    # Apply status effects bonuses and penalties
    physical_base_damage *= (1 + status_effect_damage_bonus)
    magical_base_damage *= (1 + status_effect_damage_bonus)
    defender_defense *= (1 - status_effect_defense_penalty)
    Defender.defender_resistance *= (1 - status_effect_defense_penalty)

    # Apply weakness and resistance effects
    if random.random () < attacker_weakness_chance:
        physical_base_damage *= 1.5
        magical_base_damage *= 1.5
    if random.random () < defender_weakness_resistance:
        physical_base_damage *= 0.5
        magical_base_damage *= 0.5

    # Return total damage
    total_damage = round ( physical_base_damage + magical_base_damage )

    # Return information about the attack
    return {
        "total_damage": total_damage ,
        "physical_base_damage": round ( physical_base_damage ) ,
        "magical_base_damage": round ( magical_base_damage ) ,
        "physical_critical_hit": physical_critical_hit ,
        "magical_critical_hit": magical_critical_hit ,
    }
    pass


damage = calculate_base_damage ( Attacker , Weapon , attacker_status ,
                                 defender_status , attacker_weakness_chance , defender_weakness_resistance ,
                                 Defender.defender_agility,
                                 distance_penalty=None )
print ( damage )

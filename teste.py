import math
import random

class Attacker:
    def __init__(attacker):
        print ( "Enter Attacker Attributes:" )
        attacker.level = input ( "level: " )
        attacker.strength = input ( "strength: " )
        attacker.intelligence = input ( "intelligence: " )
        attacker.dexterity = input ( "dexterity: " )
        attacker.agility = input ( "agility: " )
        attacker.stamina = input ( "stamina: " )
        attacker.willpower = input ( "willpower: " )
        attacker.perception = input ( "perception: " )
        attacker.focus = input ( "focus: " )
        attacker.luck = input ( "luck: " )
        attacker.charisma = input ( "charisma: " )
        attacker.wisdom = input ( "wisdom: " )

class Defender:
    def __init__(defender, level, defense, resistance, agility):
        defender.level = input ( "defender.level" )
        defender.defense = input ( "defender.defense" )
        defender.resistance = input ( "defender.resistance" )
        defender.agility = input ( "defender.agility" )

class Weapon:
    def __init__(weapon, damage, critical_chance, critical_damage, max_range):
        weapon.damage = input ( "weapon.damage" )
        weapon.critical_chance = input ( "weapon.critical_chance" )
        weapon.critical_damage = input ( "weapon.critical_damage" )
        weapon.max_range = input("max_range")

class Spell:
    def __init__(spell, damage, critical_chance, critical_damage):
        spell.damage = input ( "spell.damage" )
        spell.critical_chance = input ( "spell.critical_chance" )
        spell.critical_damage = input ( "spell.critical_damage" )

class Environment:
    def __init__(environment, weather, terrain, obstacle):
        environment.weather = input ( "weather.condition_bonus" )
        environment.terrain = input ( "terrain_bonus" )
        environment.obstacle = input ( "obstacle_penalty" )

def calculate_base_damage(attacker , defender , weapon , spell , environment , distance , attacker_status , defender_status ,
                          attacker_weakness_chance , defender_weakness_resistance , randomize=random.uniform( 0, 0.1 )) -> object:

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



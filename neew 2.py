import random

# import distance


distance = input("distance between them")
weapon_min_range = input("weapon mix range")
weapon_max_range = input("weapon max range")

# attacker and defender status effects
attacker_status = [ "enraged" , "bleeding" , "poisoned" , "burned" ]
defender_status = [ "shielded" , "armored" , "regenerating" , "slowed" ]
attacker_weakness_chance = random.uniform ( 0 , 10 )
defender_weakness_resistance = random.uniform ( 0 , 10 )


# call the function with the random variables
class Attacker:
    def __init__(self , level , strength , intelligence , dexterity , agility , stamina , willpower , perception ,
                 focus , luck , charisma , wisdom):
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

    attacker_level = random.randint ( 1 , 10 )
    attacker_strength = random.randint ( 1 , 10 )
    attacker_intelligence = random.randint ( 1 , 10 )
    attacker_dexterity = random.randint ( 1 , 10 )
    attacker_agility = random.randint ( 1 , 10 )
    attacker_stamina = random.randint ( 1 , 10 )
    attacker_willpower = random.randint ( 1 , 10 )
    attacker_perception = random.randint ( 1 , 10 )
    attacker_focus = random.randint ( 1 , 10 )
    attacker_luck = random.randint ( 1 , 10 )
    attacker_charisma = random.randint ( 1 , 10 )
    attacker_wisdom = random.randint ( 1 , 10 )


class Defender:
    def __init__(self , level , defense , resistance , agility):
        self.level = level
        self.defense = defense
        self.resistance = resistance
        self.agility = agility

    defender_level = random.randint ( 1 , 10 )
    defender_defense = random.randint ( 1 , 10 )
    defender_resistance = random.randint ( 1 , 10 )
    defender_agility = random.randint ( 1 , 10 )


class Weapon:
    def __init__(self , damage , critical_chance , critical_damage):
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage

    weapon_damage = random.randint ( 1 , 10 )
    weapon_critical_chance = random.uniform ( 0 , 0.1 )
    weapon_critical_damage = random.uniform ( 1 , 2 )


class Spell:
    def __init__(self , damage , critical_chance , critical_damage):
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage

    spell_damage = random.randint ( 1 , 10 )
    spell_critical_chance = random.uniform ( 0 , 0.1 )
    spell_critical_damage = random.uniform ( 1 , 2 )


class Environment:
    def __init__(self , weather_condition_bonus , terrain_bonus , obstacle_penalty):
        self.weather_condition_bonus = weather_condition_bonus
        self.terrain_bonus = terrain_bonus
        self.obstacle_penalty = obstacle_penalty

    weather_condition_bonus = random.uniform ( 0 , 0.1 )
    terrain_bonus = random.uniform ( 0 , 0.1 )
    obstacle_penalty = random.uniform ( 0 , 0.1)

#define the function to calculate the damage
def calculate_damage(attacker, defender, weapon, spell, environment):
    # calculate attacker damage
    attacker_damage = attacker.strength * weapon.damage * (1 + (attacker.willpower / 100))
    attacker_crit_chance = weapon.critical_chance * (1 + (attacker.luck / 100))
    attacker_crit_damage = attacker_damage * weapon.critical_damage

    # calculate spell damage
    spell_damage = spell.damage * (1 + (attacker.intelligence / 100))
    spell_crit_chance = spell.critical_chance * (1 + (attacker.focus / 100))
    spell_crit_damage = spell_damage * spell.critical_damage

    # calculate defender damage resistance
    defender_resistance_factor = defender.resistance / 100

    # calculate environment bonuses/penalties
    weather_bonus = attacker.agility * environment.weather_condition_bonus
    terrain_bonus = attacker.agility * environment.terrain_bonus
    obstacle_penalty = attacker.agility * environment.obstacle_penalty

    # calculate distance factor
    distance_factor = 1
    if distance < weapon_min_range:
        distance_factor = 0
    elif distance > weapon_max_range:
        distance_factor = weapon_max_range / distance

    # calculate attacker and defender status effects
    attacker_status_effect = 0
    if attacker_status:
        attacker_status_effect = attacker_weakness_chance * sum([random.uniform(0, 1) for _ in range(len(attacker_status))])
    defender_status_effect = 0
    if defender_status:
        defender_status_effect = defender_weakness_resistance * sum([random.uniform(0, 1) for _ in range(len(defender_status))])

    # calculate final damage
    final_damage = (attacker_damage * distance_factor + spell_damage) * (1 - defender_resistance_factor) + weather_bonus + terrain_bonus - obstacle_penalty
    if random.uniform(0, 1) < attacker_crit_chance:
        final_damage += attacker_crit_damage
    if random.uniform(0, 1) < spell_crit_chance:
        final_damage += spell_crit_damage
    final_damage *= (1 - attacker_status_effect) * (1 + defender_status_effect)

    return final_damage

#create objects for testing



damage = calculate_damage(Attacker, Defender, Weapon, Spell, Environment)
print("Final Damage:", damage)
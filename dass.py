import random

# attacker stats

attacker_level = random.randint (1, 10)
attacker_strength: object = random.randint ( 1 , 10 )
attacker_intelligence = random.randint ( 1 , 10 )
attacker_dexterity = random.randint ( 1 , 10 )
attacker_agility = random.randint ( 1 , 10 )
attacker_stamina = random.randint ( 1 , 10 )
attacker_willpower = random.randint ( 1 , 10 )
attacker_perception = random.randint ( 1 , 10 )
attacker_focus = random.randint ( 1 , 10 )
attacker_luck: int = random.randint ( 1 , 10 )
attacker_charisma = random.randint ( 1 , 10 )
attacker_wisdom = random.randint ( 1 , 10 )

# defender stats
defender_level = random.randint ( 1 , 10 )
defender_defense = random.randint ( 1 , 10 )
defender_resistance = random.randint ( 1 , 10 )

# weapon and spell stats
weapon_damage = random.randint ( 1 , 10 )
weapon_critical_chance = random.uniform ( 0 , 0.1 )
weapon_critical_damage = random.uniform ( 1 , 2 )
spell_damage = random.randint ( 1 , 10 )
spell_critical_chance = random.uniform ( 0 , 0.1 )
spell_critical_damage = random.uniform ( 1 , 2 )

# environmental factors
weather_condition_bonus = random.uniform ( 0, 0.1)
terrain_bonus = random.uniform (0, 0.1)
obstacle_penalty = random.uniform ( 0 , 0.1 )

# range and distance
distance = random.uniform ( 1 , 10 )
weapon_min_range = random.uniform ( 1 , 5 )
weapon_max_range = random.uniform ( 6 , 10 )

# attacker and defender status effects
attacker_status = [ "enraged" , "bleeding" , "poisoned" , "burned" ]
defender_status = [ "shielded" , "armored" , "regenerating" , "slowed" ]
attacker_weakness_chance = random.uniform ( 0 , 10 )
defender_weakness_resistance: float = random.uniform ( 0 , 10 )


# call the function with the random variables


def calculate_base_damage(attacker , defender , weapon , spell , environment , distance , attacker_status ,
                          defender_status ,
                          attacker_weakness_chance , defender_weakness_resistance , defender_agility=0 ,
                          random=random.uniform ( 0 , 0.1 ) ,
                          distance_penalty=None) -> object:
    # Attacker and defender stats
    attacker_level = attacker.level
    attacker_strength = attacker.strength
    attacker_intelligence = attacker.intelligence
    attacker_dexterity = attacker.dexterity
    attacker_agility = attacker.agility
    attacker_stamina = attacker.stamina
    attacker_willpower = attacker.willpower
    attacker_perception = attacker.perception
    attacker_focus = attacker.focus
    attacker_luck = attacker.luck
    attacker_charisma = attacker.charisma
    attacker_wisdom = attacker.wisdom

    defender_level = defender.level
    defender_defense = defender.defense
    defender_resistance = defender.resistance

    # Weapon and spell stats
    weapon_damage = weapon.damage
    weapon_critical_chance = weapon.critical_chance
    weapon_critical_damage = weapon.critical_damage
    spell_damage = spell.damage
    spell_critical_chance = spell.critical_chance
    spell_critical_damage = spell.critical_damage

    # Environmental factors
    weather_condition_bonus = environment.weather_condition_bonus
    terrain_bonus = environment.terrain_bonus
    obstacle_penalty = environment.obstacle_penalty

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
    if weapon_critical_chance > random.random ():
        physical_base_damage *= weapon_critical_damage
        physical_critical_hit = True
    if random.random () < spell_critical_chance:
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


result = calculate_base_damage ( attacker_level , attacker_strength , attacker_intelligence , attacker_dexterity ,
                                 attacker_agility , attacker_stamina , attacker_willpower , attacker_perception ,
                                 attacker_focus , attacker_luck , attacker_charisma , attacker_wisdom ,
                                 defender_level )
print ( result )

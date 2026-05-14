# Portfolio 2: Conditional Execution
# Course: BES10a
# Student: Ethan Seth S. Gratuito

print("--- Rotom Dex: Battle Calculator ---")
move_type = input("Enter your move's type (Water/Fire/Grass): ")
defender_type = input("Enter the defender's type (Water/Fire/Grass): ")

raw_power = input("Enter the move's base power (e.g., 40, 90): ")
raw_hp = input("Enter the defender's estimated HP: ")

try:
    # Attempt to convert inputs to integers
    power = int(raw_power)
    target_hp = int(raw_hp)

    # Multi-way and nested decisions for type effectiveness
    multiplier = 1.0
    
    if move_type == "Water":
        if defender_type == "Fire":
            multiplier = 2.0
        elif defender_type == "Grass":
            multiplier = 0.5
            
    elif move_type == "Fire":
        if defender_type == "Grass":
            multiplier = 2.0
        elif defender_type == "Water":
            multiplier = 0.5
            
    elif move_type == "Grass":
        if defender_type == "Water":
            multiplier = 2.0
        elif defender_type == "Fire":
            multiplier = 0.5

    # One-way decisions for the UI message
    if multiplier == 2.0:
        print("\nMatchup: It's super effective!")
    elif multiplier == 0.5:
        print("\nMatchup: It's not very effective...")
    else:
        print("\nMatchup: Normal effectiveness.")

    # Calculate damage 
    estimated_damage = power * multiplier
    print(f"Estimated Damage: {estimated_damage}")

    # Multi-way decision-making guide
    if estimated_damage >= target_hp:
        print("Rotom Recommendation: GO FOR IT! This is a guaranteed Knock Out!")
    elif estimated_damage >= (target_hp / 2):
        print("Rotom Recommendation: Good play. This will take at least half their health.")
    else:
        print("Rotom Recommendation: WARNING! Damage is too low. Consider switching your Pokemon!")

except ValueError:
    # Safety net for non-numeric input
    print("\nRotom Dex Error: Bzzzt! You must enter numeric values for Power and HP!")

print("\n--- Calculation Complete ---")

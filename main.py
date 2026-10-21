import random 

def main():
    print("Welcome to Python Battle Simulator!")

    player_name = input("Enter your character's name: ")
    player_health = 100
    max_health = 100
    healing_amount = 20
    healing_potions = 3

    print("\n--- Character Stats ---")
    print(f"Name: {player_name}")
    print(f"Health: {player_health} HP")
    print("Attack Damage: 10-20")

    enemy_name = "Goblin"
    enemy_health = 50
    
    skeleton_name = "Skeleton"
    skeleton_health = 65
    skeleton_damage = 18

    enemies = [enemy_name, skeleton_name]
    selected_enemy = random.choice(enemies)
    enemy_name = selected_enemy
    if enemy_name == skeleton_name:
        enemy_health = skeleton_health
        enemy_max_damage = skeleton_damage
    else:
        enemy_max_damage = 15

    print("\n--- Enemy Appears! ---")
    print(f"Enemy: {enemy_name}")
    print(f"Health: {enemy_health} HP")
    print(f"Attack Damage: 5-{enemy_max_damage}")

    print("\n--- Battle Begins! ---")

    while player_health > 0 and enemy_health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Defend")
        print("3. Heal")
        print(f"Healing Potions: {healing_potions}")
        choice = input("Choose your action (1, 2, or 3.): ")

        if choice not in ("1", "2", "3"):
            print("Invalid choice! Please enter 1, 2, or 3.")
            continue 
       
        defending = False 

        if choice == "1":
            print(f"{player_name} attacks {enemy_name}!")
            
            damage = random.randint(10, 20)
            critical_roll = random.randint(1, 100)
            if critical_roll <= 20:
                damage *= 2
                print("💥 CRITICAL HIT! Double damage!")
            enemy_health -= damage

            if enemy_health < 0:
               enemy_health = 0
                
            print(f"{enemy_name} takes {damage} damage!")
            print(f"{enemy_name} has {enemy_health} HP remaining.")

        elif choice == "2":
            defending = True
            print(f"{player_name} raises their shield!")

        else:
            if healing_potions > 0:
                print(f"{player_name} prepares to heal!")
                player_health = min(player_health + healing_amount, max_health)
                healing_potions -= 1
                print(f"{player_name} has {player_health} HP after healing!")

            else:
                print("You have no healing potions left!")
        
        if enemy_health <= 0:
            break 

        print(f"\n{enemy_name} attacks {player_name}!")

        hit_roll = random.randint(1, 100)
        if hit_roll <= 80:
            enemy_damage = random.randint(5, enemy_max_damage)

            if defending:
                damage = enemy_damage// 2
            else:
                damage = enemy_damage

            player_health = max(0, player_health - damage)

            print(f"{player_name} takes {damage} damage!")
            print(f"{player_name} has {player_health} HP remaining.")

        else:
            print(f"{enemy_name} missed the attack!")

    if enemy_health <= 0:
        print("\n=== VICTORY! ===")
        print(f"{player_name} defeated the {enemy_name}!")

    elif player_health <= 0:
        print("\n=== GAME OVER ===")
        print(f"{player_name} was defeated by the {enemy_name}!")

main()
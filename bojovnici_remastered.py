import random

name_array = ["Jake", "Liam", "Sam", "Martin", "Peter", "Josh"]
game_running = True

player = {
    "name": input("Imput your name: "),
    "health": random.randint(15, 250),
    "id": 1,
    "basic_attack": 2,
    "special_attack": 2,
    "heal": 2,
    "chosen_action": "",
    "chosen_attack": "",
}

enemy = {
    "name": random.choice(name_array),
    "health": random.randint(15, 250),
    "id": 2,
    "basic_attack": 2,
    "special_attack": 2,
    "heal": 2,
    "chosen_action": "",
    "chosen_attack": "",
}
def choose_action(attacker, defender):
    while game_running == True:
        if attacker["id"] == 1:
            print(f"You have {attacker["health"]} hp.")
            print("Heal ready") if attacker["heal"] == 2 else print("Heal not ready")
            print("Basic attack ready") if attacker["basic_attack"] == 2 else print("Basic attack not ready")
            print("Special attack ready") if attacker["special_attack"] == 2 else print("Special attack not ready")
            print(f"Your enemy has {defender["health"]} hp.")
            action = input("Based on previously shown chart, choose action (heal/attack): ")
            if action == "attack":
                choose_attack(attacker=attacker, defender=defender)
            elif action == "heal" and attacker["heal"] == 2:
                print(attacker["heal"])
                heal(attacker=attacker, defender=defender)
            else:
                print("You have inputed wrong word! You need to input either `attack` or `heal`!")
                choose_action(attacker=attacker, defender=defender)
        else:
            print("Ai is choosing!")
            list_of_actions = ["heal", "attack"]
            action = random.choice(list_of_actions)
            if action == "heal" and attacker["heal"] == 2:
                heal(attacker=attacker, defender=defender)
            elif action == "attack" and (attacker["basic_attack"] == 2 or attacker["special_attack"] == 2):
                choose_attack(attacker=attacker, defender=defender)

def check_health(defender):
    if defender["health"] <= 0:
        return False

def choose_attack(attacker, defender):
    if attacker["basic_attack"] == 2 or attacker["special_attack"] == 2:
        if attacker["basic_attack"] == 2:
            if attacker["special_attack"] == 2:
                if attacker["id"] == 1:
                    attack = input("You have your basic and special attack ready, which one do you want to use? basic/special: ")
                else:
                    list_of_attacks = ["basic", "special"]
                    chosen_attack = random.choice(list_of_attacks)
                    attack = chosen_attack        
            else:
                attack = "basic"
        else:
            attack = "special"
        if attack == "basic":
            if attacker["id"] == 1:
                print("You`re attacking with basic attack")
            attacker["chosen_attack"] = "basic_attack"
        else:
            if attacker["id"] == 1:
                print("You`re attacking with special attack")
            attacker["chosen_attack"] = "special_attack"
        hit(attacker=attacker, defender=defender)
    else:
        print("You dont have any attack ready!")
        choose_action(attacker=attacker)

def disable_and_eneable_actions(attacker, action):
    pass
def heal(attacker, defender):
    chosen_action = "heal"
    heal_amount = random.randint(15, 75)
    attacker["health"] += heal_amount
    print(f"After healing for {heal_amount} heals, {attacker["name"]} is left with {attacker["health"]} health")
    disable_and_eneable_actions(attacker=attacker, action=chosen_action)
    choose_action(enemy, player) if attacker["id"] == 1 else choose_action(player, enemy)


def hit(attacker, defender):
    will_hit = random.randint(0, 1)
    if will_hit == 1:
        chosen_attack = attacker["chosen_attack"]
        if chosen_attack == "basic_attack":
            damage = random.randint(1, 25)
            disable_and_eneable_actions(attacker=attacker, action=chosen_attack)
        elif chosen_attack == "special_attack":
            damage = random.randint(25, 100)
            disable_and_eneable_actions(attacker=attacker, action=chosen_attack)
        defender["health"] -= damage
        print(f"{attacker["name"]} hit {defender["name"]} for {damage} damage")
    else:
        print(f"{attacker["name"]} has missed!")
    game_running = check_health(defender=defender)
    choose_action(enemy, player) if attacker["id"] == 1 else choose_action(player, enemy)
choose_action(player, enemy)
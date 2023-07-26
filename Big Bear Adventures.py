import time
import random

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return self.name

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)
        self.level = 1
        self.exp = 0
        self.inventory = {}

    def add_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name] += quantity
        else:
            self.inventory[item.name] = quantity

    def remove_item(self, item, quantity=1):
        if item.name in self.inventory:
            if self.inventory[item.name] >= quantity:
                self.inventory[item.name] -= quantity
                return True
            else:
                return False
        else:
            return False

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def delay_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.3)

def show_inventory(player):
    print("\n你的背包：")
    for item_name, quantity in player.inventory.items():
        print(f"{item_name}: {quantity}个")

def choose_action():
    print("\n你可以做以下操作：")
    print("1. 查看角色状态")
    print("2. 查看背包")
    print("3. 探险")
    print("4. 完成任务")
    print("5. 退出游戏")
    while True:
        try:
            choice = int(input("请输入你的选择（1/2/3/4/5）："))
            if 1 <= choice <= 5:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def show_character_status(player):
    print(f"\n{name}等级：{player.level}")
    print(f"生命值：{player.health}")
    print(f"攻击力：{player.attack}")
    print(f"经验值：{player.exp}/{player.level * 100}")

def explore(player):
    delay_print("\n你踏上了哆啦A梦的冒险之旅。")
    encounter = random.choice(["monster", "item", "nothing"])
    
    if encounter == "monster":
        monster_attack(player)
    elif encounter == "item":
        collect_item(player)
    else:
        delay_print("这片区域看起来平静无事。")

def monster_attack(player):
    delay_print("\n突然，一只机器猫出现在你面前！")
    while player.health > 0 and player_attack_choice(player):
        delay_print(f"\n你的生命值：{player.health}  机器猫的生命值：{player.attack}")
        player.attack_doraemon()
        if player.health > 0:
            delay_print("机器猫反击了！")
            player.doraemon_attack()

def player_attack_choice(player):
    while True:
        choice = input("你要攻击（A）还是逃跑（E）？").lower()
        if choice == "a":
            return True
        elif choice == "e":
            delay_print("你逃跑了。")
            break
        else:
            delay_print("无效的选择，请重新输入。")
    return False

def collect_item(player):
    item = random.choice(item_list)
    quantity = random.randint(1, 5)
    player.add_item(item, quantity)
    delay_print(f"你发现了{item.name} x {quantity}。")

def complete_task(player):
    if player.inventory.get("藏宝图", 0) >= 1:
        player.remove_item(Item("藏宝图"))
        player.exp += 50
        delay_print("你完成了任务，获得了50经验值。")
    else:
        delay_print("你没有藏宝图，无法完成任务。")

def play_game():
    player_name = input("请输入你的角色名字：")
    player = Player(player_name)
    
    item_list = [
        Item("铜板", "普通的铜板"),
        Item("木材", "用于建造的木材"),
        Item("食物", "补充生命值的食物"),
        Item("藏宝图", "寻找宝藏的地图")
    ]

    delay_print(f"欢迎来到《哆啦A梦的冒险》游戏，{player_name}！")
    delay_print("你将在这片神奇的世界中历险。")

    while True:
        show_character_status(player)
        action = choose_action()

        if action == 1:
            show_character_status(player)
        elif action == 2:
            show_inventory(player)
        elif action == 3:
            explore(player)
        elif action == 4:
            complete_task(player)
        elif action == 5:
            delay_print("谢谢你玩《哆啦A梦的冒险》游戏，再见！")
            exit()

if __name__ == "__main__":
    play_game()

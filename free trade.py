import time
import random

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# 其他类和函数不变，省略...

def trade_items(player1, player2):
    print(f"\n欢迎来到交易所，{player1.name}和{player2.name}！")
    show_inventory(player1)
    show_inventory(player2)

    item_name = input(f"{player1.name}，请输入你要交易的道具名字：")
    if item_name not in player1.inventory:
        delay_print(f"{player1.name}没有该道具，无法交易。")
        return

    quantity = int(input(f"{player1.name}，请输入你要交易的{item_name}数量："))
    if player1.inventory[item_name] < quantity:
        delay_print(f"{player1.name}没有足够的{item_name}，无法交易。")
        return

    price = int(input(f"{player2.name}，请输入你愿意出售{item_name}的价格："))
    if price <= 0:
        delay_print(f"{player2.name}价格必须为正整数。")
        return

    total_cost = price * quantity
    if total_cost > player2.inventory.get("铜板", 0):
        delay_print(f"{player2.name}没有足够的铜板，无法交易。")
        return

    player1.remove_item(Item(item_name), quantity)
    player1.add_item(Item(item_name), quantity)
    player1.inventory["铜板"] += total_cost
    player2.remove_item(Item(item_name), quantity)
    player2.inventory["铜板"] -= total_cost

    delay_print(f"交易完成！{player1.name}交易了{quantity}个{item_name}，支付了{total_cost}个铜板。")
    show_inventory(player1)
    show_inventory(player2)

def choose_action():
    print("\n你可以做以下操作：")
    print("1. 查看角色状态")
    print("2. 查看背包")
    print("3. 探险")
    print("4. 完成任务")
    print("5. 自由交易")
    print("6. 退出游戏")
    while True:
        try:
            choice = int(input("请输入你的选择（1/2/3/4/5/6）："))
            if 1 <= choice <= 6:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def play_game():
    # 玩家创建和游戏主循环等不变，省略...
    
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
            other_player = select_other_player(player)
            if other_player:
                trade_items(player, other_player)
        elif action == 6:
            delay_print("谢谢你玩《哆啦A梦的冒险》游戏，再见！")
            exit()

if __name__ == "__main__":
    play_game()

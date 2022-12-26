# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")



##local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

##Global_Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#     drink_potion()

# drink_potion()     #error


##There is no block scope in python
# if 3>2:
#     a_varible = 10
# print(a_varible)

# for t in range(2):
#     print("s")
# print(t)

# game_level = 3
# enemies = ["skeleton","Zombie","Alien"]
# if game_level<5:
#     new_enemy = enemies[0]

# print(new_enemy)

# game_level = 3
# def create_enemy():
#     enemies = ["skeleton","Zombie","Alien"]
#     if game_level<5:
#         new_enemy = enemies[0]
#     print(new_enemy)

# print(new_enemy)      #now error becausewithin the function there is local scope



'''so 
if you crate a varible within a function then its only available within that function.

but if you create a variable in if block,while loop,for loop,or anything that has indetation and colon then that is not count as creating a separate local scope'''
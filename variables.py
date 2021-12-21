#Состояние организма
health = 30
hunger = 20
fatigue = 50
thirst = 20
frostbite = 10
disease = 0
stage_of_disease = 0

#Координати игрока
pos_y = 0

#Размеры игрока
height = 100
widht = 35

#Движение
speed = 1
jump_speed = 6
acceleration = 3*jump_speed/20
speed_of_jump = jump_speed
move_right = False
move_left = False
jump = False
right = True
move_right_time = 0
move_left_time = 0

#Вспомогательные переменные
sleep = 100/8
hand = 1
time = 0
H = 0
plate = []
inventory = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
hand_image = 1
block_size = 20
new_y = 0

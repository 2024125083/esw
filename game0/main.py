import time
from PIL import Image
from joystick import Joystick
from player import Player
from arrow import Arrow
from castle import Castle
from fence import Fence
from soldier import Soldier

background = Image.open("images/background.png").convert("RGB")
joystick = Joystick()
main_player = Player()
castle = Castle()
arrows = [] # 화살 객체가 1개면 이상해진다
cooltime = 0 # 연사제한 : 쿨타임 0일때만 사용 가능 
fences = []
for x in [70, 90, 110, 130, 150, 170]:
    fences.append(Fence(x, 70))
    fences.append(Fence(x, 170))
for y in [90, 110, 130, 150]:
    fences.append(Fence(70, y))
    fences.append(Fence(170, y))
enemy_soldier = Soldier(110,-10)



while True:
    image = background.copy()  # 배경 
    main_player.move(joystick)
    enemy_soldier.move()

    if cooltime > 0:
        cooltime -= 1

    if not joystick.button_A.value and cooltime == 0: # 눌리면 false, 눌리면 객체 만듬
        arrows.append(Arrow(main_player.x,main_player.y,main_player.dir_x,main_player.dir_y))
        cooltime = 10

    for arrow in arrows:
            arrow.move()

    arrows = [arrow for arrow in arrows if not arrow.is_out()]
    for fence in fences:
        fence.draw(image)
    castle.draw(image)
    main_player.draw(image)
    enemy_soldier.draw(image)

    for arrow in arrows:
            arrow.draw(image)

    joystick.disp.image(image)
    time.sleep(0.03)
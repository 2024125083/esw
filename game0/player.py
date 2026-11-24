import config
from PIL import Image


class Player: 
    def __init__(self):
        self.x = 120 
        self.y = 150        # 플레이어 위치
        self.size = 16
        self.hp = config.PLAYER_HP # 5
        self.speed = config.PLAYER_SPEED # 3
        self.dir_x = 1
        self.dir_y = 0 # 위의 방향을 보면서 시작 

        self.img = Image.open("images/player.png").convert("RGBA")


    def move(self,joystick):
        
        dx = 0
        dy = 0

        if not joystick.button_L.value:
            dx -= 1
        if not joystick.button_R.value:
            dx += 1
        if not joystick.button_U.value:
            dy -= 1
        if not joystick.button_D.value:
            dy += 1

        if dx != 0 or dy != 0:  # 둘 중 하나라도 0이 아니면 보는 방향으로 쓰기
            self.dir_x = dx
            self.dir_y = dy

        self.x += dx * self.speed
        self.y += dy * self.speed

        if self.x < 0:
            self.x = 0
        if self.x > 240:
            self.x = 240
        if self.y < 0:
            self.y = 0
        if self.y > 240:
            self.y = 240



    def draw(self,image):
        image.paste(self.img, (self.x - self.img.width // 2, self.y - self.img.height // 2), self.img)    # 왼쪽 위 모서리에 그림 / 그림의 가운데를 self.x,y로 둘거임





    
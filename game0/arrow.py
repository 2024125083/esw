import config
from PIL import Image

ANGLES = {
    (1,0) : 0, # 오른쪽
    (1,-1): 45, # 오른쪽 위 대각선
    (0,-1): 90, # 위
    (-1,-1): 135, # 왼쪽 위 대각선
    (-1,0): 180, # 왼쪽
    (-1,1): 225, # 왼쪽 아래 대각선
    (0,1): 270, # 아래
    (1,1): 315 # 오른쪽 아래
}

class Arrow: 
    def __init__(self,x,y,dir_x,dir_y):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.speed = config.ARROW_SPEED

        sample = Image.open("images/arrow.png").convert("RGBA")
        angle = ANGLES[(self.dir_x,self.dir_y)]
        self.img = sample.rotate(angle,expand = True)

        

    def move(self):
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed

    def is_out(self):
        return self.x < 0 or self.x > 240 or self.y < 0 or self.y > 240 # 나가면 없앤다
    
    def draw(self,image):
        image.paste(self.img, (self.x - self.img.width // 2, self.y - self.img.height // 2), self.img)


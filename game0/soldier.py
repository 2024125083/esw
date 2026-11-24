from PIL import Image

class Soldier:
    def __init__(self, x, y):         
        self.x = x
        self.y = y
        self.speed = 1                
        self.img = Image.open("images/sword.png").convert("RGBA")   # 칼 병사 그림

    def move(self):                    
        if self.y < 50:                
            self.y += self.speed       
                                      

    def draw(self, image):             
        image.paste(self.img, (self.x - self.img.width // 2, self.y - self.img.height // 2), self.img)
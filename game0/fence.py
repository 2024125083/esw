from PIL import Image

class Fence:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = Image.open("images/fence.png").convert("RGBA")

    def draw(self, image):
        image.paste(self.img, (self.x - self.img.width // 2, self.y - self.img.height // 2), self.img)




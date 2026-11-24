from PIL import Image

class Castle:
    def __init__(self):
        self.x = 120
        self.y = 120
        self.img = Image.open("images/castle.png").convert("RGBA")

    def draw(self, image):
        image.paste(self.img, (self.x - self.img.width // 2, self.y - self.img.height // 2), self.img)
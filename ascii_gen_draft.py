from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

class AsciiImageScale:

    def __init__(self, charecter_size: int, columns: int, rows: int) -> None:
        self.width = charecter_size * columns
        self.heigt = charecter_size * rows

    def __str__(self) -> str:
        return f"'width': {self.width}, 'height': {self.heigt}"

def create_image_from_path(path: Path) -> Image.Image:
    return Image.open(path.open("rb"))

def scale_image(image: Image.Image, scale: AsciiImageScale) -> Image.Image:
    return image.resize(size=(scale.width,scale.heigt))

def main() -> None:
    FONT_SIZE = 16
    COLS = 120
    ROWS = 80
    GRAYSCALE_CHARS = '@%#*+=-:. '
    ascii_image_scale = AsciiImageScale(charecter_size=FONT_SIZE, columns=COLS, rows=ROWS)
    path_to_image: Path = Path("assets/snufkin.jpg")
    image = create_image_from_path(path_to_image).convert("L")
    resized_image: Image.Image = scale_image(image, ascii_image_scale)
    ascii_art: str = ""
    for x in range(resized_image.width):
        for y in range(resized_image.height):
            ascii_art += GRAYSCALE_CHARS[int((resized_image.getpixel((x,y))*9)/255)]
        ascii_art += "\n"
    ascii_art_image = Image.new("RGB", resized_image.size)
    d = ImageDraw.Draw(ascii_art_image)
    d.multiline_text((0,0), ascii_art,fill=(255,255,255),font=ImageFont.truetype("cour.ttf",size=16))
    ascii_art_image.save(open("assets/ascii_art.jpg","w"))



if __name__ == "__main__":
    main()
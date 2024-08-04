from PIL import Image, ImageFont, ImageDraw, ImageColor
from favicons import Favicons

def text_to_image(
text: str,
font_filepath: str,
font_size: int,
color: (int, int, int), #color is in RGB
font_align="center"):
    font = ImageFont.truetype(font_filepath, 620)
    font2 = ImageFont.truetype('prosto/Prosto.ttf', 240)
    img = Image.new("RGBA", (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text(
        (950, 910),
        text,
        (0, 0, 100),
        anchor="rs",
        font=font,
        #align='center'
    )
    draw.text(
        (500, 30),
        'MDCC',
        color,
        anchor="mt",
        font=font2,
        #align='center'
    )
    draw.rectangle([(0, 0), (40, 1000)] , fill=color, outline=None)
    draw.rectangle([(40, 960), (1000, 1000)] , fill=(0, 0, 100), outline=None)
    # img.show()
    # img.save("a_test.png")
    return img

if __name__ == '__main__':
    res = text_to_image(
        'MFV',
        'targa/Targa.ttf',
        600,
        (255, 153, 0)
    )
    print(res)
    res.show()
    res.save("mfv.png")


    YOUR_ICON = "mfv.png"
    WEB_SERVER_ROOT = "favicon"

    with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
        favicons.generate()

import shutil
import os

from PIL import Image, ImageFont, ImageDraw, ImageColor
from favicons import Favicons

def text_to_image(app_name: str, environment: str):
    orange = (255, 153, 0)
    blue = (0, 0, 100)
    font = ImageFont.truetype('targa/Targa.ttf', 620)
    font2 = ImageFont.truetype('prosto/Prosto.ttf', 240)
    img = Image.new("RGBA", (1000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text(
        (950, 910),
        app_name,
        blue,
        anchor="rs",
        font=font,
    )
    draw.text(
        (500, 30),
        environment,
        orange,
        anchor="mt",
        font=font2,
    )
    draw.rectangle([(0, 0), (40, 1000)] , fill=orange)
    draw.rectangle([(40, 960), (1000, 1000)] , fill=blue)
    return img

if __name__ == '__main__':
    app_name = 'MFV'

    shutil.rmtree(app_name)
    os.mkdir(app_name)
    environments = ['MDCC', 'TEST', 'DEV', 'DEV 1', 'DEV 2', 'DEV 3', 'DEV 4', 'DEV 5', 'BUILD']
    for environment in environments:
        os.mkdir(f"{app_name}/{environment}")
        os.mkdir(f"{app_name}/{environment}/favicon")
        res = text_to_image(
            app_name,
            environment
        )
        print(res)
#        res.show()
        res.save(f"{app_name}/{environment}/{environment}.png")


        YOUR_ICON = f"{app_name}/{environment}/{environment}.png"
        WEB_SERVER_ROOT = f"{app_name}/{environment}/favicon"

        with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
            favicons.generate()

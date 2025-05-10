import pystray
from PIL import Image
from utils.menu import menu

image = Image.open('assets/icon.ico')

icon = pystray.Icon(
    name='test',
    icon=image,
    menu=menu(),
)
icon.run()

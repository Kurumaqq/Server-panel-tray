import pystray
from PIL import Image
from menu import menu

image = Image.open('icon.jpg')


icon = pystray.Icon(
    name='test',
    icon=image,
    menu=menu(),
)
icon.run()

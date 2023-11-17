from PIL import Image


def test(a, b):
    img = Image.open('image.png').convert('RGB').resize((a, b))
    img.show()


test(500, 500)
for i in range(3):
    print('Ну...')

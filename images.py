from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save("grey.png", "png")

crooked = filtered_img.rotate(90)
crooked.save('crooked.png', 'png')

box = (100, 100, 400, 400)
crop = filtered_img.crop(box)
crop.save('crop.png', 'png')

resize = filtered_img.resize((300, 300))
resize.save('resized.png', 'png')

img2 = Image.open('./astro.jpg')
img2.thumbnail((400,400))
img2.save('astro-thumb.jpg')

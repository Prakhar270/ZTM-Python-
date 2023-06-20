from PIL import Image, ImageFilter

img2 = Image.open('./scripting_with_python/working_image/astro.jpg')

#resize = img2.resize((300, 300))
img2.thumbnail((400, 400))
img2.save('./scripting_with_python/working_image/astro1_thumbnail.png')
print(img2.size)
#resize.show()
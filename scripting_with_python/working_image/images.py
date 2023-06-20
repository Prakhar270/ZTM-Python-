from PIL import Image, ImageFilter


img = Image.open('./scripting_with_python/working_image/pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img3 = img.filter(ImageFilter.SHARPEN)
filtered_img4 = img.convert('L')
roated = filtered_img3.rotate(90)
resize = filtered_img2.resize((300, 300))
box = (100, 100, 400, 400)
regions = filtered_img2.crop(box)
regions.save('./scripting_with_python/working_image/crop.png ', 'png')
#print(img.format)
#print(img.size)
#print(img.mode)
#filtered_img3.show()

from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')

# print(img.format)   # JPEG
# print(img.size)     # (640, 640)
# print(img.mode)     # RGB
# print(dir(img))       # prints methods we can run for img object

# Filter BLU
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save('blur.png', 'png') # png supports these filters, jpg doesn't

# Convert, Show, Rotate
# filtered_img = img.convert('L')     # greyed out the image
# filtered_img.save('grey.png', 'png') 

# filtered_img.show() # Shows image

# crooked = filtered_img.rotate(90) # rotates 90 degrees counterclockwise
# crooked.save('grey.png', 'png')

# resize = filtered_img.resize((300, 300))
# resize.save('grey.png', 'png')

# box = (100, 100, 400, 400)
# cropped = filtered_img.crop(box)
# cropped.save('cropped.png', 'png')

# Resize Image
img = Image.open('./astro.jpg')
# print(img.size) # (5611, 5339)
# new_img = img.resize((400, 400)) # aspect ratio changed, original doesnt have this ratio
# new_img.save('thumbnail.jpg')

# Useful when creating a profile pic
img.thumbnail((400, 380)) # this way keeps the aspect ratio, doesnt return a new object, modifies itself
img.save('thumbnail.jpg')
print(img.size) # (399, 380) funny it is 400 in the video





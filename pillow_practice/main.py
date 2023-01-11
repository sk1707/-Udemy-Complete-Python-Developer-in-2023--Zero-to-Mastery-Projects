from PIL import Image, ImageFilter
img = Image.open('/Users/bapnarb/Desktop/watermelon.jpeg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')
filtered_img = Image.open('/Users/sonia/PyCharm/pythonProject/pillow_practice/blur.png')
print(img.format)
print(filtered_img.format)

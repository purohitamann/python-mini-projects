from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import os

if os.path.exists('./edited') and os.path.isdir('./edited') or os.path.exists('./images') and os.path.isdir('./images'):
    pass
else:
    os.mkdir('./edited') and os.mkdir('./images')
    
pathOut= './edited/'
pathIn = './images/'

for filename in os.listdir(pathIn):
    items = os.listdir(pathOut)
    i= len(items) + 1
    
    img = Image.open(pathIn + filename)
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    
    factor= 1.5
    enhancer = ImageEnhance.Contrast(edit)
    
    edit = enhancer.enhance(factor)
    edit = ImageOps.fit(edit, (200,200))
    new_fielname = filename.split(filename)[0] 
    newPath =f'{pathOut}{new_fielname}{i}.jpg'
    edit.save(newPath)
    print('Edited: ', filename)
    
print(f'All images edited successfully, check the edited folder for your images.  \n {newPath}')



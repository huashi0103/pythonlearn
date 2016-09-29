from PIL import Image

im=Image.open('D:\\Desktop\\psb.jpg')
w,h=im.size
print('Original image size:%sx%s'%(w,h))
im.thumbnail((w//2,h//2))
print('resize image to:%sx%s'%(w//2,h//2))
im.save('D:\\Desktop\\psb1.jpg','jpeg')

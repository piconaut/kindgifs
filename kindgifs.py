#!/usr/bin/python3

from PIL import Image
import sys
import imageio
import os

height = 10
bgcolour = (255,117,255)
txtcolour = (255,255,255)

y0 = 2

row0 = {'a':[txtcolour,txtcolour,txtcolour],'b':[txtcolour,txtcolour,txtcolour],'c':[bgcolour,txtcolour,txtcolour],'d':[txtcolour,txtcolour,bgcolour],'e':[txtcolour,txtcolour,txtcolour],'f':[txtcolour,txtcolour,txtcolour],'g':[bgcolour,txtcolour,txtcolour],'h':[txtcolour,bgcolour,txtcolour],'i':[txtcolour,txtcolour,txtcolour],'j':[txtcolour,txtcolour,txtcolour],'k':[txtcolour,bgcolour,txtcolour],'l':[txtcolour,bgcolour,bgcolour],'m':[txtcolour,txtcolour,txtcolour],'n':[txtcolour,txtcolour,bgcolour],'o':[bgcolour,txtcolour,txtcolour],'p':[txtcolour,txtcolour,txtcolour],'q':[bgcolour,txtcolour,bgcolour],'r':[txtcolour,txtcolour,txtcolour],'s':[bgcolour,txtcolour,txtcolour],'t':[txtcolour,txtcolour,txtcolour],'u':[txtcolour,bgcolour,txtcolour],'v':[txtcolour,bgcolour,txtcolour],'w':[txtcolour,bgcolour,txtcolour],'x':[txtcolour,bgcolour,txtcolour],'y':[txtcolour,bgcolour,txtcolour],'z':[txtcolour,txtcolour,txtcolour],' ':[bgcolour,bgcolour,bgcolour]}

row1 = {'a':[txtcolour,bgcolour,txtcolour],'b':[txtcolour,bgcolour,txtcolour],'c':[txtcolour,bgcolour,bgcolour],'d':[txtcolour,bgcolour,txtcolour],'e':[txtcolour,bgcolour,bgcolour],'f':[txtcolour,bgcolour,bgcolour],'g':[txtcolour,bgcolour,bgcolour],'h':[txtcolour,bgcolour,txtcolour],'i':[bgcolour,txtcolour,bgcolour],'j':[bgcolour,txtcolour,bgcolour],'k':[txtcolour,bgcolour,txtcolour],'l':[txtcolour,bgcolour,bgcolour],'m':[txtcolour,txtcolour,txtcolour],'n':[txtcolour,bgcolour,txtcolour],'o':[txtcolour,bgcolour,txtcolour],'p':[txtcolour,bgcolour,txtcolour],'q':[txtcolour,bgcolour,txtcolour],'r':[txtcolour,bgcolour,txtcolour],'s':[txtcolour,bgcolour,bgcolour],'t':[bgcolour,txtcolour,bgcolour],'u':[txtcolour,bgcolour,txtcolour],'v':[txtcolour,bgcolour,txtcolour],'w':[txtcolour,bgcolour,txtcolour],'x':[txtcolour,bgcolour,txtcolour],'y':[txtcolour,bgcolour,txtcolour],'z':[bgcolour,bgcolour,txtcolour],' ':[bgcolour,bgcolour,bgcolour]}

row2 = {'a':[txtcolour,txtcolour,txtcolour],'b':[txtcolour,txtcolour,bgcolour],'c':[txtcolour,bgcolour,bgcolour],'d':[txtcolour,bgcolour,txtcolour],'e':[txtcolour,txtcolour,bgcolour],'f':[txtcolour,txtcolour,bgcolour],'g':[txtcolour,bgcolour,bgcolour],'h':[txtcolour,txtcolour,txtcolour],'i':[bgcolour,txtcolour,bgcolour],'j':[bgcolour,txtcolour,bgcolour],'k':[txtcolour,txtcolour,bgcolour],'l':[txtcolour,bgcolour,bgcolour],'m':[txtcolour,bgcolour,txtcolour],'n':[txtcolour,bgcolour,txtcolour],'o':[txtcolour,bgcolour,txtcolour],'p':[txtcolour,txtcolour,txtcolour],'q':[txtcolour,bgcolour,txtcolour],'r':[txtcolour,txtcolour,bgcolour],'s':[txtcolour,txtcolour,txtcolour],'t':[bgcolour,txtcolour,bgcolour],'u':[txtcolour,bgcolour,txtcolour],'v':[txtcolour,bgcolour,txtcolour],'w':[txtcolour,bgcolour,txtcolour],'x':[bgcolour,txtcolour,bgcolour],'y':[txtcolour,txtcolour,txtcolour],'z':[bgcolour,txtcolour,bgcolour],' ':[bgcolour,bgcolour,bgcolour]}

row3 = {'a':[txtcolour,bgcolour,txtcolour],'b':[txtcolour,bgcolour,txtcolour],'c':[txtcolour,bgcolour,bgcolour],'d':[txtcolour,bgcolour,txtcolour],'e':[txtcolour,bgcolour,bgcolour],'f':[txtcolour,bgcolour,bgcolour],'g':[txtcolour,bgcolour,txtcolour],'h':[txtcolour,bgcolour,txtcolour],'i':[bgcolour,txtcolour,bgcolour],'j':[bgcolour,txtcolour,bgcolour],'k':[txtcolour,bgcolour,txtcolour],'l':[txtcolour,bgcolour,bgcolour],'m':[txtcolour,bgcolour,txtcolour],'n':[txtcolour,bgcolour,txtcolour],'o':[txtcolour,bgcolour,txtcolour],'p':[txtcolour,bgcolour,bgcolour],'q':[txtcolour,txtcolour,bgcolour],'r':[txtcolour,bgcolour,txtcolour],'s':[bgcolour,bgcolour,txtcolour],'t':[bgcolour,txtcolour,bgcolour],'u':[txtcolour,bgcolour,txtcolour],'v':[txtcolour,txtcolour,txtcolour],'w':[txtcolour,txtcolour,txtcolour],'x':[txtcolour,bgcolour,txtcolour],'y':[bgcolour,bgcolour,txtcolour],'z':[txtcolour,bgcolour,bgcolour],' ':[bgcolour,bgcolour,bgcolour]}

row4 = {'a':[txtcolour,bgcolour,txtcolour],'b':[txtcolour,txtcolour,txtcolour],'c':[bgcolour,txtcolour,txtcolour],'d':[txtcolour,txtcolour,txtcolour],'e':[txtcolour,txtcolour,txtcolour],'f':[txtcolour,bgcolour,bgcolour],'g':[txtcolour,txtcolour,txtcolour],'h':[txtcolour,bgcolour,txtcolour],'i':[txtcolour,txtcolour,txtcolour],'j':[txtcolour,txtcolour,bgcolour],'k':[txtcolour,bgcolour,txtcolour],'l':[txtcolour,txtcolour,txtcolour],'m':[txtcolour,bgcolour,txtcolour],'n':[txtcolour,bgcolour,txtcolour],'o':[txtcolour,txtcolour,bgcolour],'p':[txtcolour,bgcolour,bgcolour],'q':[bgcolour,txtcolour,txtcolour],'r':[txtcolour,bgcolour,txtcolour],'s':[txtcolour,txtcolour,bgcolour],'t':[bgcolour,txtcolour,bgcolour],'u':[bgcolour,txtcolour,txtcolour],'v':[bgcolour,txtcolour,bgcolour],'w':[txtcolour,txtcolour,txtcolour],'x':[txtcolour,bgcolour,txtcolour],'y':[txtcolour,txtcolour,txtcolour],'z':[txtcolour,txtcolour,txtcolour],' ':[bgcolour,bgcolour,bgcolour]}

if len(sys.argv) > 1:
  text = ' '.join(sys.argv[1:])
else:
  text = input('Say something! (be kind)\n > ')

text = text.lower()

pixels = []
# Five columns at left
for i in range(height):
  pixels.append([])
  for j in range(5):
    pixels[i].append(bgcolour)

for char in text:
  for i in range(3):
    pixels[0].append(bgcolour)
    pixels[1].append(bgcolour)
    pixels[y0].append(row0[char][i])
    pixels[y0+1].append(row1[char][i])
    pixels[y0+2].append(row2[char][i])
    pixels[y0+3].append(row3[char][i])
    pixels[y0+4].append(row4[char][i])
    pixels[7].append(bgcolour)
    pixels[8].append(bgcolour)
    pixels[9].append(bgcolour)
  for i in range(10):
    pixels[i].append(bgcolour)

for i in range(height):
  pixels.append([])
  for j in range(4):
    pixels[i].append(bgcolour)

pixels[4][2] = txtcolour
pixels[5][1] = txtcolour
pixels[5][3] = txtcolour
pixels[6][2] = txtcolour

pixels[4][-3] = txtcolour
pixels[5][-2] = txtcolour
pixels[5][-4] = txtcolour
pixels[6][-3] = txtcolour

width = len(pixels[0])

# Need to rearrange pixels to be all in one list
pixels_list = []
for i in pixels:
  for j in i:
    pixels_list.append(j)

img = Image.new('RGB',(width,height))
img.putdata(pixels_list)

basewidth = width*8
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize))#, Image.ANTIALIAS)
img.save('img1_kindgifs.png')


y0 = 3


pixels = []
# Five columns at left
for i in range(height):
  pixels.append([])
  for j in range(5):
    pixels[i].append(bgcolour)

for char in text:
  for i in range(3):
    pixels[0].append(bgcolour)
    pixels[1].append(bgcolour)
    pixels[2].append(bgcolour)
    pixels[y0].append(row0[char][i])
    pixels[y0+1].append(row1[char][i])
    pixels[y0+2].append(row2[char][i])
    pixels[y0+3].append(row3[char][i])
    pixels[y0+4].append(row4[char][i])
    pixels[8].append(bgcolour)
    pixels[9].append(bgcolour)
  for i in range(10):
    pixels[i].append(bgcolour)

for i in range(height):
  pixels.append([])
  for j in range(4):
    pixels[i].append(bgcolour)

pixels[3][2] = txtcolour
pixels[4][1] = txtcolour
pixels[4][3] = txtcolour
pixels[5][2] = txtcolour

pixels[3][-3] = txtcolour
pixels[4][-2] = txtcolour
pixels[4][-4] = txtcolour
pixels[5][-3] = txtcolour

width = len(pixels[0])

# Need to rearrange pixels to be all in one list
pixels_list = []
for i in pixels:
  for j in i:
    pixels_list.append(j)

img = Image.new('RGB',(width,height))
img.putdata(pixels_list)

basewidth = width*8
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize))#, Image.ANTIALIAS)
img.save('img2_kindgifs.png')

images = [imageio.imread('img1_kindgifs.png'),imageio.imread('img2_kindgifs.png')]
kargs = {'duration':0.5}
text = text.replace(' ','_')
imageio.mimsave(text+'.gif',images,**kargs)
os.remove('img1_kindgifs.png')
os.remove('img2_kindgifs.png')
print('Made your gif! (^-^)')
print(text+'.gif')
print('')

#!/usr/bin/python3

from PIL import Image
import sys
import imageio
import os

height = 10
bg = (255,117,255)
txt = (255,255,255)

y0 = 2

row0 = {'a':[txt,txt,txt],'b':[txt,txt,txt],'c':[bg,txt,txt],'d':[txt,txt,bg],'e':[txt,txt,txt],'f':[txt,txt,txt],'g':[bg,txt,txt],'h':[txt,bg,txt],'i':[txt,txt,txt],'j':[txt,txt,txt],'k':[txt,bg,txt],'l':[txt,bg,bg],'m':[txt,txt,txt],'n':[txt,txt,bg],'o':[bg,txt,txt],'p':[txt,txt,txt],'q':[bg,txt,bg],'r':[txt,txt,txt],'s':[bg,txt,txt],'t':[txt,txt,txt],'u':[txt,bg,txt],'v':[txt,bg,txt],'w':[txt,bg,txt],'x':[txt,bg,txt],'y':[txt,bg,txt],'z':[txt,txt,txt],' ':[bg,bg,bg],'*':[txt,bg,txt],'.':[bg,bg,bg],',':[bg,bg,bg],'@':[bg,txt,bg],'~':[bg,bg,bg]}

row1 = {'a':[txt,bg,txt],'b':[txt,bg,txt],'c':[txt,bg,bg],'d':[txt,bg,txt],'e':[txt,bg,bg],'f':[txt,bg,bg],'g':[txt,bg,bg],'h':[txt,bg,txt],'i':[bg,txt,bg],'j':[bg,txt,bg],'k':[txt,bg,txt],'l':[txt,bg,bg],'m':[txt,txt,txt],'n':[txt,bg,txt],'o':[txt,bg,txt],'p':[txt,bg,txt],'q':[txt,bg,txt],'r':[txt,bg,txt],'s':[txt,bg,bg],'t':[bg,txt,bg],'u':[txt,bg,txt],'v':[txt,bg,txt],'w':[txt,bg,txt],'x':[txt,bg,txt],'y':[txt,bg,txt],'z':[bg,bg,txt],' ':[bg,bg,bg],'*':[bg,txt,bg],'.':[bg,bg,bg],',':[bg,bg,bg],'@':[txt,bg,txt],'~':[bg,bg,txt]}

row2 = {'a':[txt,txt,txt],'b':[txt,txt,bg],'c':[txt,bg,bg],'d':[txt,bg,txt],'e':[txt,txt,bg],'f':[txt,txt,bg],'g':[txt,bg,bg],'h':[txt,txt,txt],'i':[bg,txt,bg],'j':[bg,txt,bg],'k':[txt,txt,bg],'l':[txt,bg,bg],'m':[txt,bg,txt],'n':[txt,bg,txt],'o':[txt,bg,txt],'p':[txt,txt,txt],'q':[txt,bg,txt],'r':[txt,txt,bg],'s':[txt,txt,txt],'t':[bg,txt,bg],'u':[txt,bg,txt],'v':[txt,bg,txt],'w':[txt,bg,txt],'x':[bg,txt,bg],'y':[txt,txt,txt],'z':[bg,txt,bg],' ':[bg,bg,bg],'*':[txt,txt,txt],'.':[bg,bg,bg],',':[bg,bg,bg],'@':[txt,bg,txt],'~':[txt,txt,txt]}

row3 = {'a':[txt,bg,txt],'b':[txt,bg,txt],'c':[txt,bg,bg],'d':[txt,bg,txt],'e':[txt,bg,bg],'f':[txt,bg,bg],'g':[txt,bg,txt],'h':[txt,bg,txt],'i':[bg,txt,bg],'j':[bg,txt,bg],'k':[txt,bg,txt],'l':[txt,bg,bg],'m':[txt,bg,txt],'n':[txt,bg,txt],'o':[txt,bg,txt],'p':[txt,bg,bg],'q':[txt,txt,bg],'r':[txt,bg,txt],'s':[bg,bg,txt],'t':[bg,txt,bg],'u':[txt,bg,txt],'v':[txt,txt,txt],'w':[txt,txt,txt],'x':[txt,bg,txt],'y':[bg,bg,txt],'z':[txt,bg,bg],' ':[bg,bg,bg],'*':[bg,txt,bg],'.':[bg,bg,bg],',':[bg,bg,txt],'@':[txt,bg,bg],'~':[txt,bg,bg]}

row4 = {'a':[txt,bg,txt],'b':[txt,txt,txt],'c':[bg,txt,txt],'d':[txt,txt,txt],'e':[txt,txt,txt],'f':[txt,bg,bg],'g':[txt,txt,txt],'h':[txt,bg,txt],'i':[txt,txt,txt],'j':[txt,txt,bg],'k':[txt,bg,txt],'l':[txt,txt,txt],'m':[txt,bg,txt],'n':[txt,bg,txt],'o':[txt,txt,bg],'p':[txt,bg,bg],'q':[bg,txt,txt],'r':[txt,bg,txt],'s':[txt,txt,bg],'t':[bg,txt,bg],'u':[bg,txt,txt],'v':[bg,txt,bg],'w':[txt,txt,txt],'x':[txt,bg,txt],'y':[txt,txt,txt],'z':[txt,txt,txt],' ':[bg,bg,bg],'*':[txt,bg,txt],'.':[bg,txt,bg],',':[bg,txt,bg],'@':[bg,txt,txt],'~':[bg,bg,bg]}

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
    pixels[i].append(bg)

for char in text:
  for i in range(3):
    pixels[0].append(bg)
    pixels[1].append(bg)
    pixels[y0].append(row0[char][i])
    pixels[y0+1].append(row1[char][i])
    pixels[y0+2].append(row2[char][i])
    pixels[y0+3].append(row3[char][i])
    pixels[y0+4].append(row4[char][i])
    pixels[7].append(bg)
    pixels[8].append(bg)
    pixels[9].append(bg)
  for i in range(10):
    pixels[i].append(bg)

for i in range(height):
  pixels.append([])
  for j in range(4):
    pixels[i].append(bg)

pixels[4][2] = txt
pixels[5][1] = txt
pixels[5][3] = txt
pixels[6][2] = txt

pixels[4][-3] = txt
pixels[5][-2] = txt
pixels[5][-4] = txt
pixels[6][-3] = txt

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
    pixels[i].append(bg)

for char in text:
  for i in range(3):
    pixels[0].append(bg)
    pixels[1].append(bg)
    pixels[2].append(bg)
    pixels[y0].append(row0[char][i])
    pixels[y0+1].append(row1[char][i])
    pixels[y0+2].append(row2[char][i])
    pixels[y0+3].append(row3[char][i])
    pixels[y0+4].append(row4[char][i])
    pixels[8].append(bg)
    pixels[9].append(bg)
  for i in range(10):
    pixels[i].append(bg)

for i in range(height):
  pixels.append([])
  for j in range(4):
    pixels[i].append(bg)

pixels[3][2] = txt
pixels[4][1] = txt
pixels[4][3] = txt
pixels[5][2] = txt

pixels[3][-3] = txt
pixels[4][-2] = txt
pixels[4][-4] = txt
pixels[5][-3] = txt

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

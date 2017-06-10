#!/usr/bin/python3

from PIL import Image
import sys
import imageio
import os

pride = False
height = 10
bg = (255,117,255)
tx = (255,255,255)

y0 = 2

row0 = {'a':[tx,tx,tx],'b':[tx,tx,tx],'c':[bg,tx,tx],'d':[tx,tx,bg],'e':[tx,tx,tx],'f':[tx,tx,tx],'g':[bg,tx,tx],'h':[tx,bg,tx],'i':[tx,tx,tx],'j':[tx,tx,tx],'k':[tx,bg,tx],'l':[tx,bg,bg],'m':[tx,tx,tx],'n':[tx,tx,bg],'o':[bg,tx,tx],'p':[tx,tx,tx],'q':[bg,tx,bg],'r':[tx,tx,tx],'s':[bg,tx,tx],'t':[tx,tx,tx],'u':[tx,bg,tx],'v':[tx,bg,tx],'w':[tx,bg,tx],'x':[tx,bg,tx],'y':[tx,bg,tx],'z':[tx,tx,tx],' ':[bg,bg,bg],'*':[tx,bg,tx],'.':[bg,bg,bg],',':[bg,bg,bg],'@':[bg,tx,bg],'~':[bg,bg,bg],'!':[bg,tx,bg],'?':[tx,tx,tx],"\'":[bg,bg,tx],'\"':[tx,bg,tx],'#':[tx,bg,tx],'_':[bg,bg,bg],'0':[tx,tx,tx],'1':[tx,tx,bg],'2':[tx,tx,tx],'3':[tx,tx,tx],'4':[tx,bg,tx],'5':[tx,tx,tx],'6':[tx,bg,bg],'7':[tx,tx,tx],'8':[tx,tx,tx],'9':[tx,tx,tx]}

row1 = {'a':[tx,bg,tx],'b':[tx,bg,tx],'c':[tx,bg,bg],'d':[tx,bg,tx],'e':[tx,bg,bg],'f':[tx,bg,bg],'g':[tx,bg,bg],'h':[tx,bg,tx],'i':[bg,tx,bg],'j':[bg,tx,bg],'k':[tx,bg,tx],'l':[tx,bg,bg],'m':[tx,tx,tx],'n':[tx,bg,tx],'o':[tx,bg,tx],'p':[tx,bg,tx],'q':[tx,bg,tx],'r':[tx,bg,tx],'s':[tx,bg,bg],'t':[bg,tx,bg],'u':[tx,bg,tx],'v':[tx,bg,tx],'w':[tx,bg,tx],'x':[tx,bg,tx],'y':[tx,bg,tx],'z':[bg,bg,tx],' ':[bg,bg,bg],'*':[bg,tx,bg],'.':[bg,bg,bg],',':[bg,bg,bg],'@':[tx,bg,tx],'~':[bg,bg,tx],'!':[bg,tx,bg],'?':[bg,bg,tx],"\'":[bg,tx,bg],'\"':[tx,bg,tx],'#':[tx,tx,tx],'_':[bg,bg,bg],'0':[tx,bg,tx],'1':[bg,tx,bg],'2':[bg,bg,tx],'3':[bg,bg,tx],'4':[tx,bg,tx],'5':[tx,bg,bg],'6':[tx,bg,bg],'7':[bg,bg,tx],'8':[tx,bg,tx],'9':[tx,bg,tx]}

row2 = {'a':[tx,tx,tx],'b':[tx,tx,bg],'c':[tx,bg,bg],'d':[tx,bg,tx],'e':[tx,tx,bg],'f':[tx,tx,bg],'g':[tx,bg,bg],'h':[tx,tx,tx],'i':[bg,tx,bg],'j':[bg,tx,bg],'k':[tx,tx,bg],'l':[tx,bg,bg],'m':[tx,bg,tx],'n':[tx,bg,tx],'o':[tx,bg,tx],'p':[tx,tx,tx],'q':[tx,bg,tx],'r':[tx,tx,bg],'s':[tx,tx,tx],'t':[bg,tx,bg],'u':[tx,bg,tx],'v':[tx,bg,tx],'w':[tx,bg,tx],'x':[bg,tx,bg],'y':[tx,tx,tx],'z':[bg,tx,bg],' ':[bg,bg,bg],'*':[tx,tx,tx],'.':[bg,bg,bg],',':[bg,bg,bg],'@':[tx,bg,tx],'~':[tx,tx,tx],'!':[bg,tx,bg],'?':[bg,tx,tx],"\'":[bg,bg,bg],'\"':[bg,bg,bg],'#':[tx,bg,tx],'_':[bg,bg,bg],'0':[tx,bg,tx],'1':[bg,tx,bg],'2':[tx,tx,tx],'3':[bg,tx,tx],'4':[tx,tx,tx],'5':[tx,tx,tx],'6':[tx,tx,tx],'7':[bg,bg,tx],'8':[tx,tx,tx],'9':[tx,tx,tx]}

row3 = {'a':[tx,bg,tx],'b':[tx,bg,tx],'c':[tx,bg,bg],'d':[tx,bg,tx],'e':[tx,bg,bg],'f':[tx,bg,bg],'g':[tx,bg,tx],'h':[tx,bg,tx],'i':[bg,tx,bg],'j':[bg,tx,bg],'k':[tx,bg,tx],'l':[tx,bg,bg],'m':[tx,bg,tx],'n':[tx,bg,tx],'o':[tx,bg,tx],'p':[tx,bg,bg],'q':[tx,tx,bg],'r':[tx,bg,tx],'s':[bg,bg,tx],'t':[bg,tx,bg],'u':[tx,bg,tx],'v':[tx,tx,tx],'w':[tx,tx,tx],'x':[tx,bg,tx],'y':[bg,bg,tx],'z':[tx,bg,bg],' ':[bg,bg,bg],'*':[bg,tx,bg],'.':[bg,bg,bg],',':[bg,bg,tx],'@':[tx,bg,bg],'~':[tx,bg,bg],'!':[bg,bg,bg],'?':[bg,bg,bg],"\'":[bg,bg,bg],'\"':[bg,bg,bg],'#':[tx,tx,tx],'_':[bg,bg,bg],'0':[tx,bg,tx],'1':[bg,tx,bg],'2':[tx,bg,bg],'3':[bg,bg,tx],'4':[bg,bg,tx],'5':[bg,bg,tx],'6':[tx,bg,tx],'7':[bg,bg,tx],'8':[tx,bg,tx],'9':[bg,bg,tx]}

row4 = {'a':[tx,bg,tx],'b':[tx,tx,tx],'c':[bg,tx,tx],'d':[tx,tx,tx],'e':[tx,tx,tx],'f':[tx,bg,bg],'g':[tx,tx,tx],'h':[tx,bg,tx],'i':[tx,tx,tx],'j':[tx,tx,bg],'k':[tx,bg,tx],'l':[tx,tx,tx],'m':[tx,bg,tx],'n':[tx,bg,tx],'o':[tx,tx,bg],'p':[tx,bg,bg],'q':[bg,tx,tx],'r':[tx,bg,tx],'s':[tx,tx,bg],'t':[bg,tx,bg],'u':[bg,tx,tx],'v':[bg,tx,bg],'w':[tx,tx,tx],'x':[tx,bg,tx],'y':[tx,tx,tx],'z':[tx,tx,tx],' ':[bg,bg,bg],'*':[tx,bg,tx],'.':[bg,tx,bg],',':[bg,tx,bg],'@':[bg,tx,tx],'~':[bg,bg,bg],'!':[bg,tx,bg],'?':[bg,tx,bg],"\'":[bg,bg,bg],'\"':[bg,bg,bg],'#':[tx,bg,tx],'_':[tx,tx,tx],'0':[tx,tx,tx],'1':[tx,tx,tx],'2':[tx,tx,tx],'3':[tx,tx,tx],'4':[bg,bg,tx],'5':[tx,tx,tx],'6':[tx,tx,tx],'7':[bg,bg,tx],'8':[tx,tx,tx],'9':[bg,bg,tx]}

if len(sys.argv) > 1:
  text = ' '.join(sys.argv[1:])
else:
  text = input('Say something! (be kind)\n > ')

text = text.lower()
print(text)
if ' -p' in text:
  pride = True
  text = text.replace(' -p','')
print(text)
  
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

pixels[4][2] = tx
pixels[5][1] = tx
pixels[5][3] = tx
pixels[6][2] = tx

pixels[4][-3] = tx
pixels[5][-2] = tx
pixels[5][-4] = tx
pixels[6][-3] = tx

if pride == True:
  for i in range(len(pixels)):
    for j in range(len(pixels[i])):
      if pixels[i][j] == tx:
        if i == 2:
          pixels[i][j] = (228,2,4)
        elif i == 3:
          pixels[i][j] = (255,139,1)
        elif i == 4:
          pixels[i][j] = (255,236,0)
        elif i == 5:
          pixels[i][j] = (0,127,39)
        elif i == 6:
          pixels[i][j] = (0,76,255)
        elif i == 7:
          pixels[i][j] = (118,6,135)
      elif pixels[i][j] == bg:
        pixels[i][j] = (255,255,255)

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

pixels[3][2] = tx
pixels[4][1] = tx
pixels[4][3] = tx
pixels[5][2] = tx

pixels[3][-3] = tx
pixels[4][-2] = tx
pixels[4][-4] = tx
pixels[5][-3] = tx

if pride == True:
  for i in range(len(pixels)):
    for j in range(len(pixels[i])):
      if pixels[i][j] == tx:
        if i == 2:
          pixels[i][j] = (228,2,4)
        elif i == 3:
          pixels[i][j] = (255,139,1)
        elif i == 4:
          pixels[i][j] = (255,236,0)
        elif i == 5:
          pixels[i][j] = (0,127,39)
        elif i == 6:
          pixels[i][j] = (0,76,255)
        elif i == 7:
          pixels[i][j] = (118,6,135)
      elif pixels[i][j] == bg:
        pixels[i][j] = (255,255,255)
          
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

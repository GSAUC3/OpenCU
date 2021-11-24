import numpy as np

from PIL import Image


def rgb2gray(image):
    '''This function converts RGB values to 
        grayscale
    I = 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue.
    '''
    red,green,blue=image[:,:,0],image[:,:,1],image[:,:,2]
    I = 0.299 * red + 0.587 * green + 0.114 *blue
    return I
    


def contrast(image):
    '''
    This is Michalson's equation for contrast
    contrast = (max(I)-min(I))/(max(I)+min(I))
    
    This function takes image array as an input'''
    maxI=minI=[]
    for i in range(len(image)):
        maxI.append(max(image[i][:]))
        minI.append(min(image[i][:]))
    a = max(maxI)
    b = min(minI)
    return (a-b)/(a+b)


def computing_histograms(image):
    H=[0]*256
    h,w=image.shape
    img=rgb2gray(image)
    for i in range(h):
        for j in range(w):
            H[img[i][j]]+=1

    return H

def clamp(image):
    ''' Clamping
     Deals with pixel values outside displayable range
     If (a > 255) a = 255;
     If (a < 0) a = 0;
     Function below will clamp (force) all values to fall
    within range [a,b]'''
    h ,w,c=image.shape
    img = rgb2gray(image)
    for i in range(h):
        for j in range(w):
            if img[i][j]>255:
                img[i][j]=255
            elif img[i][j]<0:
                img[i][j]=0
    return img

def invert_img(image):
    h ,w,c=image.shape
    img = rgb2gray(image)
    for i in range(h):
        for j in range(w):
            img[i][j]=255-img[i][j]
    return img

def img2array(image):
    '''this function required the 
        numpy module
        
        It converts any image into
        its respective numpy array
        for the ease of computation'''
    return np.asarray(Image.open(image))

def array2img(array):
    '''this function requires the 
        pillow module 
        
        this changes the numpy array to 
        image format to be displayed onto
        the screen'''
    return Image.fromarray(array)


path='E:/computer visiuon/shinchan.jpg'
im=np.asarray(Image.open(path))
im=invert_img(im)
i=Image.fromarray(im)
i.show()
#-------------------------------------------------------------------------------------------#
# Autor: Arkangel AI   
# Version: 2.0 
# Year: 2021 - Feb  
# Description: This code contain some general functions to run a ML algorithm.
#-------------------------------------------------------------------------------------------#

from skimage import io
import os 
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.measure import label, regionprops, regionprops_table
import cv2
import tensorflow as tf
import keras
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from dotenv import load_dotenv

load_dotenv()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
plot = lambda x: (plt.imshow(x), plt.show())
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

TESTING = 1 #int( os.getenv('TESTING') )
if not TESTING:
    model = load_model("./app/classifier.h5")
else:
    model = load_model("classifier.h5")

def preprocessingAfter(im):
    global TESTING
    '''
    This function applies an image normalization thorugh a GnGnR normalization an a grayscale
    Eg: 
    image = cv2.imread(path_Image) # image in range [0, 255]
    im_Normalized = preprocessingAfter(image) # image normalized in range [-1, +1]
    '''
    if not TESTING:
        try:
            im = preprocessing( im )
        except:
            return None, 1
    else:
        im = preprocessing( im )

    im = im.astype(float)
    im = im/255.
    im = resize(im, (224, 224), anti_aliasing=True) 
    im = 255*im
    im = im.astype(np.uint8)
    #im = 2*im.astype(float)/255 - 1
    return im, 0
    
def prediccion(im):
    #Classes=['']
    #Th = [0.27014542, 0.6013896, 0.00004144084, 0.70, 0.70, 0.70, 0.70, 0.6262402]
    Th = 0.60
    im2 = np.expand_dims(im, axis=0)
    out = model.predict(im2)
    print('out from model: ', out)
    predictions = out.squeeze()
    out = predictions > Th
    if TESTING:
        print("out: ", out)
        print(predictions)
        print("prediccion Done")
    return predictions 

def preprocessing(im):
    '''
    This function preprocess a numpy RGB image based to a repeated green channel [Gn, Gn, Gn]
    im = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB) # RGB image
    '''
    try:
        im2 = im.copy()
    except:
        print("This is not an RGB image")
        return 0*im2
    try:
        im_normalize = GnGnGn_Gray(im2) # preprocessing for MA detection
    except:
        return 0*im2
    #return im2, im_t
    return im2

def GnGnGn_Gray(im):
    R,G,B = [im[:,:,0], im[:,:,1], im[:,:,2]]
    return np.stack([G,G,G], axis=2)
#-------------------------------------------------------------------------------------------#
# Autor: Arkangel AI   
# Version: 2.0 
# Year: 2021 - Mar 
#-------------------------------------------------------------------------------------------#

import os
from funciones.funciones import *
from skimage import color, data, restoration
from skimage.filters import threshold_otsu, rank
from skimage.morphology import disk
import socket
import urllib
import matplotlib.pyplot as plt
import requests
from dotenv import load_dotenv


plot = lambda x: (plt.imshow(x), plt.show())
load_dotenv()
URL_APP = os.getenv('URL_RETINOPATIAS')

def get_image(uri):
    
    '''
    This function download an image given a uri, and store it in a variable
    uri = "https://raw.githubusercontent.com/DanielLopez-1805/Imagenes/master/imagen1.JPG"
    RGBimage, rowsSize, columnsSize = get_image(uri)
    '''
    
    # timeout in seconds
    timeout = 100
    socket.setdefaulttimeout(timeout)
    req = urllib.request.Request(str(uri))
    response = urllib.request.urlopen(req)
    a = response.read()
    image = np.asarray(bytearray(a), dtype=np.uint8)
    image = cv2.imdecode(image, -1) 
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
    except:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print("Get image Done")
    return image

def Detection(uri):
    global plot, TESTING #TESTING: variable inside funciones
    '''
    This function detect multiple diseases in eye fundus color images
    Eg:
    uri = "url_to_image"    
    Prediccion, error = EyeFundusDiseasesDetection(uri) 
    Output:
        Prediccion = [1,0,1,0,0,0,0,0] # One/Multiple of this:['Normal','Diabetes','Glaucoma','Catarata','Age','Hipertension','Miopia','Otros']
        error = 0
    '''
    error = 0
    if not TESTING:
        try:
            im = get_image(uri)
            im_Normalized, error = preprocessingAfter(im)
            out = prediccion(im_Normalized).reshape(-1)
            out_th = int(out > 0.60)
            #Pred = EnsuringNormalDiabetesPrediction(out, uri) # BE SURE THAT NORMAL IS NORMAL
            return (out, out_th, error)
        except:
            return ([], error)
    else:
        im = get_image(uri)
        im_Normalized, error = preprocessingAfter(im)
        out = prediccion(im_Normalized).reshape(-1)
        out_th = int(out > 0.60)
        #Pred = EnsuringNormalDiabetesPrediction(out, uri) # BE SURE THAT NORMAL IS NORMAL
        print("Pred: ", out)
        return (out, out_th, error)

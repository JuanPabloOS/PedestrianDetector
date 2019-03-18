
from imutils.object_detection import non_max_suppression
import numpy as np 
import cv2 
import imutils
import os

 
"""
https://carlosjuliopardoblog.wordpress.com/2018/06/28/deteccion-de-peatones-con-python-y-opencv-hog-svm/
"""
def passImg(imagen):  
    try:
        image = cv2.imread(imagen)
        cv2.imshow("Imagen original",image)
        #Escalar la imagen        
        scale = 1.0
        w = int(image.shape[1] / scale)
        image = imutils.resize(image, width=w)               
        
        #Inicializar el descriptor de histogramas
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        #copiar la nueva imagen
        orig = image.copy()        
        # buscar personas en la imagen
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                                padding=(8, 8), scale=1.05)
               
        
        # appaplicar non-maxima suppression a los cuadros limitadores con overlaping      
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        
        # dibujar los cuadros finales
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
                        
        cv2.imshow("Resultado", image)
        return True        
    except AttributeError:
        return False        













import sys
import cv2
import numpy as np
from os import listdir,mkdir,path
from os.path import isfile, join
import shutil



#Change brightness function (g = a*f + b), g is new brightness
def change_brightness(img, alpha, beta):
    img_new = np.asarray(alpha*img + beta, dtype=int)   # cast pixel values to int
    img_new[img_new>255] = 255
    img_new[img_new<0] = 0
    return img_new


#Mass update brightness in folder
def mass_change_brightness(folder,alpha,beta):
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    new_folder = f'alpha = {alpha}'
    if path.exists(new_folder):
        shutil.rmtree(new_folder)
    mkdir(new_folder)
    for i in onlyfiles:
        img = cv2.imread(f'{folder}/{i}')
        img_new = change_brightness(img, alpha, beta)
        cv2.imwrite(f'{new_folder}/{i}', img_new)


#Fix beta = 10 and alpha change from 1 to 0.1 step = 0.1
alpha = [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
beta = 10

for a in alpha:
    mass_change_brightness('Picture Data',a,beta)
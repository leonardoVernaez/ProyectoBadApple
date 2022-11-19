import cv2 as cv
import numpy as np
import pandas as pd

class asciiConverter():
    
    
    def __init__(self):
        
        pass
    def binarizarImagen(self,imagen):
        """
        Convierte un array de entrada, que contiene los valores RGB de la imagen en binario
        
        Args:
            imagen ([np.array]): [array RGB con la información de la imagen]

        Returns:
            [np.array]: [array con valores binarios respecto al color]
        """
        img = imagen.copy()
        #obtiene el tamaño original de la imagen para emplearlo más tarde
        shaped= img.shape
        
        #crea una lista bidimensional con la información de cada pixel
        imageReshaped = img.reshape(1,shaped[0]*shaped[1],3)
        
        #crea un dataframe con la información de cada pixel en una lista con los valores de cada pixel ordenados
        df = pd.DataFrame(imageReshaped[0])
        
        #le aplico la función cut al dataframe para hacer que los valores RGB sean binarios para asignarle color a cada carácter de forma posterior
        df = (df.apply(pd.cut,bins=2, labels= [0,1]))
        
        #Le asigno los valores binarios al array reescalado del que se extrajo el dataframe
        imageReshaped[0] = df.values
        
        #creo la variable imagen final que contiene la imagen reescalada con los valores iniciales
        imagenFinal= imageReshaped.reshape(shaped[0],shaped[1],3)
        
        return imagenFinal
        
    def ImageToAscii(self,imagen,dimensiones=(20,20),color=True):
        
        
        
        
        return imagen
        
        
        
        
    '''
    negro   : 30
    rojo    : 31
    verde   : 32
    amarillo: 33
    azul    : 34
    morado  : 35
    turquesa: 36
    blanco  : 37
    
    reiniciar estilo: 39
    '''
        
    

if __name__ == '__main__':
    
    a =asciiConverter()
    
    img = cv.imread('test/guaro.png')

    c= (a.binarizarImagen(img))
    
    cv.imshow('c',c*255)
    cv.imshow('img',img)
    cv.waitKey(0)
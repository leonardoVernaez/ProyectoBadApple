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
        #mensaje de error para el caso de que no se introduzca un array de numpy
        if type(imagen) != type(np.array([])):
            raise Exception('Esto no es un array de numpy')
        
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
        
    def ImageToAscii(self,imagen,ancho=50,color=True):
        """ImageToAscii convierte la imagen en condigo ascii

        Args:
            imagen ([numpy.array]): [array que contiene la información de la imagen]
            ancho (int, optional): [ancho que va a tener la imagen en código ascii]. Defaults to 50.
            color (bool, optional): [True para que se imprima con colores ascii, False para que sea solo en escala de grises]. Defaults to True.

        Returns:
            [str]: [string con la imagen en ascii art]
        """
        #copia la imagen para no alterar los valores de entrada
        img = imagen.copy()

        #guarda las dimensiones de la imagen para calcular otro tamaño proporcional a partir de un ancho y un alto        
        shape = img.shape
        #calcula las nuevas proporciones de la imagen : (largo_original*((ancho*100)/ancho_original))/100
        nuevo_ancho = ancho
        porcentaje = (ancho*100)/shape[1]
        nuevo_alto = int((shape[0]*porcentaje)/100)
        
        #realiza el reescalado de la imagen con las proporciones calculadas
        img_resized = cv.resize(img,(nuevo_ancho,nuevo_alto))

        
        return img_resized
        
        
        
        
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
        
    


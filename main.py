import cv2 as cv
import numpy as np
import pandas as pd

class asciiConverter():
    
    
    def __init__(self):
        
        #lista que contiene los valores de los colores en ascii ordenada para tener un fácil acceso
        self.colors = [[['\033[0;30m','\033[0;34m'],['\033[0;32m','\033[0;36m']],
                       [['\033[0;31m','\033[0;35m'],['\033[0;33m','\033[0;37m']]]
        #Pone por defecto la tipografía que se desea utilizar
        self.reset = '\033[0;39m'
        
        
    
    
    
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
        
        
        
        #copia la imagen 
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
        
    def PhotoToColor(self,imagen):
        """PhotToColor transforma la imagen con valores RGB binarios en los caracteres ascii que determinaran el color de la imagen final

        Args:
            imagen ([numpy.array]): [un array de numpy que contiene la imagen, nota: asegurarse que primero la imagen haya pasado primero por binarizarImagen]

        Returns:
            [list]: [lista con los caracteres de determinaran el color]
        """
        
        #copia la imagen para evitar editar la imagen original
        img = imagen.copy()
        #pasa la imagen de BGR a RGB
        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        #esta lista contendrá la salida de la función 
        result = []
        
        #bucles anidados que van a recorrer la imagen
        
        for fila in img:
            #lista de los resultados de cada columna
            preResult = []
            
            for columna in fila:
                #saca los valores RGB de la imagen
          
                colorRGB = columna
                
                #añade el color de cada pixel a su correspondiente columna
                preResult.append(self.colors[colorRGB[0]][colorRGB[1]][colorRGB[2]])
            #añade la fila a la lista
            result.append(preResult)
      
        return result
        
        
    
    
    def ImageToAscii(self,imagen,ancho=50,caracteres = ' .:(!%#@Ñ',color=True):
        """ImageToAscii convierte la imagen en condigo ascii

        Args:
            imagen ([numpy.array]): [array que contiene la información de la imagen]
            ancho (int, optional): [ancho que va a tener la imagen en código ascii]. Defaults to 50.
            color (bool, optional): [True para que se imprima con colores ascii, False para que sea solo en escala de grises]. Defaults to True.

        Returns:
            [str]: [string con la imagen en ascii art]
        """
        #copia la imagen para no alterar los valores de entrada
        img = imagen

        #guarda las dimensiones de la imagen para calcular otro tamaño proporcional a partir de un ancho y un alto        
        shape = img.shape
        #calcula las nuevas proporciones de la imagen : (largo_original*((ancho*100)/ancho_original))/100
        nuevo_ancho = ancho
        porcentaje = (ancho*100)/shape[1]
        nuevo_alto = int(((shape[0]*porcentaje)/100) -1)
        
        #realiza el reescalado de la imagen con las proporciones calculadas
        img_resized = cv.resize(img,(nuevo_ancho,nuevo_alto))

        #realiza la conversion a escala de grises de la imagen
        img_grayScale= cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY) 
        #en caso de que se desee generar una imagen con color se genera la lista de colores para cada pixel
        if color:
            
            colores =self.PhotoToColor(self.binarizarImagen(img_resized))
        
        #array de números que contiene la 
        chars = (np.round((img_grayScale/(255/(len(caracteres)-1)))))
      
        #string que contendrá el resultado
        result = ''
        
        #bucle concatenado que lee y crea el string final
        filax = 0
        for fila in chars:
            columnax = 0
            for columna in fila:
                
                #le añade color en caso de que se desee
                if color:
                  
                    result = result + colores[filax][columnax]
                    
                #esto añade el carácter correspondiente a cada píxel   
              
                result = result + caracteres[int(chars[filax][columnax])] + self.reset
                
                columnax += 1
            filax += 1    
            result += '\n'
       
        
        return result
        
        
        
        
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
        
    


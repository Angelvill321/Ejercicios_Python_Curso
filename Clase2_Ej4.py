#EJERCICIO 2

# Desarrolle una clase PUNTO, que representa una punto en el plano
# La clase contiene dos atributos, X, Y, que son los números que representa ese punto en el plano
# Se debe definir un constructor __init__ que permita crear un número pasándole las dos coordenadas.
# La clase debe incorportar un método __str__ que permita mostrar un punto como (X,Y)
# La clase debe incorporar un método getCuadrante que indique en qué cuadrante se encuentra el punto, teniendo en cuenta el grafico adjunto.
# La clase debe incorporar un método getDistanciaOrigen que indique la distancia del punto al origen (0,0) según la fórmula indicada.

class Punto:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__ (self):
        return f'Las coordenadas de dichos puntos son: ({self.x};{self.y}).'
    
    def getCuadrante(self):
        if self.x == 0.0 and self.y == 0.00:      
            print('Las coordenadas se encuentran en el origen')
        elif self.x == 0 and self.y != 0.00:
            print('Las coordenadas se encuentran en el eje de las abscisas (X)')
        elif self.y == 0 and self.x != 0.00:
            print('Las coordenadas se encuentran en el eje de las ordenadas (Y)')
        elif self.x > 0.0:
            if self.y > 0.0:
                print('Las coordenadas se encuentran en el primer cuadrante')
            else:
                print('Las coordenadas se encuentran en el cuarto cuadrante')
        elif self.x < 0.0:
            if self.y > 0.0:
                print('Las coordenadas se encuentran en el segundo cuadrante')
            else:
                print('Las coordenadas se encuentran en el tercer cuadrante')

    def getDistanciaOrigen(self):
        operacion = (self.x**2 + self.y**2)**0.5
        return round(operacion, 2)

def main():
     print('Ingrese las siguientes coordenadas: ')
     x = int(input('Para el eje X: '))
     y = int(input('Para el eje Y: '))
     coordenadas = Punto(x,y)
     print(coordenadas)
     coordenadas.getCuadrante()
     print(f'La distancia del par de coordenadas ({x};{y}) respecto del origen es {coordenadas.getDistanciaOrigen()}')


main()
    
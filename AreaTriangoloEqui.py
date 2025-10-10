lato=float(input("inserisci il lato:"))
import math
perimetro=lato*3
finto_h=(lato*lato)-((lato/2)*(lato/2))
radice = math.sqrt(finto_h)
area=(radice*lato)/2
print(area)
print(perimetro)

# Laura Yolanda Vega Hernandez  15 de agosto del 2023


# Duplicados. Dada una lista de números enteros, retorna True
# si al menos un valor aparece dos veces, y Falso si todos
# los elementos son distintos.

lista1 = [2, 5, 7, 9, 6, 4, 5, 7, 8, 9]


def duplicados(lista1):
   return len(lista1) != len(set(lista1))


print(duplicados(lista1))



# Suma de dos números. Dado una lista de números entero
# y un valor entero (target), retorna el índice de los dos
# números que sumados sean igual al target. Debe asumir que
# existe siempre una única solución, y que los elementos no se
# pueden usar dos veces. Debes retorna una tupla con los índices.

def busquedaSuma(nums, target):
    num_indices = {} 
    
    for i, num in enumerate(nums):
        resultado = target - num
        
        if resultado in num_indices:
            return (num_indices[resultado], i)
        
        num_indices[num] = i
    
    return None


nums = [2, 7, 11, 15]
target = 9
print(busquedaSuma(nums, target))  # Salida: (0, 1)


# Encriptar. Diseñe una función encripta(s, clave), que
# reciba un string s con un mensaje y un string con una clave de
# codificación, y retorne el mensaje codificado según la clave leída.
# Los signos de puntuación y dígitos que aparecen en el mensaje deben
# conservarse sin cambios.
abc = "abcdefghijklmnopqrstuvwxyz"
clave = "ixmrklstnuzbowfaqejdcpvhyg"
palabra = "cafe"


def encripta(s, clave):
    
    diccionario_clave = {abc[i]: clave[i] for i in range(26)}
    encriptado = []

    for char in s:
        if char in diccionario_clave:
            encriptado.append(diccionario_clave[char])
        else:
            encriptado.append(char)
    
    return "".join(encriptado)


print(encripta(palabra, clave))

#Desencriptar. Diseña una función desencripta(s, clave) que 
#realice la función inversa a la función anterior, es decir, 
#reciba un string s y una clave y realice la desencriptación 
#del mensaje en el string devolviendo la cadena desencriptada. 
abc2 = "abcdefghijklmnopqrstuvwxyz"
clave2 = "ixmrklstnuzbowfaqejdcpvhyg"
palabra2 = "milk"

def desencripta(s, clave):
    
    diccionario_clave2 = {clave[i]: abc2[i] for i in range(26)}
    desencriptado = []

    for char in s:
        if char in diccionario_clave2:
            desencriptado.append(diccionario_clave2[char])
        else:
            desencriptado.append(char)
    
    return "".join(desencriptado)


print(desencripta(palabra2, clave))

# Gestión de Pensionistas. Crear una clase llamada GrupoPensionistas la cual tendrá
#  un único atributo la cual es una lista o diccionario de objetos de tipo Pensionista 
#  (Elija a conveniencia si una lista o diccionario). Cada objeto de Pensionista tiene 
#  los siguientes atributos: identificador del pensionista (string), un entero que indica
#  la edad y una serie de gastos mensuales que se guardan (lista de enteros). El número 
#  de gastos mensuales puede variar entre pensionistas. Por ejemplo, el pensionista con 
#  identificador '1111A' se llama 'Carlos' tiene 68 años y tiene 3 gastos mensuales de 
#  640, 589 y 573. 
# La clase GrupoPensionistas debe tener los siguientes métodos:
# mediaGastos(identificador) , dado el identificador o indice de un pensionista, 
# devuelva el promedio de los gastos. 
# mediaEdad(), dado todos los pensionados, devuelve el promedio de las edades. 
# edadesExtremas(), dado todos los pensionados, devuelva al pensionado con menor 
# y mayor edad en una tupla.
# sumaPromedio(), dado todos los pensionados, devuelva la suma del promedio de 
# los gastos de todos los pensionistas de la lista. 
# mediaMaxima(), dado todos los pensionistas, retorne el mayor promedio de los 
# gastos entre todos los pensionistas de la lista, su nombre e identificador.
# gastoPromedio(lst), dado todos los pensionistas, devuelve una lista con el 
# gasto promedio de cada persona. La lista resultante debe estar ordenada de forma ascendente.

class Pensionista:
    def __init__(self, iden, edad, gastos_mensuales):
        self.iden = iden
        self.edad = edad
        self.gastos_mensuales = gastos_mensuales

class GrupoPensionistas:
    def __init__(self):
        self.pensionistas = []
    
    def mediaGastos(self, iden):
        pensionista = next((p for p in self.pensionistas if p.iden == iden), None)
        return sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales) if pensionista else None
    
    def mediaEdad(self):
        return sum(p.edad for p in self.pensionistas) / len(self.pensionistas)
    
    def edadesExtremas(self):
        return min(self.pensionistas, key=lambda p: p.edad), max(self.pensionistas, key=lambda p: p.edad)
    
    def sumaPromedio(self):
        return sum(sum(p.gastos_mensuales) / len(p.gastos_mensuales) for p in self.pensionistas)
    
    def mediaMaxima(self):
        pensionista_max_media = max(self.pensionistas, key=lambda p: sum(p.gastos_mensuales) / len(p.gastos_mensuales))
        return pensionista_max_media.iden, pensionista_max_media.edad, sum(pensionista_max_media.gastos_mensuales) / len(pensionista_max_media.gastos_mensuales)

    def gastoPromedio(self):
        return sorted([(p.iden, sum(p.gastos_mensuales) / len(p.gastos_mensuales)) for p in self.pensionistas], key=lambda x: x[1])

grupo = GrupoPensionistas()
grupo.pensionistas.append(Pensionista("1111A", 68, [640, 589, 573]))
grupo.pensionistas.append(Pensionista("2222B", 72, [800, 720, 650]))
grupo.pensionistas.append(Pensionista("3333C", 65, [500, 550, 600]))

print(grupo.mediaGastos("1111A"))
print(grupo.mediaGastos("2222B"))
print(grupo.mediaEdad())
print(grupo.edadesExtremas())



# Estadística Básica. Cree una clase llamada Estadística que contiene 
# como atributo una lista de números naturales la cual puede contener 
# repetidos. Debe contener los siguientes métodos:
# Frecuencia de Números. Dada la lista, devuelve un diccionario con el 
# número de veces que aparece cada número en la lista.
# Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido).
#  Puedes usar la función anterior como ayuda.
# Histograma. Dada la lista, muestra el histograma de la lista. 
# Puedes reusar los métodos anteriores. 

numeros = [1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1]

class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros
    
    def frecuenciaNumeros(self):
        frecuencias = {}
        for num in self.numeros:
            if num in frecuencias:
                frecuencias[num] += 1
            else:
                frecuencias[num] = 1
        return frecuencias
    
    def moda(self):
        frecuencias = self.frecuenciaNumeros()
        max_frecuencia = max(frecuencias.values())
        moda = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
        return moda
    
    def histograma(self):
        frecuencias = self.frecuenciaNumeros()
        for num, freq in frecuencias.items():
            print(f"{num} {'*' * freq}")

estadistica = Estadistica(numeros)
estadistica.histograma()
 




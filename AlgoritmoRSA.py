import random

class RSA:
    def __init__(self):
        # Inicialización de variables
        numeroPrimo1 = 0
        numeroPrimo2 = 0
        
        # Bucle para obtener dos números primos diferentes
        while numeroPrimo1 == 0 or numeroPrimo2 == 0 or numeroPrimo1 == numeroPrimo2:
            while numeroPrimo1 == 0:
                rango1, rango2 = self.pedirRango()  # Pedir rango al usuario
                numeroPrimo1 = self.buscarNumeroPrimo(rango1, rango2)  # Buscar número primo en el rango
                if numeroPrimo1 == 0:
                    print("No se encontró un número primo en el rango ingresado")
                else:
                    print("El número primo encontrado es:", numeroPrimo1)
            
            while numeroPrimo2 == 0:
                rango1, rango2 = self.pedirRango()  # Pedir rango al usuario
                numeroPrimo2 = self.buscarNumeroPrimo(rango1, rango2)  # Buscar número primo en el rango
                if numeroPrimo2 == 0:
                    print("No se encontró un número primo en el rango ingresado")
                else:
                    print("El número primo encontrado es:", numeroPrimo2)
            
            if numeroPrimo1 == numeroPrimo2:
                print("Los números primos deben ser diferentes")
                numeroPrimo1 = 0
                numeroPrimo2 = 0
        
        self.establecerClaves(numeroPrimo1, numeroPrimo2)  # Establecer claves pública y privada
        print("Clave pública:", self.e)
        print("Clave privada:", self.d)

    def esPrimo(self, numero):
        """Verifica si un número es primo."""
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
    
    def buscarNumeroPrimo(self, rango1, rango2):
        """Busca un número primo en el rango especificado."""
        numeroPrimo = rango1
        while not self.esPrimo(numeroPrimo) and numeroPrimo < rango2:
            numeroPrimo += 1
        if not self.esPrimo(numeroPrimo):
            return 0
        return numeroPrimo
    
    def mcd(self, a, b):
        """Calcula el máximo común divisor (MCD) de dos números."""
        resto = 0
        while b > 0:
            resto = b
            b = a % b
            a = resto
        return a
    
    def establecerClaves(self, p, q):
        """Establece las claves pública y privada utilizando los números primos p y q."""
        self.n = p * q  # Producto de p y q
        self.z = (p - 1) * (q - 1)  # Valor de Euler
        self.e = self.generarE()  # Clave pública
        self.d = self.generarD()  # Clave privada

    def generarE(self):
        """Genera la clave pública 'e'."""
        e = 2
        while e < self.z:
            if self.mcd(e, self.z) == 1:
                return e
            e += 1

    def generarD(self):
        """Genera la clave privada 'd'."""
        d = 2
        while d < self.z:
            if (d * self.e) % self.z == 1:
                return d
            d += 1

    def pedirRango(self):
        """Solicita al usuario que ingrese el rango para buscar números primos."""
        rango1 = 0
        rango2 = 0
        while rango1 == 0 or rango1 == 1 or rango2 == 0 or rango2 == 1 or rango1 == 2 or rango2 == 2:
            rango1 = int(input("Ingrese el número para comenzar a buscar un número primo: "))
            rango2 = int(input("Ingrese el número para terminar de buscar un número primo: "))
            if rango1 == 0 or rango2 == 0 or rango1 == 1 or rango2 == 1 or rango1 == 2 or rango2 == 2:
                print("El rango debe ser mayor a 2")
            else:
                print("El rango ingresado es válido")
        return rango1, rango2
    
    def encriptar(self, nombreArchivo):
        """Encripta el contenido de un archivo y lo guarda en otro archivo."""
        simbolos = ("!@#$%^&*()_+):;'?/.>,<\|=-")	
        with open(nombreArchivo, "r") as archivo:
            texto = archivo.read()
        
        with open("ArchivoEncriptado.txt", "w") as archivo:
            for caracter in texto:
                encript = random.randrange(1, len(simbolos))
                simbolo = simbolos[encript]
                encriptado = pow(ord(caracter), self.e, self.n)
                archivo.write(str(encriptado) + simbolo)
        
        print("El archivo se ha encriptado correctamente")
        print("El archivo encriptado se llama: ArchivoEncriptado.txt")

    def desencriptar(self, nombreArchivo):
        """Desencripta el contenido de un archivo encriptado y lo guarda en otro archivo."""
        simbolos = ("!@#$%^&*()_+):;'?/.>,<\|=-")
        with open(nombreArchivo, "r") as archivo:
            texto_encriptado = archivo.read()
            
            numeros_encriptados = []
            numero_actual = ""
            for caracter in texto_encriptado:
                if caracter in simbolos:
                    if numero_actual:
                        numeros_encriptados.append(numero_actual)
                        numero_actual = ""
                else:
                    numero_actual += caracter
            
            mensaje_desencriptado = ""
            for numero in numeros_encriptados:
                desencriptado = pow(int(numero), self.d, self.n)
                mensaje_desencriptado += chr(desencriptado)
            
            with open("ArchivoDesencriptado.txt", "w") as archivo:
                archivo.write(mensaje_desencriptado)
        
        print("El archivo se ha desencriptado correctamente")
        print("El archivo desencriptado se llama: ArchivoDesencriptado.txt")



rsa=RSA()
rsa.encriptar("Archivo.txt")
rsa.desencriptar("ArchivoEncriptado.txt")
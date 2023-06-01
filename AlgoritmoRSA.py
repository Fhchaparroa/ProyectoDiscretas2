class RSA:
    def __init__(self):
        numeroPrimo1=0
        numeroPrimo2=0
        numeroPrimo1 = self.buscarNumeroPrimo(10000, 20000)
        numeroPrimo2 = self.buscarNumeroPrimo(50000, 80000)
        while numeroPrimo1==0 or numeroPrimo2==0 or numeroPrimo1==numeroPrimo2:
            while numeroPrimo1==0:
                rango1, rango2=self.pedirRango()
                numeroPrimo1=self.buscarNumeroPrimo(rango1, rango2)
                if numeroPrimo1==0:
                    print("No se encontró un número primo en el rango ingresado")
                else:
                    print("El número primo encontrado es: ", numeroPrimo1)
            while numeroPrimo2==0:
                rango1, rango2=self.pedirRango()
                numeroPrimo2=self.buscarNumeroPrimo(rango1, rango2)
                if numeroPrimo2==0:
                    print("No se encontró un número primo en el rango ingresado")
                else:
                    print("El número primo encontrado es: ", numeroPrimo2)
            if numeroPrimo1==numeroPrimo2:
                print("Los números primos deben ser diferentes")
                numeroPrimo1=0
                numeroPrimo2=0
        self.establecerClaves(numeroPrimo1, numeroPrimo2)
        print("Clave publica: ",self.e)
        print("Clave privada: ",self.d)

    def esPrimo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True
    
    def buscarNumeroPrimo(self, rango1, rango2):
        numeroPrimo = rango1
        while not self.esPrimo(numeroPrimo) and numeroPrimo<rango2:
            numeroPrimo = numeroPrimo + 1
        if self.esPrimo(numeroPrimo)==False:
            return 0
        return numeroPrimo
    
    def mcd(self, a, b):
        resto = 0
        while b > 0:
            resto = b
            b = a % b
            a = resto
        return a
    
    def establecerClaves(self, p, q):
        self.n = p * q
        self.z = (p - 1) * (q - 1)
        self.e = self.generarE()
        self.d = self.generarD()

    def generarE(self):
        e = 2
        while e < self.z:
            if self.mcd(e, self.z) == 1:
                return e
            e += 1

    def generarD(self):
        d = 2
        while d < self.z:
            if (d * self.e) % self.z == 1:
                return d
            d += 1

    def pedirRango(self):
        rango1=0
        rango2=0
        while rango1==0 or rango1==1 or rango2==0  or rango2==1:
            rango1=int(input("Ingrese el numero a comenzar a buscar un número primo: "))
            rango2=int(input("Ingrese el numero a terminar de buscar un número primo: "))
            if rango1==0 or rango2==0 or rango1==1 or rango2==1:
                print("El rango debe comenzar o terminar en un numero mayor a 1")
            else:
                print("El rango ingresado es válido")
        return rango1, rango2
    
    def encriptar(self, nombreArchivo):
        with open(nombreArchivo, "rb") as archivo:
            bytesTexto = archivo.read()
        enteroTexto = int.from_bytes(bytesTexto, 'big')
        if enteroTexto >= self.n:
            print("El archivo es demasiado grande para ser encriptado con las claves actuales.")
            return
        encriptado = pow(enteroTexto, self.e, self.n)
        bytesEncriptado = encriptado.to_bytes((encriptado.bit_length() + 7) // 8, 'big')
        with open("ArchivoEncriptado.txt", "wb") as archivo:
            archivo.write(bytesEncriptado)
        print("El archivo se ha encriptado correctamente")
        print("El archivo encriptado se llama: ArchivoEncriptado.txt")

    def desencriptar(self, nombreArchivo):
        with open(nombreArchivo, "rb") as archivo:
            bytesEncriptado = archivo.read()
        enteroEncriptado = int.from_bytes(bytesEncriptado, 'big')
        desencriptado = pow(enteroEncriptado, self.d, self.n)
        bytesDesencriptado = desencriptado.to_bytes((desencriptado.bit_length() + 7) // 8, 'big')
        with open("ArchivoDesencriptado.txt", "wb") as archivo:
            archivo.write(bytesDesencriptado)
        print("El archivo se ha desencriptado correctamente")


rsa=RSA()
rsa.encriptar("Archivo.txt")
rsa.desencriptar("ArchivoEncriptado.txt")
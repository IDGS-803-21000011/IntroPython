class OperasBas:
    #Declaración de propiedades de clase
    num1 = 0
    num2 = 0
    res = 0

    #Declaración de constructor
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    #Declaración de métodos de clase
    def suma(self):
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))

def main():
    obj = OperasBas(3, 4)
    obj.suma()

if __name__ == "__main__":
    main()
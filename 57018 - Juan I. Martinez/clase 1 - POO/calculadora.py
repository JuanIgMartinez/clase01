#Juan I. Martinez, Legajo 57018

class Calculadora():

    def __init__(self):
        self.nro1 = 0
        self.nro2 = 0
        self.resultado = 0
        self.listaInputs = []

    def ingresar(self, input_usuario):
        try:

            caracter = int(input_usuario)
            self.nro1 = self.nro1 * 10 + caracter

        except ValueError:

            self.listaInputs.append(input_usuario)

            if input_usuario == "+":
                self.nro2 = self.nro1 + self.nro2
                self.nro1 = 0

            elif input_usuario == "-":
                self.nro2 = self.nro1 
                self.nro1 = 0

            elif input_usuario == "*":
                self.nro2 = self.nro1 
                self.nro1 = 0

            elif input_usuario == "%":
                self.nro2 = self.nro1 
                self.nro1 = 0

            elif input_usuario == "=":
                if self.listaInputs[-2] == "+":
                    self.resultado = self.nro1 + self.nro2
                elif self.listaInputs[-2] == "-":
                    self.resultado = self.nro2 - self.nro1
                elif self.listaInputs[-2] == "*":
                    self.resultado = self.nro1 * self.nro2
                elif self.listaInputs[-2] == "%":
                    self.resultado = self.nro2 / self.nro1


'''
De esa forma anda las operaciones distintas a la suma solo si pasamos 2 argumentos, en el caso de ser mas habria que checkear primero si nro2 es igual a 0
y de ahi hacer la logica ya implementada si es 0, sino, habria que agregar un condicional que haga la operacion previa hasta pedir el resultado final

'''


'''
c1 = Calculadora()
c1.ingresar('6')
c1.ingresar('+')
c1.ingresar('3')
c1.ingresar('-')
c1.ingresar('2')
c1.ingresar('=')

print(c1.nro1)
print(c1.nro2)
print(c1.resultado)
'''
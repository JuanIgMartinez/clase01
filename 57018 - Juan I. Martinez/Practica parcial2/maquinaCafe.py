class Maquina_de_cafe(object):
    def __init__ (self, agua, cafe):
        self.agua = agua
        self.cafe = cafe
        self.cantidad_de_monedas = 0
        self.coin = False
        self.cup = False
        self.milk = None
        self.azucar = 0

 
#    def check_completo(self):
#        if self.coin == True:
#            print("Moneda OK")
#        if self.cup == True:
#            print("Vaso OK")
#        print("Tiene leche:", self.milk)
#        print("Cantidad de azucar en gramos:", self.sugar)

    def check_moneda(self, moneda):
        if int(moneda) == 1:
            self.coin = True
            return "moneda ok"
        else:
            print("Ingrese una moneda valida")
    
    def check_vaso(self, vaso):
        if vaso == "si":
            self.cup = True
            return "vaso ok"
        else:
            print("Ingrese un vaso")
    
    def check_leche(self, leche):
        if leche == "si":
            self.milk = "Si"
            return "con leche"
        elif leche == "no":
            self.milk = "No"
        else:
            print("Input incorrecto ingrese si/no")
    
    def check_azucar(self, azucar):
        if int(azucar) >= 0 and int(azucar) <= 5:
            self.sugar = azucar
            return 3
        else:
            print("El valor de azucar tiene que ser entre 0 y 5g")
    

        
'''

test = Maquina_de_cafe(1,1)
test.check_moneda(1)
test.check_vaso("si")
test.check_leche("si")
test.check_azucar(3)
test.check_completo()
'''
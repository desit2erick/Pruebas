import re

tiposPanalValidos = ['V', 'Z', 'C', 'H', 'EA', 'EL']

class CalculadoraPanal:
    def __init__(self, referencia: str):
        try:
            self.referencia = referencia
            self.tipo = ''.join(re.findall(r'[a-zA-Z]+', self.referencia))
            self.filas = re.search(r'[0-9]+', self.referencia).group()
            self.dimensiones = re.findall(r'[0-9]+', self.referencia)[1]
            self.repartirDimension()
        except Exception as error:
            raise Exception('Referencia invalida - "{}"'.format(referencia))
        self.validarDatos()

    def repartirDimension(self):
        digits = len(self.dimensiones)
        esPar = digits % 2 == 0

        if esPar:
            self.alto = self.dimensiones[:digits//2] 
            self.ancho = self.dimensiones[digits//2:]
        else:
            A1, B1 = int(self.dimensiones[:digits//2]), \
                int(self.dimensiones[digits//2:])
            diff1 = abs(A1-B1)
            A2, B2 = int(self.dimensiones[:digits//2+1]), \
                int(self.dimensiones[digits//2+1:])
            diff2 = abs(A2-B2)

            self.alto, self.ancho = (A1, B1) if diff1 < diff2 else (A2, B2)

    def validarDatos(self):
        if self.tipo not in tiposPanalValidos:
            raise Exception('Tipo de panal incorrecto - "{}"'.format(self.referencia))
        if not self.filas.isnumeric():
            raise Exception('Filas de panal incorrecto - "{}"'.format(self.referencia))
    

    def calcularCostoTotal(self, **kwargs):
        self.costo_total = 0
        for value in kwargs.values():
            if isinstance(value, (int, float)):
                self.costo_total += value
            elif isinstance(value, str):
                self.costo_total += str(value)
        return self.costo_total            


if __name__ == '__main__':
    
    try:
        calculadora = CalculadoraPanal('V2-4054')
        CT = calculadora.calcularCostoTotal(CostoFins=4, CostoPlatinas=6, CostoTubos=5, CostoEstano=6)
        print(CT)
    except Exception as error:
        print(error)

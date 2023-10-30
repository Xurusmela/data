class data(object):
    def __int__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def setDia(self, dia):
        self.dia = dia
    def getDia(self):
        return self.dia
    def setMes(self, mes):
        self.mes = mes
    def getMes(self):
        return self.mes
    def setAno(self, ano):
        self.ano = ano
    def getAno(self):
        return self.ano

    def __str__(self):
        return '\n\n Dia' + str(self.dia), '\nMes' + str(self.mes), '\nAno' + str(self.ano)
class Validador_CPF:

    def __init__(self, cpf):
        self.cpf = str(cpf)

        tamanho_cpf = 11
        if len(self.cpf) ==  tamanho_cpf:
            pass
        else:
            exit()

    def vericador(self):
        lista1 = []
        lista2 = []
        num_cpf = self.cpf[0:9]

        for i in range(1, 10):
            validador = int(num_cpf[i-1])
            cal = validador*i
            lista1.append(cal)

        soma = sum(lista1)
        resto = soma%11
        num_cpf2 = num_cpf + str(resto)

        for x in range(0, 10):
            validador2 = int(num_cpf2[x])
            cal2 = validador2*x
            
            lista2.append(cal2)

        soma2 = sum(lista2)
        resto2 = soma2%11

        resto_total = str(resto)+str(resto2)

        cpf_verificador = self.cpf[9:11]
        if resto_total == cpf_verificador:
            return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{resto_total}"
        else:
            exit()


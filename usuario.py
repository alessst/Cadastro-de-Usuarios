from validar_cpf import Validador_CPF


class Usuario:

    def __init__(self, nome, idade, endereco, cpf, email):
        
        self.nome       = nome
        self.idade      = idade
        self.cpf        = cpf
        self.endereco   = endereco
        self.email      = email
    
    
        
    def dados_usuario(self):
        
        self.cpf_valido = Validador_CPF(self.cpf)
        usuario = [self.nome, self.idade, self.endereco, self.cpf_valido.vericador(), self.email]
        return usuario      

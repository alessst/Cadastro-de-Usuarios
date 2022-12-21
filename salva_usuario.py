from usuario import Usuario
import pandas as pd


class SalvaDados:

    def __init__(self, nome, idade, endereco, cpf, email):

        self.user = Usuario(nome, idade, endereco, cpf, email)
    
    def verificar_cadastro(self, dado, lista):    
    
        for valor in lista:
            if dado == valor: 
                print(f"CPF ({dado}) já cadatrado.")
                exit()
        
    def salvar(self):

        df = pd.read_excel('usuarios.xlsx').reset_index(drop=True)
        lista_usuario = self.user.dados_usuario()
        cpf_existe = lista_usuario[3]
        email_existe = lista_usuario[4]
        
        self.verificar_cadastro(cpf_existe, df["CPF"])    
        
        self.verificar_cadastro(email_existe, df["Email"]) 

        df.loc[len(df)] = self.user.dados_usuario()
        
        #print(df)

        df.to_excel("usuarios.xlsx", index = False)

        



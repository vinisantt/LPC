class Projeto:
        
        def __init__(self,nome,data_inicio,data_fim):
            self.nome = nome
            self.data_inicio = data_inicio
            self.data_fim = data_fim
            

        def __str__(self):
            return "Pessoa." + self.nome


class Atividade:
    

    def __init__(self,nome,data_inicio,data_fim,prioridade,pessoa,projeto):
        self.nome = nome
        self.prioridade = prioridade
        self.projeto = projeto
        self.pessoa = pessoa
        self.status = "Ativa"

    def __str__(self):
        return self.nome

    def finalizar_atividade(self):
        self.status = "Finalizada"
         


class Pessoa:
   
    def __init__(self,nome,data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return nome


class Endereço:
    pass

p = Projeto("Projeto1","15-02-2019","31-12-2019")
pe = Pessoa("Vinicius","24-09-1998")
a = Atividade("Atividade1","Máxima","20-02-2019","21-02-2019",pe,p)



print("Nome da atividade:",a.nome,"   ","Status:",a.status)
a.finalizar_atividade()
print("Nome da atividade:",a.nome,"   ","Status:",a.status)

# LPC

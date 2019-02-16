class Projeto:
        
        def __init__(self,nome,data_inicio,data_fim):
            self.nome = nome
            self.data_inicio = data_inicio
            self.data_fim = data_fim
            

        def __str__(self):
            return "Pessoa." + self.nome


class Atividade:
    

    def __init__(self,nome,data_inicio,data_fim,prioridade,pessoa):
        self.nome = nome
        self.prioridade = prioridade
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


class Projeto_Atividade:
        def __init__(self,projeto,atividade):
                self.projeto = projeto
                self.atividade = atividade

        def __str__(self):
                return "Nome do projeto:" + self.projeto.nome + "\nNome da atividade:" + self.atividade.nome

p = Projeto("Projeto1","15-02-2019","31-12-2019")
pe = Pessoa("Vinicius","24-09-1998")
a = Atividade("Atividade1","Máxima","20-02-2019","21-02-2019",pe)
pa = Projeto_Atividade(p,a)


print("Nome da atividade:",a.nome,"   ","Status:",a.status)
a.finalizar_atividade()
print("Nome da atividade:",a.nome,"   ","Status:",a.status)
print('*'*52)
print(Projeto_Atividade)

# LPC

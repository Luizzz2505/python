class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.amigos = []

    def adicionar_amigo(self, amigo):
        self.amigos.append(amigo)
        print(f"{amigo.nome} foi adicionado aos amigos de {self.nome}.")

    def mostrar_amigos(self):
        amigos_str = ', '.join(amigo.nome for amigo in self.amigos)
        print(f"Amigos de {self.nome}: {amigos_str}" if self.amigos else f"{self.nome} não tem amigos ainda.")

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    def exibir_info_funcionario(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Cargo: {self.cargo}, Salário: {self.salario}")

    def aumentar_salario(self, percentual):
        self.salario *= (1 + percentual / 100)
        print(f"O salário de {self.nome} foi aumentado em {percentual}%. Novo salário: {self.salario}")

# Exemplo de uso
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)
funcionario1 = Funcionario("Carlos", 35, "Desenvolvedor", 5000)

pessoa1.cumprimentar()
pessoa1.adicionar_amigo(pessoa2)
pessoa1.mostrar_amigos()

funcionario1.exibir_info_funcionario()
funcionario1.aumentar_salario(10)


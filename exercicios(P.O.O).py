#Exercicio 1
 #   def __init__(self, modelo, cor, ano, valor):
  #      self.modelo = modelo
   #     self.cor = cor
    #    self.ano = ano
     #   self.valor = valor

   # def exibir_informacoes(self):
    #    print(f"Modelo: {self.modelo}")
     #   print(f"Cor: {self.cor}")
      #  print(f"Ano: {self.ano}")
       # print(f"Valor: R${self.valor}")
       
#modelo = input("Digite o modelo do carro: ")
#cor = input("Digite o cor do carro: ")
#ano = input("Digite o ano do carro: ")
#valor = input("Digite o valor do carro: ")

#car1 = Carro(modelo, cor, ano, valor)

#car1.exibir_informacoes()








#Exercicio 2
#class ContaBancaria:
 #   def _init_(self, titular, saldo):
  #      self.titular = titular
   #     self.saldo = saldo
#
 #   def depositar(self):
  #      
   #     dep = int(input(self.titular, ",digite o valor a ser depositado: "))
    #    self.saldo + dep
     #   print(self.saldo)
    #
    
 #   def sacar(self):
  #      int = i
   #     for i in range(1):
    #     
     #   sac = int(input(self.titular, ",digite o valor a ser sacado: "))
    #
     #   if sac > self.saldo:
      #     print("Esse valor não pode ser sacado por ser maior que o disponível")
       #    i=-1
    #
     #   else: 
      #      self.saldo - sac
       #     print(self.saldo)
        #
   # def Menu(self): 
    #    print( self.titular, "Escolha uma opção abaixo: ")
    #    
    #    while opc < 1 or opc > 3:
    #        opc = int(input( "1- REALIZAR DEPÓSITO\n", "2- REALIZAR SAQUE \n" ))
    #     
    #    if opc == 1 :
    #        self.depositar()
    #    if opc == 2 :
    #        self.sacar()
    #    if opc >= 3 or opc <= 0:
    #        print("Opção inválida...")
        
#usu1 = ContaBancaria("Aline", 0)

#usu1.Menu()








#Exercicio 3

#class Animal:
 #      def emitiSom(self):
  #            print("Som dos Animais")

#class Cachorro(Animal):
#        def emitirSom(self):
#               print("Latindo...")

#class Gato(Animal):
#        def emitirSom(self):
#               print("Miando...")

#cachorro = Cachorro()
#cachorro.emitirSom()

#gato = Gato
#gato.emitirSom()







#Exercicio 4
#class funcionario:
#    def _init_(self, nome, salario):
#        self.nome = nome
#        self.salario = salario
#        

#    def exibir_informacoes(self):
#         print(f"Nome: {self.nome}")
#         print(f"Salario: R${self.salario:.2f}")
    
#funcionario1 = funcionario("Marcos", 1900.00)

#funcionario1.exibir_informacoes()
#def exibir_informacoes(self):
 #        print(f"Nome: {self.nome}")
  #       print(f"Salario: R${self.salario:.2f}")
    
#funcionario2 = funcionario("Pedro", 2400.00)

#funcionario2.exibir_informacoes()
#def exibir_informacoes(self):
#         print(f"Nome: {self.nome}")
#         print(f"Salario: R${self.salario:.2f}")
    
#funcionario3 = funcionario("Gabriel", 3900.00)

#funcionario3.exibir_informacoes()

#class Funcionario:
#    def _init_(self, nome, salario):
#        """Método construtor para inicializar o nome e salário do funcionário"""
#        self.nome = nome
#        self.salario = salario

#    def exibir_informacoes(self):
#        """Método para exibir o nome e salário do funcionário"""
#        print(f"Nome: {self.nome}")
#        print(f"Salário: R${self.salario:.2f}")

   #     print("\n")


#class Gerente(Funcionario):
 #   def _init_(self, nome, salario, bonus):
  #      super()._init_(nome, salario)  
   #     self.bonus = bonus

    #def exibir_informacoes(self):
     #   salario_total = self.salario + self.bonus  
      #  print(f"Nome: {self.nome}")
       # print(f"Salário: R${self.salario:.2f}")
        #print(f"Bônus: R${self.bonus:.2f}")
       # print(f"Salário total com bônus: R${salario_total:.2f}")

#gerente1 = Gerente("Gerente Julia", 3000.00, 900.00)
#gerente1.exibir_informacoes()
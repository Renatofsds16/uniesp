class Aluno:
  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.media = 0.0


  def calcular_media(self):
    self.media = (self.nota1 + self.nota2) / 2
    return self.media


  def mostrar_informacoes(self):
    print(f"Nome: {self.nome}")
    print(f"Nota 1: {self.nota1}")
    print(f"Nota 2: {self.nota2}")

  def resultado_final(self):
    if self.media >= 6:
      print("Aprovado")
    else:
      print("Reprovado")


aluno1 = Aluno("renato",10,10)
aluno2 = Aluno("carol",10,9)
aluno3 = Aluno("clara",7,8)

aluno2.calcular_media()
aluno2.mostrar_informacoes()
aluno2.resultado_final()


class Carro:
  def __init__(self):
    self.velocidade = 0

  def acelerar(self):
    self.velocidade += 10
    print("O carro está acelerando!")

  def frear(self):
    self.velocidade -= 10
    if self.velocidade < 10:
      self.velocidade = 0
    print("O carro está freando!")


carro = Carro()
for i in range(10):
  carro.acelerar()
  print(carro.velocidade)
carro.frear()
print(carro.velocidade)


class Pessoa:
  def __init__(self,nome):
    self.nome = nome


  def cumprimentar(self):
    print(f"Olá, {self.nome}!")


pessoa = Pessoa("renato")
pessoa.cumprimentar()


class Calculadora:
  def __init__(self,a,b):
    self.a = a
    self.b = b


  def soma(self):
    return self.a + self.b


  def subtracao(self):
    return self.a - self.b


  def multiplicacao(self):
    return self.a * self.b


  def divisao(self):
    if self.b == 0:
      return "Não é possível dividir por zero!"
    return self.a / self.b


calculadora = Calculadora(10,0)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())


class Retangulo:
  def __init__(Self, altura, largura):
    Self.largura = largura
    Self.altura = altura

  def calcular_area(self):
    return self.largura * self.altura

  def calcular_perimetro(self):
    return 2 * (self.largura + self.altura)


retangulo = Retangulo(10,5)
print(retangulo.calcular_area())
print(retangulo.calcular_perimetro())
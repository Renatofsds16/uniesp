
aluno='Nisston Moraes Tavares de Melo'
# Qual é o número de caracteres?
# Qual é o número de palavras?
# Qual é o número de vogais?
# Qual é o número de consoantes?
# Quais os caracteres se repetem?
# Quantos espaços em branco existem?
# Quais as iniciais do nome?
# Qual a palavra mais longa?
# Qual o tamanho das palavras?
# Formato de citação acadêmica (ABNT): extrair o último sobrenome em caixa alta seguido das iniciais.
class Dados:
    def __init__(self,string:str):
        self.string = string

    def caractere(self):
        return len(self.string)

    def contador_palavra(self):
        return len(self.string.split())

    def numero_vogais(self):
        count = 0
        for letra in self.string.lower():
            if letra in ('aeiou'):
                count += 1
        return count

    def numero_consoante(self):
        count = 0
        for letra in self.string.lower():
            if letra.isalpha() and letra not in  ('aeiou'):
                count += 1
        return count

    def letra_repetida(self):
        pass




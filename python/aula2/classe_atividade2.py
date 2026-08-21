aluno='Nisston Moraes Tavares de Melo'
class Dados:
    def __init__(self,string:str):
        self.string = string

    def qtd_caractere(self):
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


    def letras_repetidas(self):
        return list({s for s in self.string if self.string.count(s) > 1 and s != ' '})


    def caractere_branco(self):
        return self.string.count(' ')


    def iniciais_nome(self):
        return [s[0] for s in self.string.split(' ')]


    def palavra_mais_longa(self):
        return max(self.string.split(),key=len) 


    def tamanho_das_palavras(self):
        return [len(s) for s in self.string.split(' ')]


    def formato(self):
        return f'{self.string.split()[-1].upper()}  {self.iniciais_nome()[:-1]}'
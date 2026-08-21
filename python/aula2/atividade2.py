from classe_atividade2 import Dados,aluno
dados = Dados(aluno)
print('Qual é o número de caracteres? ',dados.qtd_caractere())
print('Qual é o número de palavras? ',dados.contador_palavra())
print('Qual é o número de vogais? ',dados.numero_vogais())
print('Qual é o número de consoantes? ',dados.numero_consoante())
print('Quais os caracteres se repetem? ',dados.letras_repetidas())
print('Quantos espaços em branco existem? ',dados.caractere_branco())
print('Quais as iniciais do nome? ',dados.iniciais_nome())
print('Qual a palavra mais longa?',dados.palavra_mais_longa())
print('Qual o tamanho das palavras? ',dados.tamanho_das_palavras())
print('Formato de citação acadêmica (ABNT): extrair o último sobrenome em caixa alta seguido das iniciais. ',dados.formato())





# -- coding: utf-8 --
# Code by Gustavo Valle
# Nickname: Half Blood Tech
"""
Código feito em Python no dia 16 de Julho de 2020
O objetivo do código é puramente para aprimorar os conhecimentos e lógica na linguagem Python
"""
from os import system
from sys import exit
from time import sleep
from platform import system as sistema_operacional

limpar = ''
if(sistema_operacional() == 'Linux'):
    limpar = 'clear'
elif(sistema_operacional() == 'Windows'):
    limpar = 'cls'

system(limpar)

print(f'Bem-vindo(a) à Cifra de Cesar, usuário de {sistema_operacional()}. O que deseja fazer?\n')
print('1 - Criptografar uma mensagem')
print('2 - Descriptografar uma mensagem')
print('3 - Saber um pouco sobre a Cifra de Cesar')
opcao = input('\nDigite a opção desejada: ')

try:
    opcao = int(opcao)
except ValueError:
    system(limpar)
    print('Opção inválida! A chave deve ser numérica\nPor gentileza, tente novamente...')
    sleep(2)


if opcao == 1:
    system(limpar)
    mensagem = input('Digite a mensagem a ser cifrada: ').upper()
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

    cifrada = ''

    chave = input('Digite a chave a ser utilizada: ')

    try:
        chave = int(chave)
        if(chave <= 26):
            for letra in mensagem:
                if(letra in letras):
                    num = letras.find(letra)
                    cifrada = cifrada + letras[num+chave]
                elif(letra == ' '):
                    cifrada = cifrada + ' '

        else:
            system(limpar)
            print('A chave não pode ser maior que 26...')
        if(chave <= 26):
            system(limpar)
            print(f'Mensagem criptografada:\n{cifrada.title()}')

    except ValueError:
        system(limpar)
        print('A chave digitada deve ser numérica...')
        sleep(2)


elif opcao == 2:
    system(limpar)

    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    traduzida = ''

    mensagem = input('Digite a mensagem a ser decifrada: ').upper()
    chave = input('Digite a chave: ')

    try:
        chave = int(chave)
        for letra in mensagem:
            if letra in letras:
                num = letras.find(letra)
                traduzida = traduzida + letras[num-chave]
            elif letra == ' ':
                traduzida = traduzida + ' '
        system(limpar)
        if len(traduzida) != len(mensagem):
            print('Não foi possível decifrar a mensagem.\nVerifique a mensagem e a chave e tente novamente')
            sleep(2)
            exit()

        print(f'Mensagem decifrada:\n{traduzida.title()}')
        sleep(2)

    except ValueError:
        system(limpar)
        print('A chave digitada deve ser numérica...')
        sleep(2)


elif opcao == 3:
    system(limpar)
    print('**CIFRA DE CESAR**\n\n')
    print('\tA Cifra de César é uma técnica de criptografia bastante simples e provavelmente a mais conhecida de todas.')
    print('\tTrata-se de um tipo de cifra de substituição, na qual cada letra de um texto a ser criptografado é')
    print('substituída por outra letra, presente no alfabeto porém deslocada um certo número de posições à esquerda ou à direita.')
    sleep(2)

elif opcao > 3 or opcao < 1:
    system(limpar)
    print('Opção não encontrada... Até +')
    sleep(2)
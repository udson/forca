import os
import random


def main():
  tema = ''
  while(tema not in ['1','2','3']):
    os.system('cls')
    print('-' * 30)
    print('  J O G O   D A   F O R C A')
    print('-' * 30)
    print('Animais = 1')
    print('Comidas = 2')
    print('Profissões = 3')
    print('Sair = 0')
    print(' ')

    tema = input('Escolha um tema e digite o número correspondente: ')

    if(tema == '0'):
      break
    elif(tema == '1'):
      os.system('cls')
      print("Tema escolhido: Animais")
      animais =  open('temas/animais.txt', 'r')
      palavra = random.choice(animais.readlines())
      animais.close()
      for letra in palavra:
        if letra == ' ':
          print(letra, end='')
        else:
         print('_ ', end='')

    elif(tema == '2'):
      os.system('cls')
      print("Tema escolhido: Comidas")
      comidas =  open('temas/comidas.txt', 'r', encoding='utf-8')
      palavra = random.choice(comidas.readlines())
      comidas.close()
      print('\n', palavra, sep='')

    elif(tema == '3'):
      os.system('cls')
      print("Tema escolhido: Profissões")
      profissoes =  open('temas/profissoes.txt', 'r', encoding='utf-8')
      palavra = random.choice(profissoes.readlines())
      profissoes.close()
      print('\n', palavra, sep='')


if __name__ == "__main__":
  main()

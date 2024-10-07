import os
import random

forca = ['''
  +---+
  |   |
  |   O
  |  /|\  
  |  / \ 
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   O
  |  /|\  
  |  /  
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   O
  |  /|\  
  |    
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   O
  |  /|  
  |    
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   O
  |    
  |    
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   
  |    
  |    
  | 
  +=========   
  ''',
  '''
  +---+
  |   
  |   
  |    
  |    
  | 
  +=========   
  ''']

def escolhe_palavra(tema:int):
  temas = ['Animais', 'Comidas', 'Profissões']
  with open('temas/{}.txt'.format(temas[tema - 1]), 'r') as arquivo:
    return (random.choice(arquivo.readlines()).strip(), temas[tema - 1])

def main():
  tema = ''
  while tema not in ['1','2','3']:
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

    if tema == '0':
      break
    else:
      palavra, nome_arquivo = escolhe_palavra(int(tema))
      os.system('cls')
      tentativas = 7
      palpites = []
      while tentativas:
        os.system('cls')
        print("Tema escolhido: {}.\n\n".format(nome_arquivo))
        print(forca[tentativas - 1])
        for letra in palavra:
          if letra == ' ':
            print('  ', end='')
          elif letra in palavra and letra in palpites:
            print(letra, end='')
          else:
            print(' _ ', end='')
        print('\n\nVocê tem {} tentativas.\n\n'.format(tentativas))
        print('Palpites: {}'.format(palpites))
        # print(palavra)
        palpite = input('Chute uma letra ou a palavra: ')
        palpites.append(palpite.upper().strip())

        if(palpite.upper().strip() not in palavra):
          tentativas -= 1
        
        if palavra in palpites:
          os.system('cls')
          print('Parabéns! Você venceu!')
          print('A palavra era {}.'.format(palavra))
          break
      
      if tentativas == 0:
        os.system('cls')
        print('Que pena! Você foi enforcado!')
        print('A palavra era {}.'.format(palavra))


if __name__ == "__main__":
  main()

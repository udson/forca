import os


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
    elif(tema == '2'):
      os.system('cls')
      print("Tema escolhido: Comidas")
    elif(tema == '3'):
      os.system('cls')
      print("Tema escolhido: Profissões")


if __name__ == "__main__":
  main()

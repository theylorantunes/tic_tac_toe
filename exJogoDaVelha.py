import random


jogar = "n"

def jogarDenovo(jogar):
  if jogar == "n":
    print('')
  elif jogar == "s":
    JogoDaVelha()
  else:
    print('Não é uma opção')

def JogoDaVelha():
  tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  acabou = False
  QuadradoMagico = [4, 9, 2, 3, 5, 7, 8, 1, 6]

  sORn = True
  def tabCheio_or_Vazio(sORn):
    if tabuleiro[0] == "" or tabuleiro[1] == "" or tabuleiro[2] == "" or tabuleiro[3] == "" or tabuleiro[4] == "" or tabuleiro[5] == "" or tabuleiro[6] == "" or tabuleiro[7] == "" or tabuleiro[8] == "":
      sORn = True
      return sORn
    else:
      sORn = False
      return sORn

  def ImprimirTabuleiro():
    print()
    print('', tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---|---|---")
    print('', tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---|---|---")
    print('', tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()

  def PegarNumero():
    while True:
      numero = input()
      try:
        numero  = int(numero)
        if numero in range(1, 10):
          return numero
        else:
          print("\nNúmero não está no tabuleiro.")
      except ValueError:
        print("\nIsso não é um número. Tente novamente.")
        continue

  def Turno(jogador):
    espaco_colocado = PegarNumero() - 1
    if tabuleiro[espaco_colocado] == "X" or tabuleiro[espaco_colocado] == "O":
      print("\nEspaço já ocupado. Tente colocar em outro.")
      Turno(jogador)
    else:
      tabuleiro[espaco_colocado] = jogador

  def ChecaVitoria(jogador):
    jogadas = 0

    for x in range(9):
      for y in range(9):
        for z in range(9):
          if x != y and y != z and z != x:
            if tabuleiro[x] == jogador and tabuleiro[y] == jogador and tabuleiro[z] == jogador:
              if QuadradoMagico[x] + QuadradoMagico[y] + QuadradoMagico[z] == 15:
                print("Jogador", jogador ,"ganhou!\n")
                print(tabCheio_or_Vazio(sORn))
                jogar = str(input('Quer jogar denovo? s/n\n'))
                jogarDenovo(jogar)
                return True

    for a in range(9):
      if tabuleiro[a] == "X" or tabuleiro[a] == "O":
        jogadas += 1
      if jogadas == 9:
        print("O jogo acabou em um empate\n")
        jogar = str(input('Quer jogar denovo? s/n\n'))
        jogarDenovo(jogar)
        
        return True
 
  sorteio = random.randint(1, 2)
  if sorteio == 1:
    while not acabou:
      ImprimirTabuleiro()
      acabou = ChecaVitoria("O")

      if acabou == True:
        break
      print("Jogador X, escolha um espaço.")
      Turno("X")
    
      ImprimirTabuleiro()
      acabou = ChecaVitoria("X")
      if acabou == True:
        break
      print("Jogador O, escolha um espaço.")
      Turno("O")
  if sorteio == 2:
    while not acabou:
      ImprimirTabuleiro()
      acabou = ChecaVitoria("X")

      if acabou == True:
        break
      print("Jogador O, escolha um espaço.")
      Turno("O")
    
      ImprimirTabuleiro()
      acabou = ChecaVitoria("O")
      if acabou == True:
        break
      print("Jogador X, escolha um espaço.")
      Turno("X")    


JogoDaVelha()
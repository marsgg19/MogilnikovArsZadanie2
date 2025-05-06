import os

def p(board):  # выводим поле
 os.system('cls' if os.name=='nt' else 'clear')
 for l in board: print(' '.join(l))

def win(b, s):  # проверка победы
 for i in range(1,4):
  if b[i][1]==b[i][2]==b[i][3]==s or b[1][i]==b[2][i]==b[3][i]==s:
   return 1
 if b[1][1]==b[2][2]==b[3][3]==s or b[1][3]==b[2][2]==b[3][1]==s:
  return 1
 return 0

def board_full(bb):
 for q in range(1,4):
  for w in range(1,4):
   if bb[q][w]==' ':
    return 0
 return 1

# старт
pole = [[' ', '1', '2', '3'],
        ['A', ' ', ' ', ' '],
        ['B', ' ', ' ', ' '],
        ['C', ' ', ' ', ' ']]

t = '1'
S = {'1':'X','2':'O'}
print("Игра началась\n")

while True:
    p(pole)
    print("Игрок",t,"введи место от A1 до C3:")
    m = input().strip().lower()
    if len(m)!=2: continue
    rr = {'a':1,'b':2,'c':3}
    cc = {'1':1,'2':2,'3':3}
    try:
     r = rr[m[0]]
     c = cc[m[1]]
    except: continue
    if pole[r][c]!=' ':
     print("Место занято")
     input("Введите заново")
     continue
    pole[r][c] = S[t]
    if win(pole,S[t]):
     p(pole)
     print("Игрок",t,"Победил")
     break
    if board_full(pole):
     p(pole)
     print("ничья")
     break
    t = '2' if t=='1' else '1'

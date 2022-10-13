# Задача 2. Создайте программу для игры с конфетами человек против человека.
#Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота 'интеллектом'
import random
from random import randint as rd

print('Дорбро пожаловать в игру "Забери сколько сможешь ^-^"\n'
     'Для начало расскажу вам правило: На столе лежит 150 конфет.\n'
    'Играют два игрока делая ход друг после друга. Первый ход определяется\n'
     'жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n' 
      'Все конфеты оппонента достаются сделавшему последний ход.\n')

messages = ['Ваш ход брать конфеты', 'Конфеты ждут тебя', 'Конфеты, конфеты, конфеты',
            'Бери бооольше', 'Берите еще', 'Быстрее']

def inputname(name):
    i = int(input(f"{name}, сколько конфет хотите взять? "))
    print(random.choice(messages))
    while i < 1 or i > 28:
        i = int(input(f"{name}, помните что вы можете взять от 1 до 28 конфет!"))
    return i

def text(name, k, counter, quantity):
   print(f"{name}, у вас теперь {counter} конфет. Осталось {quantity}.")

player1 = input("Введите имя игрока: ")
player2 = "Искусственный интелект"
print('Давайте узнаем кто победит в битве за сладости')
print('Игрок под номером №1: ',player1)
print('Игрок под номером №2: ',player2)
quantity = 150
print('Вообщем у вас 150 конфет')
turn = rd(0,2) 
if turn:
    print(f"Первый ход за вами {player1}")
else:
    print(f"Первый ход за {player2}")

count = 0 
count1 = 0

while quantity > 28:
    if turn:
        k = inputname(player1)
        count += k
        quantity -= k
        turn = False
        text(player1, k, count, quantity)
    else:
        k = inputname(player2)
        count1 += k
        quantity -= k
        turn = True
        text(player2, k, count1, quantity)

if turn:
    print(f"Гип Гип урааа! Выиграл {player1}")
else:
    print(f"Гип Гип урааа! Выиграл {player2}")


#Задача 3. Создайте программу для игры в 'Крестики-нолики'
#************С использованием Тkinter

from tkinter import *
import random
import tkinter
root = Tk()
root.title('Criss-cross')
game_run = True
field = []
cross_count = 0

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')

def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False

def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Georgia', 20, 'bold'),
                        background='purple',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()

#********Без использования Тkinter

from random import choice

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def drawBoard(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def takeText(choice):
   first = False
   while not first:
      answer = input("Куда поставим " + choice+"? ")
      try:
        answer = int(answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if answer >= 1 and answer <= 9:
         if(str(board[answer-1]) not in "XO"):
            board[answer-1] = choice
            first = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def checkWin(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), 
                (0,3,6), (1,4,7), (2,5,8), 
                (0,4,8), (2,4,6))               
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        drawBoard(board)
        if counter % 2 == 0:
           takeText("X")
        else:
           takeText("O")
        counter += 1
        if counter > 4:
           tmp = checkWin(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    drawBoard(board)
main(board)

input(" < Для выхода нажмите Enter >")

#Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

with open('RLE_024.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('RLE_024.txt', 'r') as file:
    mytext = file.readline()
    text_compression = mytext.split()

print(mytext)


def RLEencode(text):
    enconding = ''
    prev_char = ''
    count = 1

    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding

def RLEdecode(data):
    decode = '' 
    count = '' 
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char *int(count)
            count = ''
    return decode
    
text_compression = RLEencode(mytext)
text_compression = RLEdecode(mytext)

with open('RLE_024.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)
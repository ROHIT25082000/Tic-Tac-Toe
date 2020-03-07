#!/usr/bin/env python3
""" This is a basic version of the tic tac toe to revisit my basics of python programming """
game = [[0,0,0],        # This is gameboard which will be shown every time 
        [0,0,0],
        [0,0,0]]

def print_board():
    print('                        ',end ='')
    print('Current board position\n')     #displays the board 
    print('                        ',end='')
    print('    0    1    2',end='\n\n')
    for i in range(len(game)):
        print('                        ',end='')
        print(i,end=' ')
        for j in range(len(game[i])):
            if(j!=len(game[i])-1):
                if(game[i][j]==0):
                    print('   ',end=' | ')
                elif(game[i][j]==1):
                    print(' X ',end=' | ')
                else:
                    print(' O ',end=' | ')
            elif(i!=len(game)-1):
                 if(game[i][j]==0):
                    print('   ',end='\n')
                    print('                        ',end='')
                    print('  ----------------')
                 elif(game[i][j]==1):
                    print(' X ')
                    print('                        ',end='')
                    print('  ----------------')
                 else: 
                    print(' O ')
                    print('                        ',end='')
                    print('  ----------------')
            else:
                 if(game[i][j]==0):
                    print('   ',end='\n')
                 elif(game[i][j]==1):
                    print(' X ')
                 else: 
                    print(' O ')
    print() 
    print('Ctrl + Z : to Exit')


def check_win():
    """ Horizontal win checks """
    for i in range(len(game)):
        if game[i].count(1)==3:
            print('         X wins!!!')
            return 1
        elif game[i].count(2)==3:
            print('         O wins!!!')
            return 1
    """No horizontal wins and checks for diagonal wins"""
    ele = []
    for i in range(len(game)):
        ele.append(game[i][i])
    if ele.count(1)==3:
        print()
        print()
        print('         X wins!!!')
        return 1
    elif ele.count(2)==3:
        print()
        print()
        print('         O wins!!!')
        return 1
    ele1 = []
    for i in range(len(game)-1,-1,-1):
        ele1.append(game[i][i])
    if ele.count(1)==3:
        print()
        print()
        print('         X wins!!!')
        return 1
    elif ele.count(2)==3:
        print()
        print()
        print('         O wins!!!')
        return 1
    """Vertical win check"""
    for i in range(len(game)):
        new=[]
        for j in range(len(game)):
            new.append(game[j][i])
        if new.count(1)==3:
            print('         X wins!!!')
            return 1
        elif new.count(2)==3:
            print('         O wins!!!')
            return 1
    return 0

def enter_num(value,row,col):
    if value=='X'or value=='x':
        if game[row][col]==0:
            game[row][col] = 1
            return 1
        else:
            print('That\'s Already filled Try again')
            return 0
    elif value=='O'or value=='o':
        if game[row][col]==0:
            game[row][col] = 2
            return 1
        else:
            print('That\'s Already filled Try again')
            return 0
    else:
        print('!!Enter valid row,col!!')


def ongoing():
    player_1 = input('Enter player_1 (X):')
    player_2 = input('Enter player_2 (O):')

    count=1
    for i in range(len(game)):
        for j in range(len(game)):
            if count%2==1:
                print('                        ',end='')
                print(player_1,'(X)','\'s turn')
                print('row col')
                input_stream = list(input())
                result = enter_num('x',int(input_stream[0]),int(input_stream[1]))
                while result!=1:
                    print('row col')
                    input_stream = list(input())
                    result = enter_num('x',int(input_stream[0]),int(input_stream[1]))
                l = check_win()
                count+=1
                if(1==l):
                    print_board()
                    start()
                    return
                print_board()
            elif count%2==0:
                print('                        ',end='')
                print(player_2,'(O)','\'s turn')
                print('row col')
                input_stream = list(input())     
                result = enter_num('o',int(input_stream[0]),int(input_stream[1]))
                while result!=1:
                    print('row col')
                    input_stream = list(input())
                    result = enter_num('o',int(input_stream[0]),int(input_stream[1])) 
                l = check_win()
                count+=1
                if(1==l):
                    print_board()
                    start()
                    return
                print_board()
    print('Okay it\'s a Tie!!')
    start()
def start():
    for i in range(3):
        for j in range(3):
            game[i][j] =0
    n = input('Do you want to play again Y|n')
    if n=='Y' or n=='y':
        ongoing()
    else:
        print('See ya!')

""" This is the way it goes on"""

print('                        Welcome to _TIC_TAC_TOE_\n\n')
print_board()
print('\n\n')
ongoing()

            













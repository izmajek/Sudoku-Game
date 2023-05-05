'''Name: Israel Majek
Course: AUCSC 113
Date: Saturday December 10 2022
Assignment: Sudoku Project2
This file contains 6 parent functions
Function display board for displaying the 9x9 sudoku board
Function all cells filled for printing complete message when sudoku game has been solved
Function Horizontal_rule_violated for checking if the more than 1 number is on the x axis
Function Vertical_rule_violated for checking if the more than 1 number is on the y axis
Function square_rule_violated for checking  each 3x3 square and sees if there is more than 1 value.
Function board input has 26 functions. Each functions does their own thing but overall
they are for inputting user input into the board and for checking errors and
printing the hints.'''

#Colors:
Black = "\033[0;30m" 
Green = "\033[0;32m"
Background_Red = "\033[41m"
Bold_Yellow="\033[1;33m"
Normal = '\033[0m'
Background_Purple="\033[45m"
Bold_Red="\033[1;31m"
Red="\033[0;31m"
Purple="\033[0;35m"
Yellow="\033[0;33m"

board = eval(input('Enter your 2-d board (9x9): '))#User Input
k = [[' ', ' ', 2, ' ', ' ', 1, ' ', 4, ' '], [6, ' ', 4, ' ', ' ', ' ', ' ', ' ', 8], [' ', ' ', ' ', ' ', 6, ' ', 5, ' ', ' '], [1, 7, ' ', 2, ' ', 3, ' ', 9, ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 3, ' ', 6, ' ', 9, ' ', 8, 7], [' ', ' ', 3, ' ', 9, ' ', ' ', ' ', ' '], [9, ' ', ' ', ' ', ' ', ' ', 6, ' ', 4], [' ', 1, ' ', 7, ' ', ' ', 3, ' ', ' ']]



def display_board():
    '''Display Board function for displaying 9x9 sudoku board'''
    print('   1 2 3 4 5 6 7 8 9 ')
    print('  +-+-+-+-+-+-+-+-+-+')
    print('1 |{} {} {}|{} {} {}|{} {} {}|'.format(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6], board[0][7], board[0][8]))
    print('2 |{} {} {}|{} {} {}|{} {} {}|'.format(board[1][0], board[1][1], board[1][2], board[1][3], board[1][4], board[1][5], board[1][6], board[1][7], board[1][8]))
    print('3 |{} {} {}|{} {} {}|{} {} {}|'.format(board[2][0], board[2][1], board[2][2], board[2][3], board[2][4], board[2][5], board[2][6], board[2][7], board[2][8]))
    print('  +-+-+-+-+-+-+-+-+-+')
    print('4 |{} {} {}|{} {} {}|{} {} {}|'.format(board[3][0], board[3][1], board[3][2], board[3][3], board[3][4], board[3][5], board[3][6], board[3][7], board[3][8]))
    print('5 |{} {} {}|{} {} {}|{} {} {}|'.format(board[4][0], board[4][1], board[4][2], board[4][3], board[4][4], board[4][5], board[4][6], board[4][7], board[4][8]))
    print('6 |{} {} {}|{} {} {}|{} {} {}|'.format(board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6], board[5][7], board[5][8]))
    print('  +-+-+-+-+-+-+-+-+-+')
    print('7 |{} {} {}|{} {} {}|{} {} {}|'.format(board[6][0], board[6][1], board[6][2], board[6][3], board[6][4], board[6][5], board[6][6], board[6][7], board[6][8]))
    print('8 |{} {} {}|{} {} {}|{} {} {}|'.format(board[7][0], board[7][1], board[7][2], board[7][3], board[7][4], board[7][5], board[7][6], board[7][7], board[7][8]))
    print('9 |{} {} {}|{} {} {}|{} {} {}|'.format(board[8][0], board[8][1], board[8][2], board[8][3], board[8][4], board[8][5], board[8][6], board[8][7], board[8][8]))
    print('  +-+-+-+-+-+-+-+-+-+')

display_board()


def board_input():
    '''Function for inputting user input into the 9x9 board and checking for errors and giving users hints, Inside this function there are 26 functions that does these'''
    inputted_values2 = input('Type a row number, a column number, and a value (e.g., 1 2 9) (If you type only one number, all the cells having the number will be highlighted in the board) (If you want a hint, type h):')
    inputted_values = inputted_values2.split()

    if 's' in inputted_values:

                    
        def find_empty_location(board):
        
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ' ':
                        return (row, col)
            return None

        def is_valid(board, row, col, value):
            for i in range(9):
                if board[row][i] == value or board[row][i] == Green+str(value)+Black:
                    return False
                if board[i][col] == value or board[i][col] == Green+str(value)+Black:
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3] == value or board[3*(row//3)+i//3][3*(col//3)+i%3] == Green+str(value)+Black:
                    return False
            return True

        def solve_sudoku(board):
    
            empty_cell = find_empty_location(board)
            if not empty_cell:
                return True
            row, col = empty_cell
            for value in range(1, 10):
                if is_valid(board, row, col, value):
                    board[row][col] = Green+str(value)+Black
                    
                    if solve_sudoku(board):
                        return True
                    board[row][col] = ' '
            return False
        
    
        if solve_sudoku(board):
            display_board()
        else:
            for i in range(9):
                for j in range(9):
                    for value in range(1,10):
                        if board[i][j] == Green+str(value)+Black or board[i][j] == Bold_Yellow+Background_Red+str(value)+Normal+Black or board[i][j] == Green+str(value)+Black or board[i][j] == str(value)+Black or board[i][j] == Bold_Yellow+Background_Red+str(value)+Black:
                            print((Green+('Unable to Solve Sudoku Board, Row:{}, Col:{} with value {} is wrong')+Black).format(i+1, j+1, value))

    

        
 
    if 's' not in inputted_values:

        def nn():
            '''try and except Error for checking if the first user input is wrong'''
            try:
                if len(inputted_values)>=0 and inputted_values[0]!= 'h':
                    int(inputted_values[0])
                    

            except:
                print(Red+'Your Input is wrong! The first input is wrong'+ Normal)
                return True
            
            
            
        def pl():
            '''try and except error for checking if the user second input is wrong'''
            try:
                if len(inputted_values)>1:
                    int(inputted_values[1])
              
            except:
                print(Red+'Your input is wrong! The second input is wrong'+Normal)
                return True
         
                
                
                
        def kt():
            '''try and except error for checking if the user third input is wrong'''
            try:
                if len(inputted_values)>2:
                    int(inputted_values[2])
                 
            except:
                print(Red+'Your input is wrong! The third input is wrong'+Normal)
                return True
          
                


        

        def b():
            '''Error for checking if input length is not 5'''
            if len(inputted_values2)==1 and str.isdigit(inputted_values2[0]) == False and 'h' not in inputted_values :
                print(Red+'Your input is Wrong! The input length is not 5.'+Normal)
                return True
            else:
                return False
        def c():
            '''error for checking if input length is not 5'''
            if len(inputted_values2)==2 and len(inputted_values)> 1 and str.isdigit(inputted_values[1]) == False and 'h' not in inputted_values:
                print(Red+'Your input is Wrong! The input length is not 5.'+Normal)
                return True
            else:
                return False
        def d():
            '''error for checking if input length is not 5'''
            if len(inputted_values2) > 2 and str.isdigit(inputted_values2[1]) == True and len(inputted_values2)!=5:
                print(Red+'Your input is Wrong! The input length is not 5.'+Normal)
                return True
            else:
                return False
        def e():
            '''error for checking if input length is not 5'''
            if len(inputted_values2)>1 and len(inputted_values2)!=5 and str.isdigit(inputted_values2[0]) == True:
                print(Red+'Your input is Wrong! The input length is not 5.'+Normal)
                return True
            else:
                return False


                    
        def f():
            '''error for checking if input length is not 5'''
            if len(inputted_values2)>1 and len(inputted_values2)!=5 and 'h' not in inputted_values:
                print(Red+'Your input is Wrong! The input length is not 5.'+Normal)
                return True
            else:
                return False

        
           
                
            #if len(inputted_values2) != 5 and len(inputted_values) >=1 and str.isdigit(inputted_values[0]) == True and int(inputted_values[0])>9:
                #print('First input wrong')
        def aa():
            '''error for checking if user did not input 3 seperate numbers'''
            if len(inputted_values2) == 5 and len(inputted_values) >=1 and str.isdigit(inputted_values[0]) == True and int(inputted_values[0])>9:
                print(Red+'Your input is Wrong! You did not input three separate numbers.'+Normal)
                return True
            else:
                return False

        def poi():
            '''error for checking if user first input is wrong'''
            if len(inputted_values2) == 5 and len(inputted_values) >1 and str.isdigit(inputted_values[0]) == True and int(inputted_values[0])<1:
                print(Red+'Your input is Wrong! The first input value is wrong.'+Normal)

            #if len(inputted_values2) == 5 and len(inputted_values)>1 and str.isdigit(inputted_values[1]) == True and int(inputted_values[1])>9 and 1<len(inputted_values[0])<=2:
                #print('Second Input Wrong')
        def v():
            '''error for checking if user second input is wrong'''
                
            if len(inputted_values2) == 5 and len(inputted_values)>1 and str.isdigit(inputted_values[1]) == True and int(inputted_values[1])>9 and 1<len(inputted_values[1])<=2:
                print(Red+'Your input is Wrong! The second input value is wrong.'+Normal)
                return True
            else:
                return False
        def v2():
            '''error for checking if user second input is wrong'''
            if len(inputted_values2) == 5 and len(inputted_values)>1 and str.isdigit(inputted_values[1]) == True and int(inputted_values[1])<1:
                print(Red+'Your input is Wrong! The second input value is wrong.'+Normal)
                return True
            else:
                return False

        def v3():
            '''error for checking if user second input is wrong'''
            if len(inputted_values) == 1 and len(inputted_values2)>1 and str.isdigit(inputted_values2[1]) == False:
                print(Red+'Your input is Wrong! The second input value is wrong.'+Normal)
                return True
            else:
                return False

        def goi():
            '''error for checking if user third input is wrong'''
            if len(inputted_values2) == 5 and len(inputted_values)>2 and str.isdigit(inputted_values[2]) == True and int(inputted_values[2])<1:
                print(Red+'Your input is Wrong! The third input value is wrong.'+Normal)
                return True
            else:
                return False

        def goi2():
            '''error for checking if user third input is wrong'''
            if len(inputted_values2) == 5 and inputted_values2[4] == ' 'and len(inputted_values)>=2:
                print(Red+'Your input is Wrong! The third input value is wrong.'+Normal)
                return True
            else:
                return False
        def bb():
            '''error for cehcking if user did not input 3 seperate numbers'''
            if len(inputted_values2) == 5 and len(inputted_values)>=1 and str.isdigit(inputted_values[0]) == True and len(inputted_values[0])>2:
                print(Red+'Your input is Wrong! You did not input three separate numbers.'+Normal)
                return True
            else:
                return False

        def cc():
            '''error for checking if user did not input 3 seperate numbers'''
            if len(inputted_values2) == 5 and len(inputted_values)>1 and str.isdigit(inputted_values[1]) == True and len(inputted_values[1])>2:
                print(Red+'Your input is Wrong! You did not input three separate numbers.'+Normal)
                return True
            else:
                return False
            
       #Functions are called here so errors can only be printed 1 by 1     
        if nn()== True:
            pass
        elif pl() == True:
            pass
        elif kt() == True:
            pass
        elif b() == True:
            pass
        elif c() == True:
            pass
        elif d() == True:
            pass
        elif e() == True:
            pass
        elif f() == True:
            pass
        elif aa() ==True:
            pass
        elif bb() == True:
            pass
        elif poi() == True:
            pass
        elif v() == True:
            pass
        elif v2() == True:
            pass
        elif v3()== True:
            pass
        elif goi() == True:
            pass
        elif goi2() == True:
            pass
        elif cc() == True:
            pass

                
        #If statement if user inputs the right length and right input then adds the value to the board
        if len(inputted_values2) == 5  and len(inputted_values)==3 and inputted_values2!='     ' and inputted_values2[4] != ' ' and str.isdigit(inputted_values2[0])==True and str.isdigit(inputted_values2[2]) == True and int(inputted_values2[0])<=9 and int(inputted_values[1])<=9 and  str.isdigit(inputted_values2[4]) == True and 0<int(inputted_values2[0])<=9 and 0<int(inputted_values2[2])<=9 and 0<int(inputted_values2[4])<=9 and ' ' in inputted_values2:
            
            k = [[' ', ' ', 2, ' ', ' ', 1, ' ', 4, ' '], [6, ' ', 4, ' ', ' ', ' ', ' ', ' ', 8], [' ', ' ', ' ', ' ', 6, ' ', 5, ' ', ' '], [1, 7, ' ', 2, ' ', 3, ' ', 9, ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 3, ' ', 6, ' ', 9, ' ', 8, 7], [' ', ' ', 3, ' ', 9, ' ', ' ', ' ', ' '], [9, ' ', ' ', ' ', ' ', ' ', 6, ' ', 4], [' ', 1, ' ', 7, ' ', ' ', 3, ' ', ' ']]
            
            
            row = int(inputted_values[0])-1
            col = int(inputted_values[1])-1 
            value = int(inputted_values[2])
            
            #For range for checking if there is something in the board and the spot is not empty
            for l in range(1,10):
                if board[row][col] == l or board[row][col] == Bold_Yellow+Background_Red+str(l)+Normal+Black or board[row][col] == Green+str(l)+Black or board[row][col] == str(l)+Black or board[row][col] == Bold_Yellow+Background_Red+str(l)+Black: 
                    print(Red+'Your input is Wrong! The spot is not empty.'+Normal)

            #Changes highlighted values back to original color
            if board[row][col] == ' ':
                for j in range(1,10):
                    if len(inputted_values) == 3:
                        for x in range(9):
                            for y in range(9):
                                if board[x][y] == str(j)+Black or board[x][y] == Bold_Yellow+Background_Red+str(j)+Normal+Black:
                                    board[x][y] = Green+str(j)+Black
                #Inputs values into board                   
                for j in board:
                    if board.index(j) == int(inputted_values[0])-1:
                        j[int(inputted_values[1])-1] = value
                


                def player():
                    '''If statements for calling rules when they are violated and only prints 1 by 1.'''
           
                    if horizontal_rule_violated(row,col,value) == True:
                        print("============================\nHorizontal rule violated.\nDo it again!\n==============================================")
                        board[row][col] = ' '
                        pass
            
                    elif vertical_rule_violated(row,col,value) == True:
                        print("============================\nVertical rule violated.\nDo it again!\n==============================================")
                        board[row][col] = ' '
                        pass
                    elif square_rule_violated(row,col,value) == True:
                        print("============================\nSquare rule violated.\nDo it again!\n==============================================")
                        board[row][col] = ' '
                        pass
                    else:
                        board[row][col] = Green+str(value)+Black
                        display_board()

                player()

        #If statement for the highlight
        if len(inputted_values2) == 1 and 'h' not in inputted_values and str.isdigit(inputted_values2[0]) == True:
            #For loop for changing the user inputted value into highlighted
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == int(inputted_values[0]):
                        board[i][j] = Bold_Yellow+ Background_Red+str(inputted_values[0])+Normal
                    if board[i][j] == Green+str(inputted_values[0])+Black:
                        board[i][j] = Bold_Yellow+Background_Red+str(inputted_values[0])+Normal+Black
                    if board[i][j] == str(inputted_values[0])+Black:
                        board[i][j] = Bold_Yellow+Background_Red+str(inputted_values[0])+Normal+Black
            #For loop for distinguishing between a coloured letter and a non colored letter for when user highlights
            for m in range(1,10):
                if len(inputted_values) == 1:
                    for x in range(9):
                        for y in range(9):
                            if board[x][y] == Green+str(m)+Black:
                                board[x][y] = str(m)+Black
                        
            display_board()
            #For loop for changing value back to normal and new value into highlight           
            for x in range(9):
                for y in range(9):        
                    if board[x][y] == Bold_Yellow+Background_Red+str(inputted_values[0])+Normal:
                        d = int(inputted_values[0])
                        board[x][y] = d
                    if board[x][y] == Bold_Yellow+Background_Red+str(inputted_values[0])+Normal+Black:
                        board[x][y] = str(inputted_values[0])+Black

    #If statement for the hints  
    if 'h' in inputted_values:
        print(Purple+'=================================HINT========================='+Normal)
        #While true statement to make keep on asking user for input until they get it right
        while True:
            batty = input('Type the cells row number and column number for which you want a hint: ')
            bat = batty.split()
            
            def ll():
                '''Function ll for printing error when user first input is wrong'''
                try:
                    int(bat[0])
                except:
                    print(Red+'Your input is Wrong! The first input value is wrong'+Normal)
                    return True
            def kk():
                '''Function kk for printing error when user second input is wrong'''
                try:
                    if len(bat)>1:
                        int(bat[1])
                except:
                    print(Red+'Your input is Wrong! The second input value is wrong'+Normal)
                    return True

                else:
                    def a():
                        '''Function a for when user first input is wrong'''
                        if len(batty) == 3 and len(bat) >=1 and batty[0] ==' ':
                            print(Red+'Your input is Wrong! The first input value is wrong'+Normal)
                            return True
                        else:
                            return False

                    def p():
                        '''Fucntion p for if the user first input is wrong'''
                        if len(batty) == 3 and len(bat) ==1 and len(bat[0])<=2:
                            print(Red+'Your input is Wrong! The first input value is wrong'+Normal)
                            return True
                        else:
                            return False
                        
       
                        
                    def b():
                        '''Fucntion b for printing error if the user input length is not 3'''
                        if len(batty)==1 and str.isdigit(bat[0]) == True:
                            print(Red+'Your input is Wrong! The input length is not 3'+Normal)
                            return True
                        else:
                            return False

                    def k():
                        '''Fucntion k for if the user input length is not 3'''
                        if len(batty)>1 and str.isdigit(bat[0]) == True and len(batty)!=3:
                            print(Red+'Your input is Wrong! The input length is not 3'+Normal)
                            return True
                        else:
                            return False

                    def G():
                        '''Function g for printing error if the user input length is not 3'''
                        if len(batty)>1 and str.isdigit(bat[0]) == False and len(batty)!=3:
                            print(Red+'Your input is Wrong! The input length is not 3'+Normal)
                            return True
                        else:
                            return False
                    def j():
                        '''Fucntion j for printing error if the user input length is not 3'''
                        if len(batty)>1:
                            print(Red+'Your input is Wrong! The input length is not 3'+Normal)
                            return True
                        else:
                            return False
                    def c():
                        '''Fucntion c for printing error if the user input did not input 3 speerate numbers'''
                        if len(batty) == 3 and len(bat[0])>1 and len(bat[0])>2:
                            print(Red+'Your input is Wrong! You did not input two separate numbers.'+Normal)
                            return True
                        else:
                            return False
                        
                    #Prints errors 1 by 1
                    if G() == True:
                        a = 0
                    elif k() == True:
                        a = 0
                    elif a() == True:
                        a = 0
                    elif p() == True:
                        a=0
                    elif b() == True:
                        a = 0
                    elif a() == True:
                        a = 0
                    elif c() == True:
                        a = 0

            #prints try and except errors 1 by 1
            if ll() == True:
                pass
            elif kk() == True:
                pass

                    
    
                    
            #If statement for checking if spot is empty and for printing an hint when user inputs it right and breaks the loop   
            if len(batty) == 3 and len(bat)==2 and str.isdigit(bat[0]) == True and str.isdigit(bat[1]) == True:
                row  = int(bat[0])-1
                col = int(bat[1])-1
                for m in range(1,10):
                    if board[row][col] == m or board[row][col] == Green+str(m)+Black or board[row][col] == Bold_Yellow+Background_Red+str(m)+Normal+Black or board[row][col] == str(m)+Black or board[row][col] == Bold_Yellow+Background_Red+str(inputted_values[0])+Normal:
                        print(Red+'Your input is wrong! the spot is not empty'+Normal)
                lst = []
                test = []
                if board[row][col] == ' ':
                    for x in range(1,10):
                        test.append(board[x-1][col])
                    for x in range(1,10):
                        if board[row].count(x) != 1 and board[row].count(Green+str(x)+Black)!=1 and board[row].count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and board[row].count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and board[row].count(str(x)+Black)!=1: 
                            if test.count(x)!=1 and test.count(Green+str(x)+Black)!=1 and test.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test.count(str(x)+Black)!=1:
                                if row<=2:
                                    if 5>=col>=3:
                                        test2 = [board[0][3],board[0][4],board[0][5],board[1][3],board[1][4],board[1][5],board[2][3],board[2][4],board[2][5]] 
                                        a = test2.count(x)
                                        if a != 1 and test2.count(Green+str(x)+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test2.count(str(x)+Black)!=1:
                                            lst.append(x)
                            

                     
                                if row<=2:
                                    if col<=2:
                                        test2 = [board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]] 
                                        a = test2.count(x)
                                        if a != 1 and test2.count(Green+str(x)+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test2.count(str(x)+Black)!=1:
                                            lst.append(x)
                
                                if row<=2:
                                    if col>=6:
                                        test2 = [board[0][6],board[0][7],board[0][8],board[1][6],board[1][7],board[1][8],board[2][6],board[2][7],board[2][8]]
                                        a = test2.count(x)
                                        if a != 1 and test2.count(Green+str(x)+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test2.count(str(x)+Black)!=1:
                                            lst.append(x)
                    


                                if 5>=row>=3:
                                    if col<=2:
                                        test2 = [board[3][0],board[3][1],board[3][2],board[4][0],board[4][1],board[4][2],board[5][0],board[5][1],board[5][2]]
                                        a = test2.count(x)
                                        if a != 1 and test2.count(Green+str(x)+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test2.count(str(x)+Black)!=1:
                                            lst.append(x)
               
                                if 5>=row>=3:
                                    if 5<=col<=3:
                                        test2 = [board[3][3], board[3][4], board[3][5], board[4][3], board[4][4], board[4][5], board[5][3],board[5][4],board[5][5]]
                                        a = test2.count(x)
                                        if a != 1 and test2.count(Green+str(x)+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test2.count(str(x)+Black)!=1:
                                            lst.append(x)
                 

                                if 5>=row>=3:
                                    if col>=6:
                                        test2 = [board[3][6],board[3][7],board[3][8],board[4][6],board[4][7],board[4][8],board[5][6],board[5][7],board[5][8]]
                                        a = test2.count(x)
                                        if a != 1 and test2.count(Green+str(x)+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test2.count(str(x)+Black)!=1:
                                            lst.append(x)
                                if row>=6:
                                    if col<=2:
                                        test2 = [board[6][0],board[6][1],board[6][2],board[7][0],board[7][1],board[7][2],board[8][0],board[8][1],board[8][2]]
                                        a = test2.count(x)
                                        if a != 1 and test2.count(Green+str(x)+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test2.count(str(x)+Black)!=1:
                                            lst.append(x)
                                if row>=6:
                                    if 3<=col<=5:
                                        test2 = [board[6][3],board[6][4],board[6][5],board[7][3],board[7][4],board[7][5],board[8][3],board[8][4],board[8][5]]
                                        a = test2.count(x)
                                        if a!=1 and test2.count(Green+str(x)+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test2.count(str(x)+Black)!=1:
                                            lst.append(x)

                                if row>=6:
                                    if col>=6:
                                        test2 = [board[6][6],board[6][7],board[6][8],board[7][6],board[7][7],board[7][8],board[8][6],board[8][7],board[8][8]]
                                        a = test2.count(x)
                                        if a!=1 and test2.count(Green+str(x)+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Normal+Black)!=1 and test2.count(Bold_Yellow+Background_Red+str(x)+Black)!=1 and test2.count(str(x)+Black)!=1:
                                            lst.append(x)
                        
                    print('The possible values for the spot ({},{}) are {}'.format(int(bat[0]),int(bat[1]),Background_Purple+str(lst)+Normal))
                    break
                        

        
                

                
                        

                



def horizontal_rule_violated(row, col, value):
    '''Function horizontal_rule_violated for if there is more than 1 value in the row'''
    test2 = []
    for i in range(9):
        test2.append(board[row][i])
        if test2.count(value)>1 or test2.count(Green+str(value)+Black)==1 or test2.count(Bold_Yellow+Background_Red+str(value)+Normal+Black) == 1 or test2.count(str(value)+Black)==1 or test2.count(Bold_Yellow+Background_Red+str(value)+Normal)==1:
            return True

        
def vertical_rule_violated(row, col, value):
    '''Function vertical_rule_violated(row,col,value) first assigns an empty list to the variable test or then i used a for loop for the range(4) so then i applend the index (i) and (col) of board to test,
then counts the inputted value in test. i then used an if statement that if it is greater than 1 then print vertical rule violated'''
    test = []
    for i in range(9):
        test.append(board[i][col])
        if test.count(value)>1 or test.count(Green+str(value)+Black)==1 or test.count(Bold_Yellow+Background_Red+str(value)+Normal+Black) == 1 or test.count(str(value)+Black)==1 or test.count(Bold_Yellow+Background_Red+str(value)+Normal)==1:
            return True

def square_rule_violated(row,col,value):
    '''Function square rule violated for checking each 3x3 square'''
    #TOP LEFT:
    if row<=2 and col<=2:
        a = []
        for i in range(3):
            for j in range(3):
                if board[i][j] != ' ':
                    a.append(board[i][j])
                    if a.count(value)>1 or a.count(Green+str(value)+Black)==1 or a.count(Bold_Yellow+Background_Red+str(value)+Normal+Black)==1 or a.count(Bold_Yellow+Background_Red+str(value)+Normal)==1 or a.count(str(value)+Black)==1:
                        return True

    #TOP MIDDLE:
    if row<=2 and 3<=col<=5:
        b = []
        for x in range(3):
            for y in range(3,6,1):
                if board[x][y]!=' ':
                    b.append(board[x][y])
                    if b.count(value)>1 or b.count(Green+str(value)+Black)==1 or b.count(Bold_Yellow+Background_Red+str(value)+Normal+Black)==1 or b.count(Bold_Yellow+Background_Red+str(value)+Normal)==1 or b.count(str(value)+Black)==1:
                        return True

    #TOP RIGHT:
    if row<=2 and col>=6:
        c = []
        for i in range(3):
            for j in range(6,9,1):
                if board[i][j] != ' ':
                    c.append(board[i][j])
                    if c.count(value)>1 or c.count(Green+str(value)+Black)==1 or c.count(Bold_Yellow+Background_Red+str(value)+Normal+Black)==1 or c.count(Bold_Yellow+Background_Red+str(value)+Normal)==1 or c.count(str(value)+Black)==1:
                        return True

    #MIDDLE LEFT:
    if 3<=row<=5 and row<=2:
        d = []
        for i in range(3,6,1):
            for j in range(3):
                if board[i][j]!=' ':
                    d.append(board[i][j])
                    if d.count(value)>1 or d.count(Green+str(value)+Black)==1 or d.count(Bold_Yellow+Background_Red+str(value)+Normal+Black)==1 or d.count(Bold_Yellow+Background_Red+str(value)+Normal)==1 or d.count(str(value)+Black)==1:
                        return True
                    
    #MIDDLE CENTER
    if 3<=row<=5 and 3<=col<=5:
        e = []
        for i in range(3,6,1):
            for j in range(3,6,1):
                if board[i][j]!=' ':
                    e.append(board[i][j])
                    if e.count(value)>1 or e.count(Green+str(value)+Black)==1 or e.count(Bold_Yellow+Background_Red+str(value)+Normal+Black)==1 or e.count(Bold_Yellow+Background_Red+str(value)+Normal)==1 or e.count(str(value)+Black)==1:
                        return True
    #MIDDLE RIGHT
    if 3<=row<=5 and col>=6:
        f = []
        for i in range(3,6,1):
            for j in range(6,9,1):
                if board[i][j]!= ' ':
                    f.append(board[i][j])
                    if f.count(value)>1 or f.count(Green+str(value)+Black)==1 or f.count(Bold_Yellow+Background_Red+str(value)+Normal+Black)==1 or f.count(Bold_Yellow+Background_Red+str(value)+Normal)==1 or f.count(str(value)+Black)==1:
                        return True
    #BOTTOM LEFT
    if row>=6 and row<=2:
        g = []
        for i in range(6,9,1):
            for j in range(3):
                if board[i][j]!=' ':
                    g.append(board[i][j])
                    if g.count(value)>1 or g.count(Green+str(value)+Black)==1 or g.count(Bold_Yellow+Background_Red+str(value)+Normal+Black)==1 or g.count(Bold_Yellow+Background_Red+str(value)+Normal)==1 or g.count(str(value)+Black)==1:
                        return True
    #BOTTOM MIDDLE
    if row>=6 and 3<=col<=5:
        h = []
        for i in range(6,9,1):
            for j in range(3,6,1):
                if board[i][j]!=' ':
                    h.append(board[i][j])
                    if h.count(value)>1 or h.count(Green+str(value)+Black)==1 or h.count(Bold_Yellow+Background_Red+str(value)+Normal+Black)==1 or h.count(Bold_Yellow+Background_Red+str(value)+Normal)==1 or h.count(str(value)+Black)==1:
                        return True
    #BOTTOM RIGHT
    if row>=6 and col>=6:
        t = []
        for i in range(6,9,1):
            for j in range(6,9,1):
                if board[i][j] != ' ':
                    t.append(board[i][j])
                    if t.count(value)>1 or t.count(Green+str(value)+Black)==1 or t.count(Bold_Yellow+Background_Red+str(value)+Normal+Black)==1 or t.count(Bold_Yellow+Background_Red+str(value)+Normal)==1 or t.count(str(value)+Black)==1:
                        return True
    
       

def all_cells_filled():
    '''Function all_cells_filled for printing success when user completes board and no more empty strings left in the 2d list'''
    for i in range(9):
        for j in range(9):
            while board[i][j] == ' ':
                board_input()
    if board[i][j]!=' ':
        return True
        

if all_cells_filled() == True:
    print(Green+'==============================================\nYou solved this Sudoku! Congratulations!!!!\n=============================================='+Normal)



#!/usr/bin/env python
# coding: utf-8

# In[1]:
def choose_symbol ():
    symbol=""   
    while symbol.upper()!="X" and symbol.upper()!="O":
        symbol=(input("Choose your symbol 'X' or 'O': ")) 
        if symbol.upper()=="X" or symbol.upper()=="O":
            break
        else:
            print("That's neither an 'X' or a 'O', try again!!")
            
    print("The player has chosen "+symbol.upper()+"!")        
    return symbol.upper()


def player_move(board,symbol):
    while True:
        try:
            position=int((input("Choose a number between '0' and '8' :")))
            if position>=0 and position<=8:
                if board[position]!=" ":
                    print("The position "+str(position)+" is already taken, try again!!")
                else:
                    board[position]=symbol
                    break
            else:
                print("The number must be between '0' and '8'!!, try again:  ")
        except ValueError:
            print("hey that's not a number, try again: ")
        
    print("The player has chosen position "+str(position)+"!")
    return board
def comp_move(board,symbol):
    from time import sleep
    from random import choice
    
    computer_list=[]
    #Adding random choice for computer move
    for i in range(len(board)):
        if board[i]==" ":
            computer_list.append(i) 
            
    computer_position=choice(computer_list)
    board[computer_position]=symbol
    print("Computer is thinking it's next random move...")
    sleep(1)
    print("The computer has chosen position "+str(computer_position)+"!")
    print_gameboard(board)
    
    return board
        
  
def print_gameboard(board):
    print(" _________________\n|     |     |     |\n|  "+board[0]+"  |  "+board[1]+"  |  "+board[2]+
      "  |\n|_____|_____|_____|\n|     |     |     |\n|  "+board[3]+"  |  "+board[4]+"  |  "+board[5]+
      "  |\n|_____|_____|_____|\n|     |     |     |\n|  "+board[6]+"  |  "+board[7]+"  |  "+board[8]+
      "  |\n|_____|_____|_____|")
    
def check_win_draw(board,p):
    Xs=0
    Os=0
    #checked player wins:
    if ((board[0]==p and board[1]==p and board[2]==p) or (board[3]==p and board[4]==p and board[5]==p) or
        (board[6]==p and board[7]==p and board[8]==p) or (board[0]==p and board[3]==p and board[6]==p) or
        (board[1]==p and board[4]==p and board[7]==p) or (board[2]==p and board[5]==p and board[8]==p) or
        (board[0]==p and board[4]==p and board[8]==p) or (board[2]==p and board[4]==p and board[6]==p)):
        return 1
    #ends in draw:   
    else:
        
        if not board.count(" ")>0:
            return 2
        
        return 0

def game_start():
    from time import sleep
    
    #Forcecheck draw:  gameboard=["O","X","X","X","X","O","O","O","X"]
    
    gameboard=[" "," "," "," "," "," "," "," "," "]
    who_starts=""
    
    print("Welcome to Tic Tac Toe, get ready to play!!")
    print("\nThis grid down here is the gameboard with each coordinate number inside of each cell, for each turn " 
          +"you are going to write down one of those numbers in order to place your next token into that cell")
    print(" _________________\n|     |     |     |\n|  "+str(0)+"  |  "+str(1)+"  |  "+str(2)+
      "  |\n|_____|_____|_____|\n|     |     |     |\n|  "+str(3)+"  |  "+str(4)+"  |  "+str(5)+
      "  |\n|_____|_____|_____|\n|     |     |     |\n|  "+str(6)+"  |  "+str(7)+"  |  "+str(8)+
      "  |\n|_____|_____|_____|")
    print("\nFake loading...")
    sleep(4)
    print("\nLet the game begin!\n")
    
    #Assigning symbols to each player:
    PlayerSymbol=choose_symbol()
    if PlayerSymbol=="X":
        ComputerSymbol="O"
    else:
        ComputerSymbol="X"
        
    #Assigning first turn:
    while True:
        who_starts=(input("Do you want to start first? y/n :"))
        
        if who_starts.lower()=="y" or who_starts.lower()=="n":
            break
        else:
            print("That's neither an 'y' or a 'n', try again!!")
    

    while(check_win_draw(gameboard,PlayerSymbol)==0 and check_win_draw(gameboard,ComputerSymbol)==0):
        if who_starts=="y":
            gameboard=player_move(gameboard,PlayerSymbol)
            print_gameboard(gameboard)
        
        if(check_win_draw(gameboard,PlayerSymbol)==0):
            
            gameboard=comp_move(gameboard,ComputerSymbol)
            who_starts="y"
            
        else:
            break
        
                
                
    if (check_win_draw(gameboard,PlayerSymbol)==1):
        print("\n\nCongratulations human!!, you have won against a random decision based opponent")
    elif(check_win_draw(gameboard,ComputerSymbol)==1):
        print("\n\nShame on you... you lost against a random decision based opponent")
    else:
        print("The game ends in Draw!")
            


# In[ ]:



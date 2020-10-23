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


def choose_position():
    position=10
    while int(position)<0 or int(position)>=8:
        try:
            position=int((input("Choose a number between '0' and '8' :")))
            if position>=0 and position<=8:
                break
            else:
                print("The number must be between '0' and '8'!!, try again:  ")
        except ValueError:
            print("hey that's not a number, try again: ")
        
    print("The player has chosen position "+str(position)+"!")
    return position
        

def change_gameboard(position,symbol,board):
    updated_board=board
    if updated_board[position]=="X" or updated_board[position]=="O":
        print("The position "+str(position)+" is already taken, try again!!")
        updated_board=change_gameboard(choose_position(),symbol,updated_board)
    else:
        updated_board[position]=symbol
    return updated_board
  
def print_gameboard(board):
    print(" _________________\n|     |     |     |\n|  "+board[0]+"  |  "+board[1]+"  |  "+board[2]+
      "  |\n|_____|_____|_____|\n|     |     |     |\n|  "+board[3]+"  |  "+board[4]+"  |  "+board[5]+
      "  |\n|_____|_____|_____|\n|     |     |     |\n|  "+board[6]+"  |  "+board[7]+"  |  "+board[8]+
      "  |\n|_____|_____|_____|")
    
def check_win_draw(board,p,c):
    Xs=0
    Os=0

    
    if board[0]==p and board[1]==p and board[2]==p:
        return 1
    elif board[3]==p and board[4]==p and board[5]==p:
        return 1
    elif board[6]==p and board[7]==p and board[8]==p:
        return 1
    elif board[0]==p and board[3]==p and board[6]==p:
        return 1
    elif board[1]==p and board[4]==p and board[7]==p:
        return 1
    elif board[2]==p and board[5]==p and board[8]==p:
        return 1
    elif board[0]==p and board[4]==p and board[8]==p:
        return 1
    elif board[2]==p and board[4]==p and board[6]==p:
        return 1
    
    elif board[0]==c and board[1]==c and board[2]==c:
        return 2
    elif board[3]==c and board[4]==c and board[5]==c:
        return 2
    elif board[6]==c and board[7]==c and board[8]==c:
        return 2
    elif board[0]==c and board[3]==c and board[6]==c:
        return 2
    elif board[1]==c and board[4]==c and board[7]==c:
        return 2
    elif board[2]==c and board[5]==c and board[8]==c:
        return 2
    elif board[0]==c and board[4]==c and board[8]==c:
        return 2
    elif board[2]==c and board[4]==c and board[6]==c:
        return 2
    
    else:
        counter=0
        for sym in board.values():
            if sym=="X" or sym=="O":
                counter+=1
            if counter==9:
                return 3
        return 0

def game_start():
    from random import choice
    from time import sleep
    
    
    gameboard={0:" ",1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" "}
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
    
    PlayerSymbol=choose_symbol()
    
    if PlayerSymbol=="X":
        ComputerSymbol="O"
    else:
        ComputerSymbol="X"
    
    while(check_win_draw(gameboard,PlayerSymbol,ComputerSymbol)==0):
        gameboard=change_gameboard(choose_position(),PlayerSymbol,gameboard)
        print_gameboard(gameboard)
        
        if(check_win_draw(gameboard,PlayerSymbol,ComputerSymbol)==0):
            computer_list=[]
            for key in gameboard.keys():
                if gameboard[key]==" ":
                    computer_list.append(key)
            
            computer_position=choice(computer_list)
            gameboard=change_gameboard(computer_position,ComputerSymbol,gameboard)
            
                
            print("Computer is thinking it's next random move...")
            sleep(1)
            print("The computer has chosen position "+str(computer_position)+"!")
            print_gameboard(gameboard)
            
        else:
            break
        
                
                
    if (check_win_draw(gameboard,PlayerSymbol,ComputerSymbol)==1):
        print("\n\nCongratulations human!!, you have won against a random decision based opponent")
    elif(check_win_draw(gameboard,PlayerSymbol,ComputerSymbol)==2):
        print("\n\nShame on you... you lost against a random decision based opponent having first turn granted")
    else:
        print("The game ends in Draw!")
            
            

      


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Tic Tac Toe Game 
# ##### Scratch Building
# ##### No GUI Required 

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output

def display_board(board):
    print (board[0],'l',board[1],'l',board[2])
    print('------------')
    print (board[3],'l',board[4],'l',board[5])
    print('------------')
    print (board[6],'l',board[7],'l',board[8])
    print('------------')


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[2]:


test_board = ['X','O','X','O','X','','X','O','X']
display_board(test_board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[3]:


def player_input():
    while True:
        player1 = input("Please pick a marker 'X' or 'O'")
        position = int(input('Please enter a number'))
        if player1 == 'X' or player1 == 'O':
            place_marker(board_Game,player1,position)
        else:
            print("chose one 'X' or 'O' only")
    pass


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[5]:


def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)
    if win_check(board,marker):
        print("\n you win {} \n".format(marker))
        return True
    pass


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[6]:


def win_check(board, mark):
    test = ['0 1 2','3 4 5','6 7 8','0 4 8','2 4 6','0 3 6','1 4 7','2 5 8']
    for i in test:
        j = i.split()
        #print(j)
        if board[int(j[0])] == board[int(j[1])] == board[int(j[2])]== mark:
            return True
    return False
    pass


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[7]:


def player_input(board,marker):
    print("player {} is start".format(marker)) 
    while True: 
        playerCh = player_choice(board)
        position = int(input('Please enter a number from {}: '.format(playerCh)))
        if position in playerCh:
            if not(place_marker(board,marker,position)):
                if marker == 'X':
                    marker = 'O'
                else:
                    marker = 'X'
            else:
                break
        else:
            continue
    pass


# In[9]:


import random 

def choose_first():
    marker = ''
    choose = random.randint(0,1)
    if choose == 0:
        marker = 'X'
    elif choose == 1:
        marker = 'O'
    return marker


# In[10]:


choose_first()


# **Step 6: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[11]:


def full_board_check(board):
    for i in board:
        if i == ' ':
            return False    
    return True
    pass


# **Step 7: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[12]:


def player_choice(board):
    board_free = []
    for i in range(0,len(board)):
        if board[i] == ' ':
            board_free.append(i)
    return board_free
    pass


# **Step 8: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[13]:


def replay():
    rep = input("play again? 'Y' or 'N'")
    if rep == 'N' or rep == 'n':
        return False
    else:
        clear_output()
        choose_first()    
    return True


# **Step 9: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[14]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    board_tests = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    # Choose Markers
    marker = choose_first()
    
    # Who Starts First 
    print(marker + ' will go first.')
    
    display_board(board_tests)
    
    player_input(board_tests,marker)
    
    if not(replay()):
        break


# ## Good Job!

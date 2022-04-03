import tkinter
from tkinter import ttk
from tkinter import messagebox

#global variables
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

curr_turn = 'X'
ctr = 1
win_ck = False

#FUNCTIONS
def click(row, col):
    global curr_turn, ctr, win_ck

    board[row][col] = curr_turn
    buttons[row][col].config( text = curr_turn, state='disabled')

    win_ck = win_check(curr_turn)

    if( ( ctr > 4 ) and  win_ck[0]  ):
        change_color_of_winning_elements()
        win_dialog_box(curr_turn)
    elif( ctr == 9 ):
        draw_dialog_box()
    else:
        if( curr_turn == 'X'):
            curr_turn = 'O'
        else:
            curr_turn ='X'

        curr_turn_lbl.config( text = curr_turn)
        ctr += 1

def change_color_of_winning_elements():
    global win_ck
    i = -1
    j = -1
    for index in range(1, 4):
        i = int(win_ck[index][0])
        j = int(win_ck[index][1])
        buttons[i][j].config(underline=0)

def draw_dialog_box():
    messagebox.showinfo(message='DRAW', detail='It is a draw.', parent=root)
    clear()

def win_dialog_box(winner):
    messagebox.showinfo( message='WINNER',detail=winner+' has won!', parent=root)
    clear()

def clear():
    global ctr
    for i in range(3):
        for j in range(3):
            board[i][j] = 0
            buttons[i][j].config(text = '', state='!disabled', underline=-1)

    ctr = 1

def win_check(check_for):
    ''' returns either [True, 'ij', 'ij', 'ij'] or [False]
        where 'ij' is string of indices of winning elements.
        Each 'ij' is different.
    '''
    bool_win = True
    result = [True]
    #check all rows
    for i in range(3):
        for j in range(3):
            if( board[i][j] != check_for):
                bool_win = False
                break
        if( bool_win ):
            for col in range(3):
                result.append( str(i) + str(col) )
            return result
        bool_win = True
    
    #check all columns
    for i in range(3):
        for j in range(3):
            if( board[j][i] != check_for):
                bool_win = False
                break
        if( bool_win ):
            for row in range(3):
                result.append( str(row) + str(i) )
            return result
        bool_win = True
    
    #check all diagonals
    for i in range(3):
        if( board[i][i] != check_for):
                bool_win = False
                break
    if( bool_win ):
        for index in range(3):
            result.append(str(index) + str(index))
        return result
    bool_win = True
    
    for i in range(3):
        if( board[i][2-i] != check_for):
                bool_win = False
                break
    if( bool_win ):
        for index in range(3):
            result.append(str(index) + str(2-index))
        return result
    
    #return false if no match found
    return [False]

#ROOT WINDOW
root = tkinter.Tk()

root.title('Tic Tac Toe')
root.resizable(False, False)

#FRAMES
content = ttk.Frame(root)
content.grid(row=0, column=0)

frame1 = ttk.Frame(content)
frame1.grid(row=0, column=0, columnspan=3)

frame2 = ttk.Frame(content)
frame2.grid(row=1, column=0)

#WIDGETS
#label
label = ttk.Label(frame1, text='Current Turn : ', font = ('arial', 25))
label.grid(row=0, column=0)

curr_turn_lbl = ttk.Label(frame1, text = curr_turn, font = ('arial', 30),
foreground='red', width=2)
curr_turn_lbl.grid(row=0, column=1)

#buttons for 'X' or 'O'
buttons =  [[0,0,0],
            [0,0,0],
            [0,0,0]]

for i in range(3):
    for j in range(3):
        buttons[i][j] = ttk.Button(frame2, width=2, text='', 
        command = lambda row=i,col=j:click(row,col))
        buttons[i][j].grid(row=i, column=j)

#STYLES
btn_style = ttk.Style()
btn_style.configure('TButton', font = ('arial', 60, 'bold'))

#EVENT LOOP
root.mainloop()
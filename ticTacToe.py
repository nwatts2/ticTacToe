import PySimpleGUI as sg
import time

blue = '#2e4053'
pink = '#e7615d'
teal = '#1d9081'
orange = '#fe864c'
purple = '#6336cf'
green = '#8ac040'
yellow = '#fcd008'

colorMenu = ['Teal', 'Pink', 'Orange', 'Purple', 'Green', 'Yellow']

p1Color = teal
p2Color = pink

titlefont = ('Arial', 32, 'bold')
buttonfont = ('Arial', 70, 'bold')
subtitlefont = ('Arial', 22, 'bold')
tablefont = 'SYSTEM_DEFAULT'
sg.set_options(font=tablefont)

def Spot(ke):
    ke = ke
    spot = sg.Button(
        button_text=ke,
        button_color=(blue, blue),
        expand_x=True,
        expand_y=True,
        p=((6, 6), (6, 6)),
        use_ttk_buttons=True,
        key = ke,
        font = buttonfont
    )
    return spot

def Column(col):
    column = sg.Column(
        layout=col,
        expand_x=True,
        expand_y=True,
        p=((0, 0), (10, 10)),
        element_justification='center'
    )
    return column

def Turn(spot):
    global turn, p1Color, p2Color
    if turn == 1 and winner == 0:
        spot.update(disabled_button_color=(p1Color, p1Color), disabled=True)
        turn = 2
    elif turn == 2 and winner == 0:
        spot.update(disabled_button_color=(p2Color, p2Color), disabled=True)
        turn = 1
    elif spot.Disabled == False:
        spot.update(disabled=True, disabled_button_color=(blue, blue))

playerTitles = sg.Text(
    text = 'Enter Player Names',
    font = titlefont,
    justification = 'center',
    background_color=blue,
    expand_x = True
)

player1 = sg.Text(
    text = 'Player 1 Name:',
    font = subtitlefont,
    expand_x = True,
    justification = 'left'
)

player2 = sg.Text(
    text = 'Player 2 Name:',
    font = subtitlefont,
    expand_x = True,
    justification = 'left'
)

input1 = sg.Input(
    default_text='Player 1',
    p = ((10,10),(10,10)),
    font = tablefont,
    focus = True
)

input2 = sg.Input(
    default_text='Player 2',
    p = ((10,10),(10,10)),
    font = tablefont
)

enter = sg.Button(
    button_text='Enter',
    button_color=blue,
    p=((6, 6), (6, 6)),
    use_ttk_buttons=True,
    font=subtitlefont,
    bind_return_key = True,
    expand_x = True,
    auto_size_button = True,
)

player1Color = sg.Text(
    text = 'Player 1 Color:',
    font = subtitlefont,
    expand_x = True,
    justification = 'left',
    key = '-P1COLOR-'
)

player2Color = sg.Text(
    text = 'Player 2 Color:',
    font = subtitlefont,
    expand_x = True,
    justification = 'left',
    key = '-P2COLOR-'
)

p1buttonMenu = sg.OptionMenu(
    default_value = 'Teal',
    values = colorMenu,
    #font = tablefont,
    expand_x = True,
    text_color = 'white',
    background_color = blue,
    p=((10, 10), (10, 10)),
    key = '-color1-'
)

p2buttonMenu = sg.OptionMenu(
    default_value = 'Pink',
    values = colorMenu,
    #font=tablefont,
    expand_x = True,
    text_color = 'white',
    background_color = blue,
    p=((10, 10), (10, 10)),
    key='-color2-'
)

nameCol1 = [
    [player1],
    [input1],
    [player2],
    [input2]
]

nameCol2 = [
    [player1Color],
    [p1buttonMenu],
    [player2Color],
    [p2buttonMenu]
]

nameColumn1 = Column(nameCol1)
nameColumn2 = Column(nameCol2)

nameLayout = [
    [playerTitles],
    [nameColumn1, nameColumn2],
    [enter]
]

nameWindow = sg.Window("Tic-Tac-Toe!", layout=nameLayout, keep_on_top=True)

while True:
    event, values = nameWindow.read()

    if event == sg.WIN_CLOSED or event == 'Enter':
        p1Name = str(input1.get())
        p2Name = str(input2.get())
        if values['-color1-'] == 'Teal': p1Color = teal
        elif values['-color1-'] == 'Pink': p1Color = pink
        elif values['-color1-'] == 'Orange': p1Color = orange
        elif values['-color1-'] == 'Purple': p1Color = purple
        elif values['-color1-'] == 'Green': p1Color = green
        elif values['-color1-'] == 'Yellow': p1Color = yellow

        if values['-color2-'] == 'Teal': p2Color = teal
        elif values['-color2-'] == 'Pink': p2Color = pink
        elif values['-color2-'] == 'Orange': p2Color = orange
        elif values['-color2-'] == 'Purple': p2Color = purple
        elif values['-color2-'] == 'Green': p2Color = green
        elif values['-color2-'] == 'Yellow': p2Color = yellow

        break

nameWindow.close()

headings = [p1Name.capitalize() + "'s Wins:", p2Name.capitalize() + "'s Wins:", "Ties:"]

leadtable = [[0,0,0]]

try:
    leaderboardFile = open('./leaderboard.txt', 'r')
except:
    print('File unreadable')
else:
    leadtable[0][0] = int(leaderboardFile.readline())
    leadtable[0][1] = int(leaderboardFile.readline())
    leadtable[0][2] = int(leaderboardFile.readline())

leaderboardFile.close()

p1wins = leadtable[0][0]
p2wins = leadtable[0][1]
ties = leadtable[0][2]

keepPlaying = True

while keepPlaying == True:
    statusMessage = "{}'s Turn"

    row1 = [10, 20, 30]
    row2 = [40, 50, 60]
    row3 = [70, 80, 90]

    turn = 1
    winner = 0

    title = sg.Text(
        text="Tic-Tac-Toe",
        text_color='white',
        font=titlefont,
        justification='center',
        expand_x=True,
        background_color=blue,
        grab=True
    )

    status = sg.Text(
        text=statusMessage.format(p1Name),
        text_color='white',
        font=titlefont,
        justification='center',
        expand_x=True,
        background_color=blue,
    )

    gameOver = sg.Text(
        text='Would you like to play again?',
        text_color='white',
        font=subtitlefont,
        justification='center',
        expand_x=True,
        # background_color = blue,
    )

    playagain = sg.Button(
        button_text='Play Again',
        button_color=blue,
        expand_x=True,
        expand_y=True,
        p=((6, 6), (6, 6)),
        use_ttk_buttons=True,
        font=subtitlefont
    )

    quit = sg.Button(
        button_text='Quit',
        button_color=blue,
        expand_x=True,
        expand_y=True,
        p=((6, 6), (6, 6)),
        use_ttk_buttons=True,
        font=subtitlefont
    )

    leaderboardTitle = sg.Text(
        text='Leaderboard',
        text_color='white',
        font=titlefont,
        justification='center',
        expand_x=True,
        background_color = blue,
        grab = True
    )

    spot1 = Spot('1')
    spot2 = Spot('2')
    spot3 = Spot('3')
    spot4 = Spot('4')
    spot5 = Spot('5')
    spot6 = Spot('6')
    spot7 = Spot('7')
    spot8 = Spot('8')
    spot9 = Spot('9')

    col1 = [
        [spot1],
        [spot4],
        [spot7]
    ]

    col2 = [
        [spot2],
        [spot5],
        [spot8]
    ]

    col3 = [
        [spot3],
        [spot6],
        [spot9]
    ]

    column1 = Column(col1)
    column2 = Column(col2)
    column3 = Column(col3)

    gamelayout = [
        [title],
        [column1, column2, column3],
        [status]
    ]

    window = sg.Window("Tic-Tac-Toe!", layout=gamelayout, keep_on_top=True, size=(600, 650))

    while winner == 0:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            keepPlaying = False
            break
        elif event == '1':
            row1[0] = turn
            Turn(spot1)
        elif event == '2':
            row1[1] = turn
            Turn(spot2)
        elif event == '3':
            row1[2] = turn
            Turn(spot3)
        elif event == '4':
            row2[0] = turn
            Turn(spot4)
        elif event == '5':
            row2[1] = turn
            Turn(spot5)
        elif event == '6':
            row2[2] = turn
            Turn(spot6)
        elif event == '7':
            row3[0] = turn
            Turn(spot7)
        elif event == '8':
            row3[1] = turn
            Turn(spot8)
        elif event == '9':
            row3[2] = turn
            Turn(spot9)

        if turn == 1:
            status.update(value=statusMessage.format(p1Name))
        else:
            status.update(value=statusMessage.format(p2Name))

        if row1[0] == row1[1] == row1[2]:
            winner = row1[0]
        elif row2[0] == row2[1] == row2[2]:
            winner = row2[0]
        elif row3[0] == row3[1] == row3[2]:
            winner = row3[0]
        elif row1[0] == row2[0] == row3[0]:
            winner = row1[0]
        elif row1[1] == row2[1] == row3[1]:
            winner = row1[1]
        elif row1[2] == row2[2] == row3[2]:
            winner = row1[2]
        elif row1[0] == row2[1] == row3[2]:
            winner = row2[1]
        elif row1[2] == row2[1] == row3[0]:
            winner = row2[1]
        elif spot1.Disabled and spot2.Disabled and spot3.Disabled and spot4.Disabled and spot5.Disabled and spot6.Disabled and spot7.Disabled and spot8.Disabled and spot9.Disabled:
            winner = 3
    else:
        if winner == 1 or winner == 2:

            if winner == 1:
                p1wins += 1
                status.update(value="{} Wins!".format(p1Name))
            else:
                p2wins += 1
                status.update(value="{} Wins!".format(p2Name))

            Turn(spot1)
            Turn(spot2)
            Turn(spot3)
            Turn(spot4)
            Turn(spot5)
            Turn(spot6)
            Turn(spot7)
            Turn(spot8)
            Turn(spot9)
        else:
            status.update(value="It's a Tie!")
            ties += 1

        leadtable = [[p1wins, p2wins, ties]]

        table = sg.Table(
            values=leadtable,
            headings=headings,
            auto_size_columns=True,
            p=((10, 10), (10, 10)),
            font=tablefont,
            num_rows=1,
            expand_x=True,
            justification='center',
            hide_vertical_scroll=True,
            background_color='white',
            text_color='black'
        )

        menulayout = [
            [leaderboardTitle],
            [table],
            [gameOver],
            [playagain, quit]
        ]

        endWindow = sg.Window('Game Over!', layout=menulayout, keep_on_top=True, modal=True)

        while True:
            event, values = endWindow.read()
            if event == sg.WIN_CLOSED:
                keepPlaying = False
                break
            elif event == 'Quit':
                keepPlaying = False
                leaderboardFile = open('./leaderboard.txt', 'w')
                leaderboardFile.write('{}\n{}\n{}'.format(leadtable[0][0], leadtable[0][1], leadtable[0][2]))
                leaderboardFile.close()
                endWindow.close()
                break
            elif event == 'Play Again':
                endWindow.close()
                break
    window.close()
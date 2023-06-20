import os

#I did not write this |
#                     v

def resource_path(relative_path):

    base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#--------------------------------------------------

piece = resource_path("piece.gif")
backSplash = resource_path("backsplash.gif")
holdShape = resource_path("hold.gif")


def play():
    import turtle, time, random, os
    global mode, linesCleared, noHeld, holdShape, piece, itBeforeUpdate, pieceX, pieceY, it, bag, score, pieceFound, pen, piecesDraw, o, jay, l, z, s, long, t, boardY, boardX, oldBoard, scrX, scrY, board, altBoard, rotation, activePiece, playing, pieceFalling, delAmnt, win, pen, im, zoomNo, intersection
    o = [[
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
            ],
        [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
            ],
        [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
            ],
        [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
            ]

    ]

    jay = [
        [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
            ],

        [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
            ],

        [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 0]
            ],

        [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
            ]
        ]

    l = [
        [[0, 0, 0, 0],
         [0, 0, 1, 0],
         [1, 1, 1, 0],
         [0, 0, 0, 0]
            ],

        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 1, 0]
            ],

        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 0],
         [1, 0, 0, 0]
            ],

        [[0, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0]
        ]

    ]

    z = [
        [[0, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]

         ],

        [[0, 0, 0, 0],
         [0, 0, 1, 0],
         [0, 1, 1, 0],
         [0, 1, 0, 0]
            ],

        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 1, 0]
            ],

        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0],
         [1, 0, 0, 0]
        ]

    ]

    s = [
        [[0, 0, 0, 0],
         [0, 1, 1, 0],
         [1, 1, 0, 0],
         [0, 0, 0, 0]

         ],

        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 0]
         ],



        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 1, 1, 0],
         [1, 1, 0, 0]
            ],

        [[0, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0]
            ],

    ]

    long = [
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 0]
            ],

        [[0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0]
            ],

        [[0, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]
            ],

        [[0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0]
        ]

    ]

    t = [
        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 1, 0],
         [0, 0, 0, 0]
            ],

        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 1, 0, 0]
            ],

        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 0],
         [0, 1, 0, 0]
            ],

        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0]
        ]

    ]

    #Functions

    def newBoard(b):
        global boardX, boardY, it
        for i in range(boardY):
            b.append([])
            for j in range(boardX):
                b[i].append(0)
        return

    def newPiece():
        global didC, pieceFalling, board, boardX, boardY, pieceX, pieceY, activePiece, piecesDraw, rotation, o, long, l, jay, z, s, t, playing, piecesDraw, bag, pieceFound, oldHeld
        didC = False
        pieceFound = random.randint(0, 6)
        activePiece = []

        if pieceX == 3 and pieceY == 0 and pieceReq is False:
            restart()
            return
        if piecesDraw == len(bag):
            piecesDraw = 0
        if piecesDraw == 0:
            bag = []
            for i in range(0, 7):
                bag.append(i)
            random.shuffle(bag)
        pieceFound = bag[piecesDraw]
        if pieceReq is False:
            piecesDraw += 1
        if pieceFound == 0:
            writePiece = o

        if pieceFound == 1:
            writePiece = long

        if pieceFound == 2:
            writePiece = l

        if pieceFound == 3:
            writePiece = jay

        if pieceFound == 4:
            writePiece = z

        if pieceFound == 5:
            writePiece = s

        if pieceFound == 6:
            writePiece = t

        for c in range(0, len(writePiece)):
            activePiece.append(writePiece[c])

        pieceX = 3
        pieceY = 0
        rotation = 0
        pieceFalling = True
        return

    def crossCheck(yVar, xVar, rot):
        global intersection, boardY, boardX, pieceX
        intersection = False
        for i in range(0, 4):
            for j in range(0, 4):
                if activePiece[rotation + rot][i][j] == 1:
                    if i + pieceY + yVar >= boardY or j + pieceX + xVar >= boardX or pieceX + xVar + j < 0:
                        intersection = True
                    elif board[i + pieceY + yVar][j + pieceX + xVar] > 0:
                        intersection = True
                    elif i + pieceY + yVar < 0:
                        intersection = True
        return

    def printBoard():
        global boardX, boardY, board, rotation, pieceX, pieceY, oldBoard, altBoard, noHeld, dp
        altBoard = []

        for i in range(0, boardY):
            altBoard.append([])
            for j in range(0, boardX):
                altBoard[i].append(board[i][j])
        for i in range(0, 4):
            for j in range(0, 4):
                if activePiece[rotation][i][j] == 1:
                    altBoard[i + pieceY][j + pieceX] = 1

        turtleScreenDraw(board)
        oldBoard = []
        for i in range(0, boardY):
            oldBoard.append(altBoard[i])
        if noHeld is not False:
            drawHold()

        return

    def downCheck():
        global intersection, rotation, pieceFalling, pieceY, pieceX, pieceFound, board, linesCleared, delAmnt, score
        intersection = False

        crossCheck(1, 0, 0)
        if intersection is True:
            for i in range(0, 4):
                for j in range(0, 4):
                    if activePiece[rotation][i][j] == 1:
                        board[i + pieceY][j + pieceX] = pieceFound + 1
            pieceFalling = False
            for i in range(0, boardY):
                if 0 not in board[i]:
                    del board[i]
                    delAmnt += 1
                    score += 1
                    board.insert(0, [])
                    for j in range(0, boardX):
                        board[0].append(0)
        else:
            pieceY += 1

        printBoard()
        return

    def turnTest(r, x):
        global rotation, pieceX, pieceY, board, activePiece, boardX, intersection

        intersection = True
        oar = r
        if r == 1 and rotation == 3:
            r = -3
        elif r == 2 and rotation >= 2:
            r = -2
        elif r == -1 and rotation == 0:
            r = 3

        y = 0

        order = [[0, 1, 2, -1, -2]]

        if oar == 1:
            order.append([0, -1, 1])
            order.append("r")
        elif oar == -1:
            order.append([0, 1, -1])
            order.append("l")
        else:
            order.append([0, -1, 1])
            order.append("n")
        
        crossCheck(0, x, r)
        if r != 0 and intersection is True:
            for i in range(0, 5):
                for j in range(0, 3):
                    i = order[0][i]
                    j = order[1][j]
                    crossCheck(i, j, r)
                    if intersection is False:
                        break
                if intersection is False:
                    break
            y = i
            x = j

        if intersection is False:
            rotation += r
            pieceX += x
            pieceY += y
        printBoard()

        return

    def turtleScreenDraw(b):
        global boardY, boardX, scrX, scrY, pen, board, oldBoard, pieceFound, c, it, itBeforeUpdate, noHeld, mode
        timesRun = 0
        for i in range(0, boardY):
            for j in range(0, boardX):
                # Use sRx and sRy
                if oldBoard[i][j] != b[i][j] or itBeforeUpdate == 0:
                    pen.shape("square")
                    cUsed = False
                    if b[i][j] == 0:
                        if mode == "normal":
                            pen.color("black")
                        elif mode == "old":
                            pen.color("skyblue")
                    else:
                        penColorLookup(board[i][j])
                        pen.color(c)
                        cUsed = True
                        # pen.shape(im)
                    x = j * zoomNo - scrX * 0.44
                    y = i * zoomNo - scrY * 0.46
                    pen.goto(x, -y)
                    pen.stamp()
                    if cUsed is True and mode == "normal":
                        pen.shape(im)
                        pen.stamp()
                        pen.shape("square")
        if len(activePiece) > 3:
            for i in range(0, 4):
                for j in range(0, 4):
                    if activePiece[rotation][i][j] > 0:
                        if mode == "normal":
                            penColorLookup(pieceFound + 1)
                        elif mode == "old":
                            c = "black"
                        pen.color(c)
                        x = (j + pieceX) * zoomNo - scrX * 0.44
                        y = (i + pieceY) * zoomNo - scrY * 0.46
                        pen.goto(x, -y)
                        pen.stamp()
                        if mode == "normal":
                            pen.shape(im)
                            pen.stamp()
                        pen.shape("square")
        drawHold()
        if noHeld is not False:
            for i in range(0, 4):
                for j in range(0, 4):
                    if dp[0][i][j] == 1:
                        x = (j) * zoomNo - scrX * 0.44
                        y = (20 - i) * zoomNo - scrY * 0.46
                        holdPen.goto(x, y)
                        holdPen.stamp()
        return

    def clockwise():
        turnTest(1, 0)
        return

    def counterClockwise():
        turnTest(-1, 0)
        return

    def doubleTurn():
        turnTest(2, 0)
        return

    def right():
        turnTest(0, 1)
        return

    def left():
        turnTest(0, -1)
        return

    def down():
        global intersection, it
        crossCheck(1, 0, 0)
        if intersection is False:
            downCheck()
            printBoard()
            it = 0
        return

    def instaDrop():
        global pieceY, intersection, board, pieceFalling
        downCheck()
        if intersection is False:
            while pieceFalling is True and intersection is False:
                downCheck()
        newPiece()
        printBoard()
        return

    def leave():
        global playing
        playing = False
        win.clear()
        startScreen()
        return

    def restart():
        global board, bag, noHeld, oldBoard, activePiece, pieceX, pieceY, playing, pieceFalling, rotation, intersection, it, piecesDraw, oldBoard, boardX, boardY, delAmnt, score, noHeld
        oldBoard = []
        activePiece = []
        board = []
        boardX = 10
        boardY = 20

        pieceX = 0
        pieceY = 0
        piecesDraw = 0

        delAmnt = 0

        playing = True
        pieceFalling = False

        score = 0

        rotation = 0

        didC = False

        bag = []

        intersection = False

        it = 0
        oldBoard = []

        noHeld = False

        for i in range(0, boardY):
            oldBoard.append([])
            for j in range(0, boardX):
                oldBoard[i].append("z")

        # while playing is True:
        newBoard(board)
        
        newPiece()
        printBoard()
        time.sleep(1)
        return

    def penColorLookup(no):
        global c, mode
        if mode == "normal":
            if no == 1:
                c = "yellow"
            if no == 2:
                c = "cyan"
            if no == 3:
                c = "orange"
            if no == 4:
                c = "blue"
            if no == 5:
                c = "red"
            if no == 6:
                c = "lime"
            if no == 7:
                c = "DarkOrchid2"
        elif mode == "old":
            if 7 >= no >= 1:
                c = "grey11"
        return

    def hold():
        global activePiece, pieceFound, noHeld, pieceReq, oldHeld, bag, piecesDraw, pieceX, didC
        holdPen.clear()
        if didC is False:
            pieceReq = True

            if noHeld is False:
                noHeld = bag[piecesDraw - 1]
                #del bag[piecesDraw]
            else:
                bag[piecesDraw - 1] = noHeld
                oldHeld = noHeld
                bag.insert(piecesDraw, oldHeld)
            noHeld = pieceFound
            pieceX = 1000
            newPiece()
            printBoard()

            pieceReq = False

            didC = True
        return

    def drawHold():
        global noHeld, o, long, l, jay, z, s, t, dp
        if noHeld == 0:
            dp = o

        if noHeld == 1:
            dp = long

        if noHeld == 2:
            dp = l

        if noHeld == 3:
            dp = jay

        if noHeld == 4:
            dp = z

        if noHeld == 5:
            dp = s

        if noHeld == 6:
            dp = t



        return

    #Variables

    oldBoard = []
    activePiece = []
    board = []
    boardX = 10
    boardY = 20


    piecesDraw = 0

    pieceX = 0
    pieceY = 0

    playing = True
    pieceFalling = False

    rotation = 0

    pieceReq = False

    intersection = False

    pieceFound = 0

    it = 0

    bag = []

    score = 0

    didC = False

    linesCleared = 0

    noHeld = False

    delAmnt = 0

    #Turtles
    scrX = 350
    scrY = 700


    zoomNo = 33.5


    win = turtle.Screen()
    if mode == "normal":
        win.bgcolor("black")
    else:
        win.bgcolor("skyblue")

    win.tracer(False)
    turtle.setup(scrX, scrY)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.turtlesize(zoomNo * 0.05)
    pen.penup()
    pen.shape("square")
    pen.color("red")
    pen.pencolor("white")
    scoreWrite = turtle.Turtle()
    scoreWrite.hideturtle()
    scoreWrite.pencolor("white")
    scoreWrite.goto(150, 300)

    win.addshape(holdShape)
    holdPen = turtle.Turtle()
    holdPen.hideturtle()
    holdPen.speed(0)
    holdPen.penup()
    holdPen.shape(holdShape)


    #images
    im = piece
    win.addshape(im)

    #Starting up
    newPiece()
    newBoard(board)

    for i in range(0, boardY):
        oldBoard.append([])
        for j in range(0, boardX):
            oldBoard[i].append("z")

    # while playing is True:
    turtleScreenDraw(board)

    #listening

    win.listen()
    win.onkeypress(clockwise, "Up")
    win.onkeypress(counterClockwise, "z")
    win.onkeypress(doubleTurn, "a")
    win.onkeypress(left, "Left")
    win.onkeypress(right, "Right")
    win.onkeypress(down, "Down")
    win.onkeypress(instaDrop, "space")
    win.onkeypress(leave, "q")
    win.onkeypress(restart, "r")
    win.onkeypress(hold, "c")




    #Frame rate setup
    FPS = 15
    refreshAt = 1/FPS
    startOfInterval = time.time()

    fullUpdateDelay = 1
    itBeforeUpdate = 0

    #Main Program

    prevUpdate = time.time
    while playing is True:
        endOfInterval = time.time()

        if endOfInterval - startOfInterval >= refreshAt:

            if linesCleared == 40:
                playing = False

            if pieceFalling is False:
                newPiece()


            if it >= 30:
                it = 0
                downCheck()
                


            itBeforeUpdate += 1
            if itBeforeUpdate >= FPS * fullUpdateDelay:
                pen.clear()
                holdPen.clear()
                itBeforeUpdate = 0
                printBoard()
                            
            win.update()
            it += 1
            delAmnt = 0



            startOfInterval = time.time()
            scoreWrite.clear()
            scoreWrite.write(str(score), False, align="right", font=("arial", 25, "bold")) 
    return




def startScreen():
    import turtle, time, os
    global backSplash
    def newButton(p, x, y, h, txt, txtSize, font, clr1, clr2, ULL, tip):
        p.penup()
        p.goto(x, y + h)
        p.pendown()
        p.pencolor(clr1)
        p.pensize(1)
        if ULL != 0:
            p.fillcolor(clr1)
            p.begin_fill()
            p.goto(-x, y + h)
            p.goto(-x, -y + h)
            p.goto(x, -y + h)
            p.goto(x, y + h)
            p.end_fill()
        p.penup()
        p.goto(x - ULL * 3, h - (txtSize))
        p.pencolor(clr2)
        p.write(txt, False, align=("right"), font=(font, txtSize, "bold"))
        if ULL != 0:
            p.goto(-x, -y + h)
            p.pendown()
            p.fillcolor(clr2)
            p.begin_fill()
            p.goto(-x, -y + h + ULL)
            p.goto(x, -y + h + ULL)
            p.goto(x, -y + h)
            p.goto(-x, -y + h)
            p.end_fill()
        p.penup()
        p.goto(x * 0.5, h - y - txtSize / 2.5)
        p.write(tip, False, align=("center"), font=(font, int(txtSize / 5), "bold"))
        return

    def mouseClicked(x, y):
        global mode
        if -50 <= y <= 50:
            pen.clear()
            mode = "normal"
            play()
        elif -200 <= y <= -100:
            pen.clear()
            mode = "old"
            play()
        return

    win = turtle.Screen()
    win.title("TETRIS")
    win.bgcolor("grey11")
    win.tracer(False)
    turtle.setup(800, 550)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    im = backSplash
    win.addshape(im)
    pen.penup()
    pen.shape(im)
    pen.goto(0, 200)
    pen.stamp()


    newButton(pen, 200, 50, 200, "TETRIS", 125, "gill sans", "grey11", "white", 0, "")

    pen.goto(-225, 95)
    pen.write("-- Mark .T", False, align=("center"), font=("arial", int(50 / 5), "bold"))

    newButton(pen, 400, 50, 0, "NORMAL MODE", 50, "arial", "dark blue", "cadetBlue1", 5, "(Basic TETRIS)")
    newButton(pen, 400, 50, -150, "MONO MODE", 50, "arial", "red3", "orchid1", 5, "(Old Colors)")




    win.update()

    win.listen()
    win.onscreenclick(mouseClicked)

    win.mainloop()
startScreen()

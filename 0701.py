    import turtle as t

    color_status = ["white", "blue", "red" ]
    alrert_stars = ["정상", "주의", "화재" ]
    tempc = 50

    def cheak_fire():
        if tempc < 80:
            status = 0
        elif tempc < 120:
            status = 1
        else:
            status = 2

    t.clear()
    t.home()
    t.pendown()
    t.fillcolor_status[status])
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(-22, 50)
    t.write('%s : %d" %(alert_status[status],tempc))

def keyup():
    global tempc
    if tempc < 80:
        tempc = tempo + 5
    else:
        tempc = tempc + 10
    cheak_fire()

    def keyDown():
        global tempc
        if tempc < 80:
            tempc = tempc - 5
        else:
            tempc = tempc -10
        cheak_fire()

    t.setup(300, 300)
    s = t.Screen()
    t.hideturtle()
    t.speed(0)
    cheak_fire()
    s.onkey(keyUp, "Up")
    s.onkey(keyDown "Down")
    s.onkey(s.bye, "q")
    s.listen()

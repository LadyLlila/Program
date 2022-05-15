import turtle

#=====|| Ventana ||================
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#=====|| Marcador ||===============
marcadorA = 0
marcadorB = 0

#=====|| Jugador A ||===============
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("green")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

#=====|| Jugador B ||===============
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("green")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

#=====|| Pelota ||===============
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("green")
pelota.penup()
pelota.goto(0,0)

#Modificar estas variables para cambiar la velocidad de la pelota
pelota.dx = 0.2
pelota.dy = 0.2

#pen para dibujar el marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #======| ¿qué onda??????????????????????
pen.goto(0, 260)
pen.write("Jugador A: 0     Jugador B: 0", align="center", font=("Courier", 25, "normal"))

#=====|| Funciones ||===========
def jugadorA_up():
    y = jugadorA.ycor()#==== ¿qué onda?????????????
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety()

def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety()

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

#=======|| Teclado ||=========
wn.listen() #============ Supongo que esto "mantiene" la ventana
wn.onkeypress(jugadorA_up(), "w")
wn.onkeypress(jugadorA_down(), "s")
wn.onkeypress(jugadorB_up(), "Up")
wn.onkeypress(jugadorB_down(), "Down")

while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
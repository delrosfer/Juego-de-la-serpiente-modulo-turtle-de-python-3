import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#preparando la pantalla
ventana = turtle.Screen()
ventana.title("Juego de la Serpiente con Python y Turtle")
ventana.bgcolor("blue")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#comida de serpiente
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Puntuación: 0  Puntuación más alta: 0", align="center", font=("Arial", 20, "normal"))


# Funciones
def go_up():
	if head.direction != "down":
		head.direction="up"

def go_down():
	if head.direction != "up":
		head.direction="down"

def go_left():
	if head.direction != "right":
		head.direction="left"

def go_right():
	if head.direction != "left":
		head.direction="right"

def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y+20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y-20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x-20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x+20)

#keyboards bindings
ventana.listen()
ventana.onkeypress(go_up, "Up")
ventana.onkeypress(go_down, "Down")
ventana.onkeypress(go_left, "Left")
ventana.onkeypress(go_right, "Right")

#main game loop
while True:
	ventana.update()

	#checar para la colision con el border
	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"

		#ocultar los segmentos
		for segment in segments:
			segment.goto(1000, 1000)

		#limpiar la lista de segmentos
		segments.clear()

		#resetear el score
		score = 0

		#resetear el delay
		delay = 0.1

		pen.clear()
		pen.write("Puntuación: {}  Puntuación más alta: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))

	#checar para una colision con la comida

	if head.distance(food) <20:
		#mover comida a una posicion aleatoria
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food.goto(x,y)

		#agregar un segmento
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("circle")
		new_segment.color("orange")
		new_segment.penup()
		segments.append(new_segment)

		#Shorten the delay
		delay -= 0.001

		#incrementar el score
		score += 10

		if score > high_score:
			high_score = score

		pen.clear()
		pen.write("Puntuación: {}  Puntuación más alta: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))

	#mover el segmento al final en orden reversivo
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)

	#mover segmento 0 a donde esta la cabeza
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	move()

	#checar colision de la cabeza con los segmentos
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction = "stop"

			#ocultar los segmentos
			for segment in segments:
				segment.goto(1000, 1000)

		#limpiar la lista de segmentos
			segments.clear()

			#resetear el score
			score = 0

			#resetear el delay
			delay = 0.1

		#actualizar el score display
			pen.clear()
			pen.write("Puntuación: {}  Puntuación mas alta: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))

	time.sleep(delay)


ventana.mainloop()
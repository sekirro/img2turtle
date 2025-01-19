import turtle

def canva_init(width=800, height=600):
    # 初始化画布大小为800x600，并将窗口左上角设置在屏幕正中心
    turtle.setup(width, height)
    pen = turtle.Turtle()
    turtle.colormode(255)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.delay(0)
    turtle.tracer(2000,100)
    return pen
def draw_pixel(x, y, color, pen):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.pencolor(color)  # 设置画笔颜色
    # print(color)
    size = 5
    pen.dot(size, color)

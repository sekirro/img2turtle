import pygame
import sys

# 设置全局常量
WINDOW_SIZE = 480
GRID_SIZE = 40
CELL_SIZE = WINDOW_SIZE // GRID_SIZE

# 初始化Pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# 创建网格
grid = [[(255, 255, 255) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
color = (13, 231, 4)

with open('test.py', 'w+', encoding='utf-8') as f:
    f.write("")

with open('test.py', 'a+', encoding='utf-8') as f:
    f.write(
        f'''import turtle

# 初始化Turtle
turtle_screen = turtle.Screen()
turtle_screen.setup(500, 500)
turtle_screen.setworldcoordinates(0, 0, 500, 500)
turtle_screen.colormode(255)
turtle_pen = turtle.Turtle()
turtle_pen.speed(0)
turtle_pen.penup()
turtle_pen.hideturtle()
color = (13, 231, 4)
# 绘制实心矩形
def draw_rectangle(x, y, width, height, color):
    turtle_pen.goto(x, y)
    turtle_pen.color(color)
    turtle_pen.begin_fill()
    for _ in range(2):
        turtle_pen.forward(width)
        turtle_pen.right(90)
  
        turtle_pen.forward(height)
        turtle_pen.right(90)
    turtle_pen.end_fill()
'''
    )


def change_color():
    global color
    color = eval(input("颜色输入rgb，例(255,255,0)\n"))
    with open('test.py', 'a+', encoding='utf-8') as f:
        f.write(
            f'''color = {color}
'''
        )


# 游戏循环
while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('test.py','a+',encoding='utf-8') as f:
                f.write('''
turtle.mainloop()''')
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
            with open('test.py', 'a+', encoding='utf-8') as f:
                f.write(
                    f'''draw_rectangle({grid_x * CELL_SIZE}, {480 - grid_y * CELL_SIZE}, 12, 12,color)
'''
                )
            # 这里的颜色是硬编码的，后续我们会增加一个颜色输入框以动态改变颜色
            grid[grid_x][grid_y] = color
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 检测空格键按下事件
                change_color()  # 触发函数

    # 清除屏幕
    screen.fill((255, 255, 255))


    # 绘制网格
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[i][j],
                             pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # 绘制网格线
    for i in range(GRID_SIZE + 1):
        pygame.draw.line(screen, (200, 200, 200), (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE))

    for j in range(GRID_SIZE + 1):
        pygame.draw.line(screen, (200, 200, 200), (0, j * CELL_SIZE), (WINDOW_SIZE, j * CELL_SIZE))

    # 更新屏幕
    pygame.display.flip()
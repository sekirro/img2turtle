from img_read import img2xyc
from turtle_process import canva_init,draw_pixel
pen = canva_init(240,240)
txt = '''from turtle_process import canva_init,draw_pixel
import turtle
pen = canva_init(240,240)'''
def m2s(inp):
    tup = ()
    for i in inp:
        temp = i//16
        tup+=(temp*16,)
    return tup
for i in img2xyc():
    loc,col = i
    col = m2s(col)
    x,y = loc
    if col==(240,240,240):
        continue
    txt+=f'''
draw_pixel({x},{y},{col},pen)'''
    draw_pixel(x,y,col,pen)
with open('test.py','w+',encoding='utf-8') as f:
    txt+='''
turtle.mainloop()'''
    f.write(txt)
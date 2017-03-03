import turtle;
from square import draw_square;
from triangle import *;
from circle import draw_circle;
from config import *;


window = turtle.Screen();
window.screensize(canvwidth=500, canvheight=500, bg="black");

pencil = turtle.Turtle();

configPencil(pencil, 0);

for x in range(37):
    draw_square(pencil, 300, 90);
    pencil.right(10);


window.exitonclick();
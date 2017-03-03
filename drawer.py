import turtle;
from square import draw_square;
from triangle import *;
from circle import draw_circle;
from config import *;

window = turtle.Screen();
window.screensize(canvwidth=500, canvheight=500, bg="black");

pencil = turtle.Turtle();

configPencil(pencil, 6);

draw_square(pencil, 300, 90);

pencil.fd(150);
draw_circle(pencil,150);

moveTurtleBeforeTriangle(pencil, 300, 90);

pencil.left(116.5);
draw_triangle(pencil, 335, 116.5);

window.exitonclick();
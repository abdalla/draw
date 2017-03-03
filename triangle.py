def draw_triangle(pencil, size, angle):
    for x in range(3):
        if(x == 1):
            pencil.fd(size - 35);
        else:
            pencil.fd(size);

        pencil.right(angle);

def moveTurtleBeforeTriangle(pencil, size, angle):
    pencil.fd(size/2);
    pencil.left(angle);
    pencil.fd(size);
    pencil.left(angle);
    pencil.fd(size/2);
def draw_square(pencil, size, angle):
    for x in range(4):
        pencil.fd(size);
        pencil.left(angle);
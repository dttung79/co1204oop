from w8_shape import Shape
from w8_rect import Rectangle
from w8_circle import Circle
from w8_square import Square


def run():
    r1 = Rectangle("ABCD", 3, 4)
    c1 = Circle("O", 5)
    s1 = Square("MNPQ", 5)

    shapes = [r1, c1, s1]

    for s in shapes:
        print(s)


if __name__ == "__main__":
    run()
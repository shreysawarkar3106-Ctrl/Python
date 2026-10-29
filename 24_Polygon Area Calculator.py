class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height*self.width
    
    def get_perimeter(self):
        return 2*(self.height + self.width)

    def get_diagonal(self):
        return (self.height**2+self.width**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        pic = ''
        for n in range(self.height):
            for m in range(self.width):
                pic += '*'
            pic += '\n'
        return pic

    def get_amount_inside(self, shape):
        return (self.height//shape.height)*(self.width//shape.width)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
    
    def set_width(self, width):
        super().__init__(width,width)

    def set_height(self, height):
        super().__init__(height,height)

    def set_side(self, side):
        super().__init__(side,side)

    def __str__(self):
        return f'Square(side={self.height})'

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
"""FCC SCP #4 — Polygon Area Calculator (Rectangle + Square)."""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, w): self.width = w
    def set_height(self, h): self.height = h
    def get_area(self): return self.width * self.height
    def get_perimeter(self): return 2 * (self.width + self.height)
    def get_diagonal(self): return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return "\n".join("*" * self.width for _ in range(self.height)) + "\n"

    def get_amount_inside(self, other):
        return (self.width // other.width) * (self.height // other.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, s):
        self.width = s
        self.height = s

    def set_width(self, w): self.set_side(w)
    def set_height(self, h): self.set_side(h)

    def __str__(self):
        return f"Square(side={self.width})"

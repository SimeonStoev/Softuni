def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    rect_area = area()
    rect_perim = perimeter()

    return f"Rectangle area: {rect_area}\nRectangle perimeter: {rect_perim}"

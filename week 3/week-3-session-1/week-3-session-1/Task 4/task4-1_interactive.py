# Interactive Area Calculator
# CHALLENGE VERSION - allows users to enter their own shape and dimensions

import math

def get_float_input(prompt):
    """Get a valid float input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def calculate_area(shape, dimensions):
    """Calculate area based on shape and dimensions"""
    match shape.lower():
        case "circle":
            radius = dimensions[0]
            area = math.pi * radius ** 2
            print(f"The area of the circle with radius {radius} is {area:.2f}")
            
        case "rectangle":
            width, height = dimensions
            area = width * height
            print(f"The area of the rectangle with width {width} and height {height} is {area:.2f}")
            
        case "triangle":
            base, height = dimensions
            area = 0.5 * base * height
            print(f"The area of the triangle with base {base} and height {height} is {area:.2f}")
            
        case "square":
            side = dimensions[0]
            area = side * side
            print(f"The area of the square with side {side} is {area:.2f}")
            
        case "trapezoid":
            top_base, bottom_base, height = dimensions
            area = 0.5 * (top_base + bottom_base) * height
            print(f"The area of the trapezoid with top base {top_base}, bottom base {bottom_base} and height {height} is {area:.2f}")
            
        case "rhombus":
            diagonal1, diagonal2 = dimensions
            area = 0.5 * diagonal1 * diagonal2
            print(f"The area of the rhombus with diagonals {diagonal1} and {diagonal2} is {area:.2f}")
            
        case "ellipse":
            a, b = dimensions  # semi-major and semi-minor axes
            area = math.pi * a * b
            print(f"The area of the ellipse with semi-major axis {a} and semi-minor axis {b} is {area:.2f}")
            
        case "parallelogram":
            base, height = dimensions
            area = base * height
            print(f"The area of the parallelogram with base {base} and height {height} is {area:.2f}")
            
        case _:
            print("Sorry, I don't know how to calculate the area for that shape.")
            return False
    return True

def get_dimensions_for_shape(shape):
    """Get the required dimensions for a given shape"""
    shape = shape.lower()
    
    if shape == "circle":
        radius = get_float_input("Enter the radius: ")
        return [radius]
        
    elif shape == "rectangle":
        width = get_float_input("Enter the width: ")
        height = get_float_input("Enter the height: ")
        return [width, height]
        
    elif shape == "triangle":
        base = get_float_input("Enter the base: ")
        height = get_float_input("Enter the height: ")
        return [base, height]
        
    elif shape == "square":
        side = get_float_input("Enter the side length: ")
        return [side]
        
    elif shape == "trapezoid":
        top_base = get_float_input("Enter the top base length: ")
        bottom_base = get_float_input("Enter the bottom base length: ")
        height = get_float_input("Enter the height: ")
        return [top_base, bottom_base, height]
        
    elif shape == "rhombus":
        diagonal1 = get_float_input("Enter the first diagonal: ")
        diagonal2 = get_float_input("Enter the second diagonal: ")
        return [diagonal1, diagonal2]
        
    elif shape == "ellipse":
        a = get_float_input("Enter the semi-major axis: ")
        b = get_float_input("Enter the semi-minor axis: ")
        return [a, b]
        
    elif shape == "parallelogram":
        base = get_float_input("Enter the base: ")
        height = get_float_input("Enter the height: ")
        return [base, height]
        
    else:
        return None

def main():
    """Main interactive program"""
    print("=== Interactive Area Calculator ===")
    print("Available shapes: circle, rectangle, triangle, square, trapezoid, rhombus, ellipse, parallelogram")
    print("Type 'quit' to exit the program")
    print()
    
    while True:
        # Get shape from user
        shape = input("Enter a shape (or 'quit' to exit): ").strip()
        
        if shape.lower() == 'quit':
            print("Goodbye!")
            break
            
        if not shape:
            print("Please enter a valid shape!")
            continue
            
        # Get dimensions for the shape
        dimensions = get_dimensions_for_shape(shape)
        
        if dimensions is None:
            print(f"Sorry, '{shape}' is not a supported shape.")
            print("Available shapes: circle, rectangle, triangle, square, trapezoid, rhombus, ellipse, parallelogram")
            continue
            
        # Calculate and display area
        success = calculate_area(shape, dimensions)
        print("-" * 50)
        print(success)

if __name__ == "__main__":
    main()


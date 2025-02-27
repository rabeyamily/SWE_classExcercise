def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)

def main():
    print("Welcome to the Geometry Calculator!")
    print("-----------------------------------")
    
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        
        area = calculate_area(length, width)
        perimeter = calculate_perimeter(length, width)
        
        print(f"\nResults:")
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Area: {area} square units")
        print(f"Perimeter: {perimeter} units")
        
        # Add a simple shape visualization
        print("\nShape visualization:")
        for i in range(min(int(width), 10)):
            print("*" * min(int(length), 20))
            
    except ValueError:
        print("Error: Please enter valid numbers for length and width.")
    
    print("\nThank you for using the Geometry Calculator!")

if __name__ == "__main__":
    main() 
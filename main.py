def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def main():
    print("Welcome to the Area Calculator!")
    print("-------------------------------")
    
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        
        area = calculate_area(length, width)
        
        print(f"\nResults:")
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Area: {area} square units")
        
    except ValueError:
        print("Error: Please enter valid numbers for length and width.")

if __name__ == "__main__":
    main() 
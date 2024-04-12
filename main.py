import turtle

def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

def draw_circle():
    turtle.circle(50)

def draw_star():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)

def main():
    turtle.setup(width=600, height=600)
    turtle.title("Animal Drawer")

    animals = {
        "square": draw_square,
        "triangle": draw_triangle,
        "circle": draw_circle,
        "star": draw_star
    }

    print("Choose an animal to draw: square, triangle, circle, star")
    user_choice = input("Enter the name of the animal: ").lower()

    if user_choice in animals:
        turtle.clear()

        animals[user_choice]()
    else:
        print("Sorry, that's not a valid choice.")

    turtle.done()

if __name__ == "__main__":
    main()

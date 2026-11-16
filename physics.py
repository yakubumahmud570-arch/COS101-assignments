
# Physics Operations Assignment

# Function to calculate Speed
def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    if time != 0:
        print("Speed =", distance / time, "m/s")
    else:
        print("Time cannot be zero")

# Function to calculate Force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    print("Force =", mass * acceleration, "N")

# Function to calculate Work
def work():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    print("Work =", force_value * distance, "J")

# Function to calculate Power
def power():
    work_done = float(input("Enter work done (J): "))
    time = float(input("Enter time (s): "))
    if time != 0:
        print("Power =", work_done / time, "W")
    else:
        print("Time cannot be zero")

# Function to calculate Density
def density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))
    if volume != 0:
        print("Density =", mass / volume, "kg/m³")
    else:
        print("Volume cannot be zero")


# Main program
while True:
    print("\n===== PHYSICS OPERATIONS =====")
    print("1. Speed")
    print("2. Force")
    print("3. Work")
    print("4. Power")
    print("5. Density")

    choice = input("Choose an operation (1-5): ")

    if choice == "1":
        speed()
    elif choice == "2":
        force()
    elif choice == "3":
        work()
    elif choice == "4":
        power()
    elif choice == "5":
        density()
    else:
        print("Invalid choice!")

    answer = input("\nDo you want to continue? (yes/no): ").lower()

    if answer != "yes":
        print("Thank you for using the Physics Calculator!")
        break

# PHYSICS FORMULA SOLVER - VERSION 2
# Five different Physics formulas using a while loop.
# Answers are rounded to 2 decimal places.

while True:
    print("\n" + "=" * 38)
    print("       PHYSICS FORMULA SOLVER 2")
    print("=" * 38)
    print("1. Acceleration")
    print("2. Kinetic Energy")
    print("3. Gravitational Potential Energy")
    print("4. Density")
    print("5. Electrical Power")

    choice = input("Choose a formula (1-5): ").strip()

    if choice == "1":
        final_velocity = float(input("Enter final velocity (m/s): "))
        initial_velocity = float(input("Enter initial velocity (m/s): "))
        time = float(input("Enter time (s): "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            acceleration = (final_velocity - initial_velocity) / time
            print(f"Acceleration = {acceleration:.2f} m/s^2")

    elif choice == "2":
        mass = float(input("Enter mass (kg): "))
        velocity = float(input("Enter velocity (m/s): "))
        kinetic_energy = 0.5 * mass * velocity ** 2
        print(f"Kinetic Energy = {kinetic_energy:.2f} J")

    elif choice == "3":
        mass = float(input("Enter mass (kg): "))
        gravity = float(input("Enter gravitational field strength (m/s^2): "))
        height = float(input("Enter height (m): "))
        potential_energy = mass * gravity * height
        print(f"Gravitational Potential Energy = {potential_energy:.2f} J")

    elif choice == "4":
        mass = float(input("Enter mass (kg): "))
        volume = float(input("Enter volume (m^3): "))
        if volume == 0:
            print("Volume cannot be zero.")
        else:
            density = mass / volume
            print(f"Density = {density:.2f} kg/m^3")

    elif choice == "5":
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))
        electrical_power = voltage * current
        print(f"Electrical Power = {electrical_power:.2f} W")

    else:
        print("Invalid choice. Please select a number from 1 to 5.")

    again = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Thank you for using the Physics Formula Solver!")
        break

import csv

# Define color codes
GREEN = "\033[32m"    # Available seat
RED = "\033[31m"      # Occupied seat
YELLOW = "\033[33m"   # Reserved seat
BLUE = "\033[34m"     # VIP seat
RESET = "\033[0m"     # Reset color

# Prices for each type of seat
SEAT_PRICES = {
    "A": 0,     # Available
    "O": 10,    # Occupied/Booked
    "R": 5,     # Reserved
    "V": 20     # VIP
}

# Create a 5x5 seating chart with all seats initially "available"
seating_chart = []
for i in range(5):
    seating_chart.append(["A"] * 5)

# Function to display the seating chart with color-coded seats
def display_chart():
    print("Seating Chart:")
    for row in seating_chart:
        for seat in row:
            if seat == "A":
                print(GREEN + "A" + RESET, end=" ")
            elif seat == "O":
                print(RED + "O" + RESET, end=" ")
            elif seat == "R":
                print(YELLOW + "R" + RESET, end=" ")
            elif seat == "V":
                print(BLUE + "V" + RESET, end=" ")
        print()  # Newline after each row

# Function to book a seat
def book_seat(row, col):
    if seating_chart[row][col] == "A":
        confirm = input(f"Booking this seat costs ${SEAT_PRICES['O']}. Proceed? (yes/no): ").lower()
        if confirm == "yes":
            seating_chart[row][col] = "O"
            print("Seat booked successfully!")
    else:
        print("Seat is not available for booking.")

# Function to reserve a seat
def reserve_seat(row, col):
    if seating_chart[row][col] == "A":
        confirm = input(f"Reserving this seat costs ${SEAT_PRICES['R']}. Proceed? (yes/no): ").lower()
        if confirm == "yes":
            seating_chart[row][col] = "R"
            print("Seat reserved successfully!")
    else:
        print("Seat is not available for reservation.")

# Function to mark a seat as VIP
def vip_seat(row, col):
    if seating_chart[row][col] == "A":
        confirm = input(f"Marking this seat as VIP costs ${SEAT_PRICES['V']}. Proceed? (yes/no): ").lower()
        if confirm == "yes":
            seating_chart[row][col] = "V"
            print("Seat marked as VIP!")
    else:
        print("Seat is not available for VIP status.")


# Function to cancel a reservation or booking
def cancel_seat(row, col):
    if seating_chart[row][col] in ["O", "R", "V"]:
        seating_chart[row][col] = "A"
        print("Seat reservation/booking canceled successfully!")
    else:
        print("Seat is already available.")

# Function to view seat summary
def view_seat_summary():
    # A dictionary can be used to store values for a key
    # In our case we can store the number of seats per category
    # e.g. Available: 24, Booked: 1
    summary = {"A": 0, "O": 0, "R": 0, "V": 0}
    for row in seating_chart:
        for seat in row:
            summary[seat] += 1
    print(f"\nSeat Summary:\nAvailable: {summary['A']}\nBooked: {summary['O']}\nReserved: {summary['R']}\nVIP: {summary['V']}")

# Save seating chart to file
def save_file():
    with open("seating_chart.txt", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(seating_chart)
    input("Seating Chart Saved. Press Enter to continue...")

# Load seating chart from file
def load_file():
    global seating_chart
    loaded_seating_chart = []
    with open("seating_chart.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            loaded_seating_chart.append(row)
    seating_chart = loaded_seating_chart
    input("Seating Chart Loaded. Press Enter to continue...")

# Main program loop
def main():
    while True:
        display_chart()
        action = input("\nChoose an action - Book, Reserve, VIP, Cancel, Summary, Save, Load, Exit: ").lower()
        
        if action == "exit":
            break
        elif action in ["book", "reserve", "vip", "free", "cancel"]:
            row = int(input("Enter row number (1-5): ")) - 1
            col = int(input("Enter seat number (1-5): ")) - 1

            if 0 <= row < 5 and 0 <= col < 5:
                if action == "book":
                    book_seat(row, col)
                elif action == "reserve":
                    reserve_seat(row, col)
                elif action == "vip":
                    vip_seat(row, col)
                elif action == "free":
                    free_seat(row, col)
                elif action == "cancel":
                    cancel_seat(row, col)
            else:
                print("Invalid row or seat number. Please choose between 1 and 5.")
        elif action == "summary":
            view_seat_summary()
        elif action == "save":
            save_file()
        elif action == "load":
            load_file()

main()

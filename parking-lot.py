import sys

parking_lot = []

def create(size):
    global parking_lot
    parking_lot = [0] * size
    print(f"Created parking lot with {size} slots")

def park(car_number):
    global parking_lot
    slot = parking_lot.index(0) + 1 if 0 in parking_lot else 0
    if not slot:
        print("Parking lot is full")
        return
    parking_lot[slot-1] = 1
    print(f"Allocated slot number: {slot}")

def leave(car_number, hours):
    global parking_lot
    try:
        slot = parking_lot.index(1) + 1
    except ValueError:
        print(f"Car {car_number} not found")
        return
    parking_lot[slot-1] = 0
    charge = 10 + (hours - 2) * 10 if hours > 2 else 10
    print(f"Registration number {car_number} with Slot Number {slot} is free with Charge {charge}")

def status():
    print("Slot No.\tRegistration No.")
    for i, status in enumerate(parking_lot):
        if status == 1:
            print(f"{i+1}\t\t{parking_lot[i]}")

with open(sys.argv[1], 'r') as f:
    for line in f:
        command = line.strip().split()
        if command[0] == "create":
            create(int(command[1]))
        elif command[0] == "park":
            park(command[1])
        elif command[0] == "leave":
            leave(command[1], int(command[2]))
        elif command[0] == "status":
            status()
        else:
            print("Invalid command")

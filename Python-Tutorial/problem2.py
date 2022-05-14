# Text Car game

command = ""
started = False
stopped = True
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started.")
        else:
            stopped = False
            started = True
            print("Car started...")
    elif command == "stop":
        if stopped:
            print("Car already stopped.")
        else:
            stopped = True
            started = False
            print("Car Stopped...")
    elif command == "help":
        print("""
start - to start the car
end - to stop the car
quit - to exit the game
        """)
    elif command == "quit":
        print("Exiting game...")
        break
    else:
        print("Sorry, I dont understand that.")

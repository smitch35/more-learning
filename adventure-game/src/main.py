def main():
    print("Welcome to the Adventure Game!")
    print("Type 'start' to begin your adventure or 'quit' to exit.")

    while True:
        command = input("> ").strip().lower()
        if command == "start":
            from game.adventure import Adventure
            game = Adventure()
            game.start_game()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command. Please type 'start' or 'quit'.")

if __name__ == "__main__":
    main()
import pygame
import sys
import os

def title_screen():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Adventure Game Title Screen")
    font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 32)
    menu_items = ["Start Game", "Options", "Credits", "Quit"]
    selected = 0
    running = True
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join("game", "music", "title_screen.mp3"))
    pygame.mixer.music.play(-1)

    while running:
        screen.fill((0, 0, 0))
        title_text = font.render("Welcome to the Adventure Game!", True, (0, 255, 0))
        screen.blit(title_text, (50, 50))

        for i, item in enumerate(menu_items):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            text = small_font.render(item, True, color)
            screen.blit(text, (100, 150 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    return menu_items[selected].lower().replace(" ", "_")

    pygame.quit()

# Example usage:
choice = title_screen()
if choice == "start_game":
    from game.adventure import Adventure
    game = Adventure()
    game.start_game()
    pass
elif choice == "options":
    print("This isn't Implemented yet.")
    sys.exit()
elif choice == "credits":
    print("Writer / Pogrammer xTigerMaskx, Music by RG450")
    sys.exit()
elif choice == "quit":
    sys.exit()

    



#def main():
#    print("Welcome to the Adventure Game!")
#    print("Type 'start' to begin your adventure or 'quit' to exit.")#
#
#    while True:
#        command = input("> ").strip().lower()
#        if command == "start":
#            
#        elif command == "quit":
#            print("Thanks for playing!")
#            break
#        else:
#            print("Invalid command. Please type 'start' or 'quit'.")
#
#if __name__ == "__main__":
#    main()
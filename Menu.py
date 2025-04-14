import pygame,sys
from button import Button
from Hard_Game import HardGame
from Easy_Game import EasyGame

pygame.init()

def Menu():
    BG = pygame.image.load("GUI\\Menu background.png")
    screen = pygame.display.set_mode((1000, 600))

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("Font/BAUHS93.TTF", size)
    def main_menu():
        while True:
            screen.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(100).render("MAIN MENU", True, "darkgreen")
            MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

            Easy_BUTTON = Button(image=pygame.image.load("GUI\\Play Rect.png"), pos=(500, 250), 
                            text_input="Easy",font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            Hard_BUTTON = Button(image=pygame.image.load("GUI\\Quit Rect.png"), pos=(500, 400), 
                            text_input="Hard",font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            screen.blit(MENU_TEXT, MENU_RECT)

            for button in [Easy_BUTTON, Hard_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Clicking events
                elif event.type == pygame.MOUSEBUTTONUP:
                    if Easy_BUTTON.checkForInput(MENU_MOUSE_POS):
                        EasyGame()
                    elif Hard_BUTTON.checkForInput(MENU_MOUSE_POS):
                        HardGame()
            pygame.display.update()
    main_menu()
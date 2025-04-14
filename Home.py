#importing, initialization,and screen
import pygame, sys
from Menu import Menu

white, gray, dark_gray = (255, 255, 255), (200, 200, 200), (150, 150, 150)

def soundConfig():
    BackgroundMusic = pygame.mixer.Sound("Sounds\\background.mp3")
    BackgroundMusic.set_volume(0.4)
    BackgroundMusic.play(-1)

def setTitle():
    pygame.display.set_caption("Image matching")

def setIcon():
    pygame.display.set_icon(pygame.image.load("GUI\\Cherries.ico"))

def playButnConfig():
    play_butn = pygame.image.load("GUI\\play.png")
    play_butn = pygame.transform.scale(play_butn,(400,100))
    return play_butn

def playButnRectConfig():
    play_butn_rect = play_butn.get_rect()
    play_butn_rect.left, play_butn_rect.top = 300, 480
    return play_butn_rect


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 600))

soundConfig();
setTitle();
setIcon();

play_butn = playButnConfig();
play_butn_rect = playButnRectConfig();

play_rect = pygame.Rect(405, 250, 250, 80)
more_rect = pygame.Rect(405, 350, 250, 80)

play_color = white
play_hover_color = gray
more_color = white
more_hover_color = gray

# button variables

#True if more button was clicked
more = False

#Home background
background = pygame.image.load("GUI\\background.jpeg")
screen.blit(background,(0,0))

more_menu = pygame.image.load("GUI\\More menu.png")

#Drawing buttons
pygame.draw.rect(screen, play_color, play_rect)
pygame.draw.rect(screen, more_color, more_rect)

#Texts on buttons
font = pygame.font.Font(None, 40)
text = font.render("PLAY", True, (0, 0, 0))     #play
screen.blit(text, (495, play_rect.y + 30))      

text = font.render("MORE", True, (0, 0, 0))     #more
screen.blit(text, (490, more_rect.y + 30))


while True:
    mouse_pos = pygame.mouse.get_pos()
    if not more:
        pygame.draw.rect(screen, play_color, play_rect)
        pygame.draw.rect(screen, more_color, more_rect)
        text = font.render("PLAY", True, (0, 0, 0))     #play word
        screen.blit(text, (495, play_rect.y + 30))      

        text = font.render("MORE", True, (0, 0, 0))     #more word
        screen.blit(text, (490, more_rect.y + 30))

    # hovering effect
    if play_rect.collidepoint(mouse_pos):
        play_color = play_hover_color
    else:
        play_color = white

    if more_rect.collidepoint(mouse_pos):
        more_color = more_hover_color
    else:
        more_color = white

    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Clicking events
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if play_rect.collidepoint (mouse_pos):
                Menu()
            elif more_rect.collidepoint(mouse_pos):
                screen.blit(more_menu,(0,0))
                more = True
                screen.blit(play_butn, play_butn_rect)
            elif play_butn_rect.collidepoint(mouse_pos) and more==True:
                more = False
                Menu()

    pygame.display.flip()
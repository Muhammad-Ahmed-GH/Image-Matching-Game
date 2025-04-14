#Members Names:
    #Mohamed Ahmed Ibrahim     231002063
    #Mahmoud Hasan             231000496
    #Shehab Sayed              231002292
    #Mazen Kamal               231002151
#Course code: CSCI102
#Lecture number: 07
#Lab number: 07A

#importing, initialization,and screen
import pygame, sys
from Menu import Menu
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 600))

#Sound
BackgroundMusic = pygame.mixer.Sound("Sounds\\background.mp3")
BackgroundMusic.set_volume(0.4)
BackgroundMusic.play(-1)

# title and icon
pygame.display.set_caption("Image matching")
icon = pygame.image.load("GUI\\Cherries.ico")
pygame.display.set_icon(icon)

#play button
play_butn2 = pygame.image.load("GUI\\play.png")
play_butn2 = pygame.transform.scale(play_butn2,(400,100))
play_butn2_rect = play_butn2.get_rect()
play_butn2_rect.left, play_butn2_rect.top = 300, 480

# colors
white, gray, dark_gray = (255, 255, 255), (200, 200, 200), (150, 150, 150)

# button colors
play_color = white
play_hover_color = gray
more_color = white
more_hover_color = gray

# button variables
play_rect = pygame.Rect(405, 250, 250, 80)
more_rect = pygame.Rect(405, 350, 250, 80)

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
                screen.blit(play_butn2, play_butn2_rect)
            elif play_butn2_rect.collidepoint(mouse_pos) and more==True:
                more = False
                Menu()

    pygame.display.flip()
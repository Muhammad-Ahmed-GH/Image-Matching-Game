import pygame, os, random, sys
pygame.init()
pygame.mixer.init()

def EasyGame():
       #Screen, resolution, and caption
       resolution = GameWidth,GameHeight= 1000,600
       screen = pygame.display.set_mode(resolution)

       #background
       background = pygame.image.load("GUI\\background.png")
       background = pygame.transform.scale(background,resolution)
       screen.blit(background,(0,0))

       #Game properties
       columns,rows,padding,score,card_width, card_height = 4,3,10,0,100,150
       clicked,now,win,pause =False,False,False,False
       font = pygame.font.Font("Font\\BAUHS93.TTF",40)
       LeftMargin = (GameWidth-card_width*columns - padding*(columns-1))//2
       TopMargin = (GameHeight-card_height*rows - padding*(rows-1))//2

       #Control lists
       ImagesDisplay, permission = [], []

       #Card back
       Card_back = pygame.image.load("GUI\\Full Card back.png")
       Card_back = pygame.transform.scale(Card_back,(card_width,card_height))

       #Music
       winning_music = pygame.mixer.Sound("Sounds\\Winning.mp3")
       bonus_music = pygame.mixer.Sound("Sounds\\Bonus.mp3")
       wrong_music = pygame.mixer.Sound("Sounds\\Wrong.mp3")

       ###   Mazen   ###
       #pause button
       pause_button = pygame.image.load("GUI\\pause.png")
       pause_button = pygame.transform.scale(pause_button,(50,40))
       pause_rect = pause_button.get_rect()
       pause_rect.left, pause_rect.top = 950,20
       screen.blit(pause_button,pause_rect)
       #menu
       menu = pygame.image.load("GUI\\menu.png")
       menu = pygame.transform.scale(menu,(600,450))
       menu_rect = menu.get_rect()
       menu_rect.left, menu_rect.top = 0.5*(GameWidth-600), 0.5*(GameHeight-450)

       #continue button
       continue_button = pygame.image.load("GUI\\continue.png")
       continue_button = pygame.transform.scale(continue_button,(400,100))
       continue_rect = continue_button.get_rect()
       continue_rect.left, continue_rect.top = 0.5*(GameWidth-400), 0.5*(GameHeight-450)+120

       #exit buttons
       exit_button = pygame.image.load("GUI\\exit.png")
       exit_button = pygame.transform.scale(exit_button,(400,100))
       exit_rect = exit_button.get_rect()
       exit_rect.left, exit_rect.top = 0.5*(GameWidth-400), 0.5*(GameHeight-500)+150

       exit2_rect = exit_rect
       exit2_rect.left, exit2_rect.top = 0.5*(GameWidth-400), 0.5*(GameHeight-500)+250

       #you win text
       you_win = pygame.font.Font("Font\\BAUHS93.TTF",70)
       you_win = you_win.render('You Win!', True, "dark green")

       #play again button
       play_again = pygame.image.load("GUI\\play again.png")
       play_again = pygame.transform.scale(play_again,(400,100))
       play_again_rect = play_again.get_rect()
       play_again_rect.left, play_again_rect.top = 300,200

       ###   Mazen   ###
       def animation(name,reverse=False):
              sprite = []
              for k in range(9):
                     sprite.append(pygame.image.load(f"Animation/{name}/0{k}_{name} Sprite2.png"))
              sprite_scale = []
              for i in sprite:
                     sprite1 = pygame.transform.scale(i,(card_width,card_height))
                     sprite_scale.append(sprite1)
              if reverse==True:
                     return sprite_scale[::-1]
              elif reverse==False:
                     return sprite_scale

       def check_display():
              for i in range(len(images)):
                     if ImagesDisplay[i]==True:
                            screen.blit(images[i],images_rect[i])
                     elif ImagesDisplay[i]== False:
                            screen.blit(Card_back,images_rect[i])
       def wait(seconds):
              start_time = pygame.time.get_ticks()
              wait_duration = seconds * 1000  # Convert seconds to milliseconds

              while (pygame.time.get_ticks() - start_time) < wait_duration:
                     for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                   pygame.quit()
                                   sys.exit()

                     pygame.display.flip()

       #List of images names
       PicNames_list=[image.split(".")[0] for image in os.listdir("Easy Images/")]   #list of names of cards
       PicNames_list+=PicNames_list[:]                                               #copying list elements             
       random.shuffle(PicNames_list)                                                 #randomizing the list

       #List of images & rect
       images, images_rect = [], []
       for k in PicNames_list:
              image = pygame.image.load(f"Easy Images/{k}.png")                      #loading of images
              image = pygame.transform.scale(image,(card_width,card_height))             #scaling of images
              images.append(image)                                                  #appending images into a list
              image_rect= image.get_rect()                                          #declaring a rectangle for each image
              images_rect.append(image_rect)                                        #appending rectangles into a list
              ImagesDisplay.append(True)
              permission.append("permitted")

       #Positions of rectangles
       for k in range(len(images)):
              images_rect[k].left = LeftMargin + (card_width+padding)*(k % columns)
              images_rect[k].top = TopMargin + (card_height+padding)*(k % rows)

       #Showing Cards
       check_display()

       #Score text
       ScoreText=font.render(f"Score: {score}",True,"dark cyan")
       screen.blit(ScoreText,(20,5))

       wait(1.5)

       #Hiding Images
       for j in range(9):
              animation_vars = [animation(PicNames_list[k],True)[j] for k in range(12)]
              wait(0.005)
              screen.blit(background,(0,0))
              screen.blit(pause_button,pause_rect)
              screen.blit(ScoreText,(20,5))

              for i in range(len(animation_vars)):
                     screen.blit(animation_vars[i],images_rect[i])
       ImagesDisplay=[False]*len(PicNames_list)
       check_display

       now, pause, win, GameFlag=True, False, False, True
       while True:
              pygame.display.update()
              screen.blit(background,(0,0))
              screen.blit(pause_button,pause_rect)

              #Images display
              check_display()
              #score text
              ScoreText=font.render(f"Score: {score}",True,"dark cyan")
              screen.blit(ScoreText,(20,5))

              #WIN
              if score==300 and GameFlag:
                     winning_music.play(0)
                     win=True
                     GameFlag = False
              #Events
              for event in pygame.event.get():
                     if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                     #Clicking events
                     elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
                            if pause == False or win==False:
                                   for i in range(len(images)):
                                          if images_rect[i].collidepoint(event.pos):
                                                 #First card
                                                 if not(clicked) and permission[i]=="permitted" and pause==False:
                                                        clicked = ImagesDisplay[i]="2"###
                                                        check_display()
                                                        selection1 = PicNames_list[i]
                                                        selection1_index=i
                                                        ###   Mazen   ###
                                                        for j in range(9):
                                                               animation_var=animation(selection1)[j]
                                                               wait(0.005)
                                                               screen.blit(background,(0,0))
                                                               screen.blit(pause_button,pause_rect)
                                                               screen.blit(ScoreText,(20,5))
                                                               check_display()
                                                               screen.blit(animation_var,images_rect[i])
                                                        ImagesDisplay[i]=True

                                                 #Second Card
                                                 elif clicked and permission[i]=="permitted" and now==True and pause==False:
                                                        now=False
                                                        ImagesDisplay[i]="2"###
                                                        
                                                        check_display()
                                                        selection2 = PicNames_list[i]
                                                        
                                                        if selection1==selection2 and i!=selection1_index:
                                                               ###   Mazen   ###
                                                               for j in range(9):
                                                                      animation_var=animation(selection2)[j]
                                                                      wait(0.005)
                                                                      screen.blit(background,(0,0))
                                                                      screen.blit(pause_button,pause_rect)
                                                                      screen.blit(ScoreText,(20,5))
                                                                      check_display()
                                                                      screen.blit(animation_var,images_rect[i])
                                                               ImagesDisplay[i]=True

                                                               bonus_music.play(0)
                                                               score+=50
                                                               permission[i] = permission[selection1_index] ="not permitted"
                                                               now=True
                                                               clicked=False
                                                        
                                                        elif selection1==selection2 and i==selection1_index:
                                                               wrong_music.play(0)
                                                               wait(0.5)
                                                               ImagesDisplay[i] = ImagesDisplay[selection1_index] ="2"####
                                                               check_display()
                                                               now=True
                                                               ###   Mazen   ###
                                                               for j in range(9):
                                                                      animation_var0=animation(selection1,True)[j]
                                                                      wait(0.005)
                                                                      screen.blit(background,(0,0))
                                                                      screen.blit(pause_button,pause_rect)
                                                                      screen.blit(ScoreText,(20,5))
                                                                      check_display()
                                                                      screen.blit(animation_var0,images_rect[selection1_index])
                                                               clicked=False
                                                               ImagesDisplay[i]=ImagesDisplay[selection1_index]=False###
                                                                                                                       
                                                        else:
                                                               ###   Mazen   ###
                                                               for j in range(9):
                                                                      animation_var=animation(selection2)[j]
                                                                      wait(0.005)
                                                                      screen.blit(background,(0,0))
                                                                      screen.blit(pause_button,pause_rect)
                                                                      screen.blit(ScoreText,(20,5))
                                                                      check_display()
                                                                      screen.blit(animation_var,images_rect[i])
                                                               ImagesDisplay[i]=True

                                                               wrong_music.play(0)
                                                               wait(0.5)
                                                               ImagesDisplay[i] = ImagesDisplay[selection1_index] ="2"####
                                                               check_display()
                                                               now=True
                                                               ###   Mazen   ###
                                                               for j in range(9):
                                                                      animation_var0=animation(selection1,True)[j]
                                                                      animation_var1=animation(selection2,True)[j]
                                                                      wait(0.005)
                                                                      screen.blit(background,(0,0))
                                                                      screen.blit(pause_button,pause_rect)
                                                                      screen.blit(ScoreText,(20,5))
                                                                      check_display()
                                                                      screen.blit(animation_var0,images_rect[selection1_index])
                                                                      screen.blit(animation_var1,images_rect[i])
                                                               clicked=False
                                                               ImagesDisplay[i]=ImagesDisplay[selection1_index]=False###
                             ###   Mazen   ###
                            if pause_rect.collidepoint(event.pos) and pause==False:
                                   pause=True
                            elif continue_rect.collidepoint(event.pos) and pause==True:
                                   pause=False
                            elif exit_rect.collidepoint(event.pos) and pause==True:
                                   pygame.quit()
                                   sys.exit()
                            elif play_again_rect.collidepoint(event.pos) and win==True:
                                   EasyGame()
                            elif exit2_rect.collidepoint(event.pos) and win==True:
                                   pygame.quit()
                                   sys.exit()
              ###   Mazan   ###
              if pause==True:
                     screen.blit(menu,menu_rect)
                     screen.blit(continue_button,continue_rect)
                     screen.blit(exit_button,exit_rect)
              if win==True:
                     screen.blit(menu,menu_rect)
                     screen.blit(you_win,(365,110))
                     screen.blit(play_again,play_again_rect)
                     screen.blit(exit_button,exit2_rect)
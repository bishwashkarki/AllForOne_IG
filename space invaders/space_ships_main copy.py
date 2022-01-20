import pygame

#screen = pygame.display.set_mode((1600,900))
screen = pygame.display.set_mode((1500,800))

background = pygame.image.load('images/background_space.bmp').convert()
player1=pygame.image.load('images/player2.bmp').convert()
player1 = pygame.transform.scale(player1, (50, 50))

class space_ships:
    
    def player1_movement():
        screen.blit(background,(0,0))
    
        position = player1.get_rect(midbottom=(700,800))
        screen.blit(player1, position)

        WHITE=(255, 255, 255)
        player1.set_colorkey(WHITE) 
        # jogo a correr
        main = True
        # equanto o jogo estiver a correr
        while main:
            speed=10

            # adiciona janela do jogo
            pygame.display.flip()
            pygame.time.wait(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); 
                    main = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        screen.blit(background, position, position)
                        position = position.move(-(speed)-10, 0)
                        screen.blit(player1, position) 
                        pygame.display.update()
                        pygame.time.delay(100)
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        screen.blit(background, position, position)
                        position = position.move(10, 0)
                        screen.blit(player1, position) 
                        pygame.display.update()
                        pygame.time.delay(100)
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        screen.blit(background, position, position)
                        position = position.move(0, -10)
                        screen.blit(player1, position) 
                        pygame.display.update()
                        pygame.time.delay(100)
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        screen.blit(background, position, position)
                        position = position.move(0, 10)
                        screen.blit(player1, position) 
                        pygame.display.update()
                        pygame.time.delay(100)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        print('left stop')
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        print('right stop')
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        print('forward stop')
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        print('backwards stop')
                    if event.key == ord('q'):
                        pygame.quit()
                        main = False 

#   def shoot_prjectiles():
#       missile=pygame.image.load('images/player1.bmp').convert()
#       missile = pygame.transform.scale(missile, (50, 50))
#       position = missile.get_rect(midbottom=(700,800))
#       screen.blit(missile, position)
#       missile_speed=50
#       for event in pygame.event.get():
#           if event.type == pygame.MOUSEBUTTONDOWN:
#               if event.key == pygame.BUTTON_LEFT:
#                   missile.



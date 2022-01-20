# importar todos os tipos de módulos disponíveis dentro do pacote do pygame
import pygame


# abre o ficheiro "game" e nos permite aceder aos metodos da classe "Game"
from game import Game


# Concede o acesso às funções subjacentes da biblioteca C permitindo usar funções matemáticas
import math


def start_game():
    # inicia todos os modulos importados do pygame
    pygame.init()

                            
    # insere a imagem de fundo do jogo
    pygame.display.set_caption("Pixel Zombie")
    screen = pygame.display.set_mode((1400, 652))
    background = pygame.image.load('objects/game_bg_image.png')


    # insere a imagem com o nome do jogo
    game_image = pygame.image.load('objects/pixel.png')
    # define a largura a altura da imagem(x, y)
    game_image = pygame.transform.scale(game_image, (400, 440))
    game_image_rect = game_image.get_rect()
    # define em que posição a imagem irá ficar de acordo ao eixo do x e y
    game_image_rect.x = math.ceil(screen.get_width() / 2.78)
    game_image_rect.y = math.ceil(screen.get_width() / 20)

    
    # insere um icon à janela
    pygame.display.set_icon(pygame.image.load('objects/toxic_icon.ico'))


    # cria um objeto que ajuda a acompanhar o tempo de algo
    clock = pygame.time.Clock()
    # atribui à variável um o valor de frames per second
    FPS = 144
    

    # variável referente à classe Game
    game = Game()


    # jogo a correr
    running = True



    # equanto o jogo estiver a correr
    while running:
        
        
        # adiciona janela do jogo
        screen.blit(background,(0,0))



        # verifica se o jogo começou
        if game.playing:
            # chama a função com os comandos para inserir os objetos, etc. no jogo
            game.update(screen)
        else:
            # aplica a imagem do nome do jogo
            screen.blit(game_image, game_image_rect)
            # implementa/ativa o som no jogo
          
       




        # tela de atualização 
        pygame.display.flip()

            
    

        # evento da janela do jogo
        for event in pygame.event.get():
            # confere se o jogo fecho
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()


            # confere se o botão foi precionado
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                            
                # reconhece se o jogador deu um toque no espaço para disparar 
                if event.key == pygame.K_SPACE:
                    game.player.shoot()
                    # implementa/ativa o som no jogo
                    game.sound_manager.play_sound('shoot')




            #  confere se o botão foi solto
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False


            # verifica se ouve interação com o bottão do jogo
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_image_rect.collidepoint(event.pos):
                    # ativa a jogo
                    game.start()
                    # implementa/ativa o som no jogo
                    game.sound_manager.play_sound('click')


    # o clock ajusta durante o jogo os fps padrões ja existentes do jogo para os fps atribuidos na variável acima (FPS)
    clock.tick(FPS)
                

            

         

            
                








        



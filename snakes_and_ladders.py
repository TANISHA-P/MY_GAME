import pygame
import random

pygame.init()
pygame.mixer.init()

game_screen = pygame.display.set_mode((1280,700))
board_x = 340
board_y = 50
pygame.display.set_caption("JOURNEY TO THE MASKLESS LAND")
board = pygame.image.load('final_image.jpg')
girl = pygame.image.load('girl_2.png')
girl = pygame.transform.smoothscale(girl, (45,35)).convert_alpha()
clock = pygame.time.Clock()
path = []
x_val = [883,824,765,706,647,588,529,470,411,352]
y_val = [592,533,474,415,356,297,238,179,120,61]

for i in range(10):
    x_val = x_val[::-1]
    y_new = [y_val[i]]
    path = path + [(x,y) for y in y_new for x in x_val]
initial_up = [path[1],path[8],path[27],path[72],path[79]]
final_up = [path[37],path[24],path[83],path[90],path[98]]
initial_down = [path[16],path[44],path[53],path[63],path[89],path[94],path[97]]
final_down = [path[6],path[22],path[33],path[59],path[29],path[74],path[78]]
def gameloop():
    steps = 35
    loss = False
    exit = False
    girl_x = 352
    girl_y = 592
    dice_x = 1070
    dice_y = 250
    restart = False
    mess = pygame.font.SysFont('lucidasans', 20)
    mess = mess.render("PRESS KEY 'r' TO ROLL THE DICE.",True,(0,0,0))
    game_screen.fill((255, 255, 255))
    pygame.draw.rect(game_screen, (255, 0, 0), [dice_x, dice_y, 100, 100])
    game_screen.blit(mess, (950, 210))
    pygame.display.update()
    pos = 0

    while(not(exit)):
        if(steps == 0):
            loss = True

        if(loss):
            game_screen.fill((244,194,194))
            loss = pygame.font.SysFont('lucidasans', 40)
            loss = loss.render("YOU LOST ! PRESS SPACE TO RESTART", True, (0, 0, 0))
            game_screen.blit(loss, (240, 240))
            pygame.display.update()
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        welcome()
                if (event.type == pygame.QUIT):
                    exit = True
                pygame.mixer.music.load('lose.ogg')
                pygame.mixer.music.play()

        else:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    exit = True
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_r):

                        steps = steps - 1
                        r = random.randint(1,6)
                        if(pos + r == 99):
                            pygame.mixer.music.load('win.ogg')
                            pygame.mixer.music.play()
                            while(not(restart)):
                                game_screen.fill((244, 194, 194))
                                win_mess = pygame.font.SysFont('lucidasans', 40)
                                win_mess = win_mess.render("CONGRATULATIONS !!! YOU WON...PRESS SPACE TO RESTART.", True,(0, 0, 0))
                                game_screen.blit(win_mess, (20, 350))
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if (event.type == pygame.KEYDOWN):
                                        if (event.key == pygame.K_SPACE):
                                            restart = True
                                    if(event.type == pygame.QUIT):
                                        pygame.quit()
                                        quit()
                            welcome()
                        game_screen.fill((255, 255, 255))
                        game_screen.blit(mess, (950, 210))
                        pygame.draw.rect(game_screen, (255, 0, 0), [dice_x, dice_y, 100, 100])
                        if(r == 1):
                            pygame.draw.rect(game_screen, (255, 0, 0), [dice_x, dice_y, 100, 100])
                            pygame.draw.rect(game_screen,(0,0,0),[dice_x+40,dice_y+40,20,20])

                            if (pos + r > 99):
                                continue
                            (girl_x,girl_y) = path[pos+1]
                            pos = pos+1
                        elif(r==2):
                            pygame.draw.rect(game_screen, (255, 0, 0), [dice_x, dice_y, 100, 100])
                            pygame.draw.rect(game_screen,(0,0,0),[dice_x+15,dice_y+40,20,20])
                            pygame.draw.rect(game_screen,(0,0,0),[dice_x+65,dice_y+40,20,20])
                            if (pos + r > 99):
                                continue
                            (girl_x,girl_y) = path[pos+2]
                            pos = pos + 2
                        elif(r==3):
                            pygame.draw.rect(game_screen, (255, 0, 0), [dice_x, dice_y, 100, 100])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 40, dice_y + 15, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 40, dice_y + 40, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 40, dice_y + 65, 20, 20])
                            if (pos + r > 99):
                                continue
                            (girl_x, girl_y) = path[pos + 3]
                            pos = pos + 3
                        elif(r==4):
                            pygame.draw.rect(game_screen, (255, 0, 0), [dice_x, dice_y, 100, 100])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 15, dice_y + 15, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 65, dice_y + 15, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 15, dice_y + 65, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 65, dice_y + 65, 20, 20])
                            if (pos + r > 99):
                                continue
                            (girl_x, girl_y) = path[pos + 4]
                            pos = pos + 4
                        elif(r==5):
                            pygame.draw.rect(game_screen, (255, 0, 0), [dice_x, dice_y, 100, 100])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 15, dice_y + 15, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 65, dice_y + 15, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 15, dice_y + 65, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 65, dice_y + 65, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 40, dice_y + 40, 20, 20])
                            if (pos + r > 99):
                                continue
                            (girl_x, girl_y) = path[pos + 5]
                            pos = pos + 5
                        elif(r==6):
                            pygame.draw.rect(game_screen, (255, 0, 0), [dice_x, dice_y, 100, 100])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 15, dice_y + 15, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 15, dice_y + 40, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 15, dice_y + 65, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 65, dice_y + 15, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 65, dice_y + 40, 20, 20])
                            pygame.draw.rect(game_screen, (0, 0, 0), [dice_x + 65, dice_y + 65, 20, 20])
                            if (pos + r > 99):
                                continue
                            (girl_x, girl_y) = path[pos + 6]
                            pos = pos + 6
            if ((girl_x, girl_y) in initial_up):
                pygame.mixer.music.load('up.ogg')
                pygame.mixer.music.play()
                (girl_x, girl_y) = final_up[initial_up.index((girl_x, girl_y))]
                pos = path.index((girl_x, girl_y))
            if ((girl_x, girl_y) in initial_down):
                pygame.mixer.music.load('down.ogg')
                pygame.mixer.music.play()
                (girl_x, girl_y) = final_down[initial_down.index((girl_x, girl_y))]
                pos = path.index((girl_x, girl_y))


            game_screen.blit(board, (board_x,board_y))
            game_screen.blit(girl, (girl_x, girl_y))
            chances = pygame.font.SysFont('lucidasans', 20)
            chances = chances.render(f"Chances left = {steps}", True, (0, 0, 0))
            game_screen.blit(chances, (950, 180))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

def welcome():
    exit_game = False
    game_screen.fill((244, 194, 194))
    def text(size,message,location):
        _text = pygame.font.SysFont('lucidasans',size)
        _text = _text.render(message,True,(0,0,0))
        game_screen.blit(_text,location)
    text(50,"WELCOME TO THE MASKLESS LAND !!",(250,40))
    text(30,"Help Misti reach her granny's home which is at box 100.",(250, 200))
    text(30,"You have 35 chances to do so.",(230, 240))
    text(30,"BEWARE OF VIRUSES !!",(250, 280))
    text(30,"DEFEAT THEM USING YOUR PROTECTOR - YOUR MASK",(230, 320))
    text(30,"BEST OF LUCK.",(250, 360))
    text(30,"PRESS 'S' TO START THE GAME.",(230, 400))
    pygame.display.update()
    while (not (exit_game)):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_s):
                    gameloop()

welcome()
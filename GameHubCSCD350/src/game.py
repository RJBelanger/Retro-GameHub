from pong import start_pong
from duck import start_duck
from snake import start_snake
#from tag import start_tag
from spaceInvaders import start_space_invaders
from tictactoe import start_tictactoe
import pygame, sys
from Button import Button


pygame.mixer.init()
# modular ability to change the size of the font
def get_font(size):
    return pygame.font.Font("res/fonts/chary___.ttf", size)

def play(window):
    while True:
        # constantly obtain position of the mouse cursor
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # overwrite the screen with a black overlay
        window.fill("black")
        PLAY_TEXT = get_font(45).render("Pick A Game To Play", True, "Gold")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        # render text to screen
        window.blit(PLAY_TEXT, PLAY_RECT)
        # clicking this will return back to the main menu
        Game1B = Button(image=None, pos=(250, 350),
                        text_input="Pong", font=get_font(50), base_color="White", hovering_color="Green")

        Game2B = Button(image=None, pos=(620, 350),
                        text_input="Tic-Tac-Toe", font=get_font(50), base_color="White", hovering_color="Green")

        Game3B = Button(image=None, pos=(990, 350),
                        text_input="DOOM", font=get_font(50), base_color="White", hovering_color="Green")

        Game4B = Button(image=None, pos=(250, 650),
                        text_input="Snake", font=get_font(50), base_color="White", hovering_color="Green")

        Game5B = Button(image=None, pos=(620, 650),
                        text_input="Duck Hunt", font=get_font(50), base_color="White", hovering_color="Green")

        Game6B = Button(image=None, pos=(990, 650),
                        text_input="Space Inv", font=get_font(50), base_color="White", hovering_color="Green")

        # change the color when the mouse is hovering
        Game1B.changeColor(PLAY_MOUSE_POS)
        Game1B.update(window)

        Game2B.changeColor(PLAY_MOUSE_POS)
        Game2B.update(window)

        Game3B.changeColor(PLAY_MOUSE_POS)
        Game3B.update(window)

        Game4B.changeColor(PLAY_MOUSE_POS)
        Game4B.update(window)

        Game5B.changeColor(PLAY_MOUSE_POS)
        Game5B.update(window)

        Game6B.changeColor(PLAY_MOUSE_POS)
        Game6B.update(window)

        pong = pygame.image.load("res/pongIcon.png")
        tik = pygame.image.load("res/tikIcon.png")
        space = pygame.image.load("res/spaceIcon.png")
        duck = pygame.image.load("res/duckIcon.png")
        snake = pygame.image.load("res/snakeIcon.png")
        Doom = pygame.image.load("res/doomIcon.png")

        # images above buttons
        window.blit(pong, (130,130))
        window.blit(tik, (525, 190))
        window.blit(Doom, (820, 145))
        window.blit(snake, (85, 435))
        window.blit(duck, (480, 425))
        window.blit(space, (810, 425))



        #images above buttons
        #window.blit(image1, (50,50))


        for event in pygame.event.get():
            # if you press the "X" button, the game will exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if the mouse clicks the back button, return to main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Game1B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_pong(window)
                if Game2B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_tictactoe(window)
                #if Game3B.checkForInput(PLAY_MOUSE_POS):
                    #pygame.mixer.quit()
                    #start_tag(window)
                if Game5B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_duck(window)
                if Game4B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_snake(window)
                if Game6B.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.quit()
                    start_space_invaders(window)

        # constantly update the screen. this is the critical piece of creating a game loo[]
        pygame.display.update()

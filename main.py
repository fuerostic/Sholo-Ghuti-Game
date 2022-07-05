import pygame, sys
from files.constants import SQUARE_SIZE, WIDTH,HEIGHT,RED, BLUE
from files.board import Board
from files.game import Game
from minimax.algorithm import minimax
from alphabeta.algorithm import minimax_pruning
from button import Button
FPS = 60
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sholo Ghuti')

def get_row_col_from_mouse(pos):
    x , y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col 


def main():

    run = True
    clock = pygame.time.Clock()
    # board = Board()
    game = Game(WIN)

    def get_font(): # Returns Press-Start-2P in the desired size
        return pygame.font.SysFont('Corbel',35)

    def play():
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            #WIN.fill("black")

            #PLAY_TEXT = get_font().render(f"score {self.Boar}", True, "White")
            #PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            #WIN.blit(PLAY_TEXT, PLAY_RECT)
            if game.turn == BLUE:
                #value, new_board = minimax(game.get_board(),3,True, game)
                value, new_board = minimax_pruning(game.get_board(), 3,True, game, float('-inf'), float('inf'))
                game.ai_move(new_board)

            if game.winner()!= None:
                while True:
                    Back_MOUSE_POS = pygame.mouse.get_pos()
                    WIN.fill("black")

                    winnertext = get_font().render(f"{game.winner()} Has WON", True, "White")
                    winnerrect = winnertext.get_rect(center=(200, 400))
                    WIN.blit(winnertext, winnerrect)
                    run = False
                    #print(game.winner())
                    backbutton = Button(pos=(200, 450), 
                                text_input="BACK", font=get_font(), base_color="white", hovering_color="red")

                    backbutton.changeColor(Back_MOUSE_POS)
                    backbutton.update(WIN)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if backbutton.checkForInput(Back_MOUSE_POS):
                                main_menu()

                    pygame.display.update()
                


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    #print(f"row {row} col {col}")
                    # piece = board.get_piece(row,col)
                    #board.move(piece,4,3)
                    # if game.turn == RED:
                    game.select(row,col)

                    # board.draw(WIN)
                    # pygame.display.update()
                game.update()

                #pygame.quit()

            PLAY_BACK = Button( pos=(200, 750), 
                            text_input="BACK", font=pygame.font.SysFont('Corbel',14), base_color="black", hovering_color="red")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
               
            PLAY_BACK.update(WIN)
            pygame.display.update()
    

    def main_menu():
        while True:
            WIN.fill("black")

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font().render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(200, 100))

            PLAY_BUTTON = Button(pos=(200, 250), 
                                text_input="PLAY", font=get_font(), base_color="#d7fcd4", hovering_color="green")
            QUIT_BUTTON = Button(pos=(200, 550), 
                            text_input="QUIT", font=get_font(), base_color="#d7fcd4", hovering_color="red")

            WIN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(WIN)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        play()
                    elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    main_menu()
    


main()
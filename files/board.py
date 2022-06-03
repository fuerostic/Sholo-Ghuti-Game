import pygame

from .constants import BLACK, COLS, GREY, RADIUS, ROWS, RED, SQUARE_SIZE, WHITE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 16
        self.red_kings = self.white_kings = 0
        # self.create_board()

    def draw_line(self,point1,point2,win):
        y1,x1 = point1
        y2,x2 = point2
        pygame.draw.line(win, BLACK, (x1*SQUARE_SIZE + SQUARE_SIZE//2, y1*SQUARE_SIZE + SQUARE_SIZE//2), (x2*SQUARE_SIZE + SQUARE_SIZE//2, y2*SQUARE_SIZE + SQUARE_SIZE//2),2)

    def draw_points(self,win):
        PADDING = 15
        OUTLINE  = 2
        win.fill(WHITE)
        point_list = []
        point_list1 = [(0,0),(1,1),(2,0),(3,0),(4,0),(5,0),(6,0),(7,1),(8,0),(0,2),(2,4)]
        point_list2= [[(0,4),(4,4)],[(1,3)],[(2,4),(6,4),(6,0)],[(3,4)],[(0,4),(4,4),(8,4)],[(5,4)],[(2,4),(6,4)],[(7,3)],[(4,4),(8,4)],[(8,2)],[(6,4)]]
        blank_list = [(0,1),(0,3),(1,0),(1,4),(7,0),(7,4),(8,1),(8,3)]
        for col in range(COLS):
            for row in range(ROWS):
                point_list.append((row*SQUARE_SIZE + SQUARE_SIZE//2, col*SQUARE_SIZE + SQUARE_SIZE//2))
                
                # pygame.draw.rect(win,RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if (col,row) not in blank_list:
                    pygame.draw.circle(win, GREY, (row*SQUARE_SIZE + SQUARE_SIZE//2, col*SQUARE_SIZE + SQUARE_SIZE//2), radius= RADIUS)
                else:
                    continue

        for i in range(len(point_list1)):
            point1 = point_list1[i]
            point2_list= point_list2[i]
            for point2 in point2_list:
                self.draw_line(point1,point2,win)

                
        

    
    
                
        


    # def move(self, piece, row, col):
    #     self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col] ,self.board[piece.row][piece.col]
    #     piece.move(row,col)

    #     if row == ROWS or row ==0:
    #         piece.make_king()
    #         if piece.color == WHITE:
    #             self.white_kings +=1
    #         else:
    #             self.red_kings +=1

    # def get_piece(self, row, col):
    #     return self.board[row][col]

    # def create_board(self):
    #     for row in range(ROWS):
    #         self.board.append([])
    #         for col in range(COLS):
    #             if col %2 == ((row+1) %2):
    #                 if row<3:
    #                     self.board[row].append(Piece(row,col,WHITE))
    #                 elif row> 4:
    #                     self.board[row].append(Piece(row,col,RED))
    #                 else:
    #                     self.board[row].append(0)

    #             else:
    #                 self.board[row].append(0)


    # def draw(self,win):
    #     self.draw_squares(win)
    #     for row in range(ROWS):
    #         for col in range(COLS):
    #             piece = self.board[row][col]
    #             if piece != 0:
    #                 piece.draw(win)
                        


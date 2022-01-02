import pygame
import time
import solver 
import boards
pygame.init() #Initialize

screen = pygame.display.set_mode((800,800))
GAME_FONT = pygame.freetype.Font("fonts/UFont Sans Medium.ttf", 60)

board = boards.board #import board from boards file

#Name and icon
pygame.display.set_caption("Sudoku Solver")
icon = pygame.image.load("images/icons8-sudoku-64.png")
pygame.display.set_icon(icon)

#colors
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
white = (255,255,255)

#starting box coordinates (top left)
start_col_i = 103
start_row_i = 50

delay = 1 #determines speed of solving sudoku

def draw_board():
    # boarder
    side_left = 80
    side_right = 710
    height_down = 35
    height_up = 665
    pygame.draw.line(screen, black, (side_left, height_down), (side_right, height_down), width=5)
    pygame.draw.line(screen, black, (side_right, height_down), (side_right, height_up), width=5)
    pygame.draw.line(screen, black, (side_right, height_up), (side_left, height_up), width=5)
    pygame.draw.line(screen, black, (side_left, height_up), (side_left, height_down), width=5)

    #large squares
    pygame.draw.line(screen, black, (side_left + (70 * 3), height_up), (side_left + (70 * 3), height_down), width = 5)
    pygame.draw.line(screen, black, (side_left + (70 * 6), height_up), (side_left + (70 * 6), height_down), width = 5)
    pygame.draw.line(screen, black, (side_left, height_down + (70*3)), (side_right, height_down + (70* 3)), width = 5)
    pygame.draw.line(screen, black, (side_left, height_down + (70 * 6)), (side_right, height_down + (70 * 6)), width = 5)

    #individual squares (vertical)
    pygame.draw.line(screen, black, (side_left + (70 * 1), height_up), (side_left + (70 * 1), height_down), width = 2)
    pygame.draw.line(screen, black, (side_left + (70 * 2), height_up), (side_left + (70 * 2), height_down), width = 2)
    pygame.draw.line(screen, black, (side_left + (70 * 4), height_up), (side_left + (70 * 4), height_down), width = 2)
    pygame.draw.line(screen, black, (side_left + (70 * 5), height_up), (side_left + (70 * 5), height_down), width = 2)
    pygame.draw.line(screen, black, (side_left + (70 * 7), height_up), (side_left + (70 * 7), height_down), width = 2)
    pygame.draw.line(screen, black, (side_left + (70 * 8), height_up), (side_left + (70 * 8), height_down), width = 2)

    #individual squares (horizontal)
    pygame.draw.line(screen, black, (side_left, height_down + (70 * 1)), (side_right, height_down + (70 * 1)), width = 2)
    pygame.draw.line(screen, black, (side_left, height_down + (70 * 2)), (side_right, height_down + (70 * 2)), width = 2)
    pygame.draw.line(screen, black, (side_left, height_down + (70 * 4)), (side_right, height_down + (70 * 4)), width = 2)
    pygame.draw.line(screen, black, (side_left, height_down + (70 * 5)), (side_right, height_down + (70 * 5)), width = 2)
    pygame.draw.line(screen, black, (side_left, height_down + (70 * 7)), (side_right, height_down + (70 * 7)), width = 2)
    pygame.draw.line(screen, black, (side_left, height_down + (70 * 8)), (side_right, height_down + (70 * 8)), width = 2)

   
def print_numbers(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] != 0:
                GAME_FONT.render_to(screen, (start_col_i + (col * 70), start_row_i + (row * 70)), str(bo[row][col]), (0, 0, 0))

def set(row, col, i, color):
    GAME_FONT.render_to(screen, (start_col_i + (col * 70), start_row_i + (row * 70)), str(i), (0, 0, 0))

    cube_left = 80
    cube_right = 150
    cube_down = 35
    cube_up = 105
    pygame.draw.line(screen, color, (cube_left + (70 * col), cube_down + (70 * row)), (cube_right + (70 * col), cube_down + (70 * row)), width = 5)
    pygame.draw.line(screen, color, (cube_right + (70 * col), cube_down + (70 * row)), (cube_right + (70 * col), cube_up + (70 * row)), width = 5)
    pygame.draw.line(screen, color, (cube_left + (70 * col), cube_up + (70 * row)), (cube_right + (70 * col), cube_up + (70 * row)), width = 5)
    pygame.draw.line(screen, color, (cube_left + (70 * col), cube_down + (70 * row)), (cube_left + (70 * col), cube_up + (70 * row)), width = 5)

def erase(row, col):
    pygame.draw.rect(screen, white, pygame.Rect(start_col_i + (col * 70), start_row_i + (row * 70), 55, 55))

def solve(bo):

    find = solver.find_empty(bo)
    if not find:
        return True
    else: 
        row, col = find
    
    for i in range(1, 10):
        if solver.valid(bo, i, (row, col)):
            bo[row][col] = i
            erase(row, col)
            set(row, col, i, green)
            pygame.display.update()
            pygame.time.delay(delay)

            if solve(bo):
                return True

            bo[row][col] = 0
            erase(row, col)
            set(row, col, 0, red)
            pygame.display.update()
            pygame.time.delay(delay)
    
    return False

#pygame while loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    draw_board()

    print_numbers(boards.board)

    if solve(boards.board):
        GAME_FONT.render_to(screen, (80, 710), "Solved!", (0, 0, 0))
    else:
        GAME_FONT.render_to(screen, (80, 710), "Impossible to Solve", (0, 0, 0))

    pygame.display.update()

    

pygame.quit()
quit()
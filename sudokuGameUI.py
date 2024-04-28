import pygame
import Components
import sudokuGen

COLOR_PURPLE:tuple[int, int, int] = (101, 33, 255)
WIN_WIDTH:int = 700
WIN_HEIGHT:int = 700

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Client")
clientNumber = 0
Gen = sudokuGen.SudoGrid()
grid = Gen.getGrid()


"""
def main():
    run = True
    win.fill(COLOR_PURPLE)
    clock = pygame.time.Clock();
    btn = Components.Button("hello", 100, 100, 75, 50, (255,00,0))
    g = Components.Grid(grid,(10,10), win)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                g.click(pos)
            if event.type == pygame.KEYDOWN:
                g.key_event(event)
        pygame.display.update()
main()
"""

Menu = Components.Menu(win)

Menu.main()

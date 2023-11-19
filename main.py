import pygame
import ChessEngine

WIDTH = 512 
HEIGHT = 512 
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(f'assets/{piece}.png'), (SQ_SIZE, SQ_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    game = ChessEngine.GameState()
    load_images()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

        drawGameState(screen, game)

        clock.tick(MAX_FPS)
        pygame.display.flip()

def drawGameState(screen, game):
    drawBoard(screen)
    drawPieces(screen, game.board)

def drawBoard(screen):
    colors = [pygame.Color('white'), pygame.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece!= '--':
                screen.blit(IMAGES[piece], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == '__main__':
    main()
import sys
import pygame

class Maze:
    def __init__(self, grid, start):
        self.grid = grid
        self.start = start

class Agente:
    def __init__(self, start_position):
        self.position = start_position

# Define o labirinto, agente e direção dos movimentos
maze = Maze([
    ['S', 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'G'],
], (0, 0))

agent = Agente(maze.start)

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
path = []

# Recursão/Ação do agente
def walk(maze, agente, curr):
    grid = maze.grid

    if (curr[0] < 0 or curr[0] >= len(grid) or
        curr[1] < 0 or curr[1] >= len(grid[0]) or
        grid[curr[0]][curr[1]] == 1 or
        grid[curr[0]][curr[1]] == 2):
        return None

    if grid[curr[0]][curr[1]] == 'G':
        path.append(curr)
        return path

    path.append(curr)
    grid[curr[0]][curr[1]] = 2  # Marca como visitado

    pygame.event.pump()  # Processa eventos para garantir que a tela atualize
    draw_maze(screen, maze, False)  # Passa False para visualização normal
    pygame.display.flip()
    pygame.time.delay(50)  # Ajuste o tempo para a visualização desejada

    for dir in dirs:
        next_step = (curr[0] + dir[0], curr[1] + dir[1])
        result = walk(maze, agente, next_step)
        if result:
            return result

    path.pop()
    grid[curr[0]][curr[1]] = 0  # Desmarca a visita para outras tentativas
    return None

# Configurações do Pygame
pygame.init()
cell_size = 40
cols, rows = len(maze.grid[0]), len(maze.grid)
width, height = cols * cell_size, rows * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Solver")

colors = {
    'wall': (0, 0, 0),
    'path': (255, 255, 255),
    'start': (235, 207, 52),
    'goal': (7, 237, 42),
    'visited': (100, 100, 255),
    'impossible': (255, 0, 0)
}

def draw_maze(screen, maze, impossible):
    for y, row in enumerate(maze.grid):
        for x, cell in enumerate(row):
            if (x, y) == maze.start:
                color = colors['start']
            elif impossible:
                if cell in [0, 2]:  # Células relevantes
                    color = colors['impossible']  # Cor vermelha para células
                elif cell in ['G']:
                    color = colors['goal']
                else:
                    color = colors['wall']
            else:
                if cell == 1:
                    color = colors['wall']
                elif cell == 0:
                    color = colors['path']
                elif cell == 'S':
                    color = colors['start']
                elif cell == 'G':
                    color = colors['goal']
                elif cell == 2:
                    color = colors['visited']
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))


# Roda o programa
running = True
final_path = walk(maze, agent, agent.position)
impossible = final_path is None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    draw_maze(screen, maze, impossible)

    if impossible:
        font = pygame.font.Font(None, 74)
        text = font.render("Solução não encontrada!", True, (255, 255, 255))
        screen.blit(text, (width // 4, height // 2))

    pygame.display.flip()

pygame.quit()
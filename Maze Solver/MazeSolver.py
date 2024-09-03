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
    [0, 1, 0, 0, -1, 0, 1, 0, 0, -1],
    [0, -1, 1, 0, 0, 0, -1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, -1, 0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, -1, 1, 0, 0, 0, -1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, -1, 0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
], (0, 0))

agent = Agente(maze.start)

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
path = []
moveCounter = 0


# Recursão/Ação do agente
def findPath(maze, agente, curr):
    grid = maze.grid
    if (curr[0] < 0 or curr[0] >= len(grid) or
        curr[1] < 0 or curr[1] >= len(grid[0]) or
        grid[curr[0]][curr[1]] == 1 or
        grid[curr[0]][curr[1]] == 2):
        return None

    if grid[curr[0]][curr[1]] == -1:
        path.append(curr)
        walk(grid)
        return path

    path.append(curr)
    grid[curr[0]][curr[1]] = 2  # Marca como visitado

    pygame.event.pump()  # Processa eventos para garantir que a tela atualize
    draw_maze(screen, maze, False)  # Passa False para visualização normal
    pygame.display.flip()

    for dir in dirs:
        next_step = (curr[0] + dir[0], curr[1] + dir[1])
        result = findPath(maze, agente, next_step)
        if result:
            return result

    if len(path) > 0:
        path.pop()
    else:
        return None
    return None

def walk(grid):
    chkPoint = path[len(path) - 1]
    print(path)
    print('chk: ', chkPoint)
    for step in path:
        grid[step[0]][step[1]] = 3
        pygame.event.pump()
        draw_maze(screen, maze, False)
        pygame.display.flip()
        pygame.time.delay(10)
        prev = step
        grid[prev[0]][prev[1]] = 0
    path.clear()
    clearVisited()
    findPath(maze, agent, chkPoint)

def clearVisited():
    for cell in maze.grid:
        if maze.grid[cell[0]][cell[1]] == 2:
            maze.grid[cell[0]][cell[1]] = 0
# Configurações do Pygame
pygame.init()
cell_size = 40
cols, rows = len(maze.grid[0]), len(maze.grid)
width, height = cols * cell_size, rows * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aspirador")

colors = {
    'wall': (0, 0, 0),
    'path': (255, 255, 255),
    'start': (235, 207, 52),
    'dirt': (88, 36, 72),
    'visited': (255, 255, 255),
    'clean': (255, 0, 0),
    'agent': (100, 100, 255)
}

def draw_maze(screen, maze, clean):
    for y, row in enumerate(maze.grid):
        for x, cell in enumerate(row):
            if (x, y) == maze.start:
                color = colors['start']
            elif clean:
                if cell in [0, 2]:  # Células relevantes
                    color = colors['path']
                elif cell in [-1]:
                    color = colors['dirt']
                else:
                    color = colors['wall']
            else:
                if cell == 1:
                    color = colors['wall']
                elif cell == 0:
                    color = colors['path']
                elif cell == 'S':
                    color = colors['start']
                elif cell == -1:
                    color = colors['dirt']
                elif cell == 2:
                    color = colors['visited']
                elif cell == 3:
                    color = colors['agent']
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))


# Roda o programa
running = True
final_path = findPath(maze, agent, agent.position)
clean = final_path is None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    draw_maze(screen, maze, clean)

    if clean:
        font = pygame.font.Font(None, 74)
        text = font.render("Limpo!", True, (0, 255, 0))
        screen.blit(text, (width // 4, height // 2.5))

    pygame.display.flip()

pygame.quit()
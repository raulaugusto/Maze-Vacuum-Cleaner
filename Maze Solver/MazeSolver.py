import sys
import pygame
from collections import deque

class Maze:
    def __init__(self, grid, start):
        self.grid = grid
        self.start = start

class Agente:
    def __init__(self, start_position):
        self.position = start_position

# Define o labirinto, agente e direção dos movimentos
maze = Maze([
    [0, 1, 0, 0, -1, 0, 1, 0, 0, 0, 0, 1, 0, 0, -1, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, -1, 0, 0, 1, 0, 1, 0, 0, 0, 0, -1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, -1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, -1, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, -1, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0],
    [0, 0, -1, 1, 0, 0, 0, 0, -1, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, -1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, -1],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, -1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, -1, 0, 0, 1, 0, 1, 0, 0, 0, 0, -1, 0]
], (7, 7))

agent = Agente(maze.start)

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
path = []
moveCounter = 0


def findPath(maze, agente, start):
    global moveCounter  # Declara que moveCounter é global
    grid = maze.grid
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if grid[x][y] == -1:
            walk(grid, path)

        grid[x][y] = 2  # Marca como visitado

        pygame.event.pump()  # Processa eventos para garantir que a tela atualize
        draw_maze(screen, maze, False)  # Passa False para visualização normal
        pygame.display.flip()

        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 0 or grid[nx][ny] == -1:
                    queue.append(((nx, ny), path))
    print(moveCounter)
    return None


def walk(grid, path):
    global moveCounter  # Declara que moveCounter é global
    chkPoint = path[-1]  # último ponto de sujeira encontrado
    print(path)
    print('chk: ', chkPoint)

    for step in path:
        moveCounter = moveCounter + 1
        grid[step[0]][step[1]] = 3  # marca a célula como limpa
        pygame.event.pump()
        draw_maze(screen, maze, False)
        pygame.display.flip()
        pygame.time.delay(180)
        prev = step
        grid[prev[0]][prev[1]] = 0  # redefine para caminho

        # Verifica se o contador de movimentos atingiu 30
        if moveCounter >= 30:
            # Move o agente de volta ao início
            agent.position = maze.start
            grid = maze.grid  # Reseta o grid para o estado inicial
            moveCounter = 0  # Reseta o contador de movimentos
            path.clear()  # Limpa o caminho atual
            clearVisited()  # Limpa células visitadas
            return findPath(maze, agent, agent.position)  # Recomeça a busca

    path.clear()  # Limpa o caminho atual
    clearVisited()  # Limpa células visitadas

    # Verifica se ainda há sujeira no labirinto
    if any(-1 in row for row in grid):
        findPath(maze, agent, chkPoint)  # Continua a partir do último ponto
    else:
        print("Labirinto limpo!")  # Quando não há mais sujeira


def clearVisited():
    for y in range(len(maze.grid)):
        for x in range(len(maze.grid[0])):
            if maze.grid[y][x] == 2:  # Se a célula foi visitada
                maze.grid[y][x] = 0  # Redefine para caminho

# Configurações do Pygame
pygame.init()
cell_size = 40
cols, rows = len(maze.grid[0]), len(maze.grid)
width, height = cols * cell_size, rows * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aspirador")

colors = {
    'wall': (59, 58, 57),
    'path': (255, 255, 255),
    'start': (235, 207, 52),
    'dirt': (97, 68, 39),
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
    # Desenha o contador de movimentos
    font = pygame.font.Font(None, 36)
    counter_text = font.render(f"Movimentos: {moveCounter}", True, (68, 219, 108))
    screen.blit(counter_text, (10, height - 40))

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
        screen.blit(text, (width // 2.7, height // 2))

    pygame.display.flip()

pygame.quit()

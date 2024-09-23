# Maze Cleaner with Pygame

## Descrição do Projeto

Este projeto implementa um simulador de um agente autônomo que navega em um labirinto para limpar áreas sujas. O labirinto é composto por células que podem representar paredes, caminhos limpos, ou sujeira. O agente segue um caminho para limpar todas as células sujas enquanto exibe a simulação visualmente usando a biblioteca **Pygame**.

O código contém:
- Um labirinto onde o agente navega.
- Um agente que se move pelo labirinto limpando as células sujas.
- Um contador de movimentos que limita a quantidade de ações do agente, exigindo que ele retorne ao ponto de partida após 30 movimentos.
- Interface gráfica para visualizar o labirinto, os movimentos do agente e o estado das células.

## Como Funciona

1. **Labirinto**: É representado por uma matriz onde:
   - `0`: Caminho livre
   - `1`: Parede
   - `-1`: Sujeira
   - `2`: Célula visitada
   - `3`: Célula limpa

2. **Agente**: O agente começa no ponto inicial definido e percorre o labirinto em busca de células sujas. O caminho é encontrado usando uma abordagem de busca em largura (BFS). Quando o agente limpa uma célula, o valor é alterado de `-1` para `3`. Se o agente atingir 30 movimentos, ele retorna ao ponto inicial e reseta o grid.

3. **Contador de Movimentos**: O agente realiza até 30 movimentos antes de retornar ao ponto inicial. O contador é exibido na interface gráfica, e ao atingir o limite, o agente volta à posição inicial para reiniciar a busca.

4. **Simulação com Pygame**: O labirinto é desenhado usando blocos retangulares, onde cada célula do grid tem uma cor diferente de acordo com seu estado (parede, caminho, sujeira, etc.). O contador de movimentos também é exibido na tela, e, quando todo o labirinto estiver limpo, a mensagem "Limpo!" aparece.

## Estrutura do Código

- **Maze**: Classe que representa o labirinto, inicializado com um grid e a posição inicial do agente.
- **Agente**: Classe que representa o agente de limpeza, responsável por mover-se pelo labirinto.
- **findPath**: Função que busca células sujas no labirinto usando busca em largura (BFS). Marca o caminho percorrido e chama a função `walk` para limpar as células encontradas.
- **walk**: Função que move o agente ao longo do caminho até a célula suja e limpa o labirinto. Verifica o contador de movimentos e decide quando o agente deve voltar ao início.
- **clearVisited**: Função que reseta o grid, removendo as marcas de células visitadas após o agente retornar ao ponto inicial.
- **draw_maze**: Função responsável por desenhar o estado atual do labirinto na interface gráfica usando Pygame.

## Como Executar o Código

### Pré-requisitos

- Python 3.x
- Biblioteca Pygame

### Instalação do Pygame

Para instalar a biblioteca **Pygame**, execute:

```bash
pip install pygame
```

### Executando o Projeto

1. Clone este repositório ou faça o download dos arquivos.
2. Execute o script principal:

```bash
python main.py
```

A simulação abrirá uma janela mostrando o labirinto e o agente realizando a limpeza.

## Controles e Interação

- **Fechar Janela**: Para finalizar a simulação, basta fechar a janela ou pressionar "Alt + F4".
- **Visualização do Processo**: O agente limpa as células sujas de forma automática. O número de movimentos do agente é exibido no canto inferior esquerdo.

## Personalização

- Você pode modificar o layout do labirinto alterando a matriz `grid` na classe `Maze`. Exemplo:
  
```python
maze = Maze([
    [0, 1, 0, -1],  # Exemplo de labirinto 4x4
    [0, 1, 0, 0],
    [0, 1, -1, 1],
    [0, 0, 0, 0]
], (0, 0))  # Posição inicial do agente
```

- Altere o número máximo de movimentos antes do retorno ao ponto inicial ajustando o valor de `moveCounter`.

## Funcionalidades Futuras

- Implementação de múltiplos agentes para limpar diferentes partes do labirinto ao mesmo tempo.
- Adição de obstáculos dinâmicos e interação com múltiplas áreas sujas.

## Contribuições

Contribuições são bem-vindas! Para contribuir:
1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b minha-nova-funcionalidade`).
3. Faça as modificações e adicione commits.
4. Envie um pull request.

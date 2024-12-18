import pygame
import sys
import random
from graph import *

pygame.init()

LINE_WIDTH = 1
LINE_COLOR = (255, 255, 255)
CIRCLE_COLOR = (238, 36, 0)
CROSS_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (28, 170, 156)

class Screen:
    def __init__(self):
        self.height = 600  # Corrected typo
        self.width = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.run = True
        self.search_algo = None
        self.font = pygame.font.SysFont('Segoe Print', 30)
        self.graph = pygame.image.load(r"""images\graph.png""")
        self.usc = pygame.image.load(r"""images\ucs.png""")
        self.dfs = pygame.image.load(r"""images\dfs.png""")
        self.dls = pygame.image.load(r"""images\dls.png""")
        self.a_star = pygame.image.load(r"""images\a_star.png""")
        self.ids = pygame.image.load(r"""images\a_star.png""")
        self.gcs =pygame.image.load(r"""images\gcs.png""")
        self.LINE_COLOR = ['White', 'White', 'White', 'White', 'White', 'White', 'White']
        self.graph_shown = False
        self.bds = pygame.image.load(r"""images\bds.png""")
        self.rectangles = [
            pygame.Rect(50, 50, 500, 50),   
            pygame.Rect(50, 120, 500, 50),  
            pygame.Rect(50, 190, 500, 50),  
            pygame.Rect(50, 260, 500, 50),  
            pygame.Rect(50, 330, 500, 50),  
            pygame.Rect(50, 400, 500, 50),  
            pygame.Rect(50, 470, 500, 50)
        ]
        self.text_list = [
            "Breadth First Search",
            "Uniform Cost Search",
            "Depth-first search (DFS)",
            "Depth-limited search",
            "Iterative Deepening Search",
            "A* Search",
            "Greedy Best First Algorithm"
        ]
        self.clock = pygame.time.Clock()

    def draw_graph(self):
        self.screen.fill('Black')
        self.draw_random_dots()
        if self.search_algo == 0:
            self.screen.blit(self.bds,(80,0))
            print('super done')
        if self.search_algo == 1:
            self.screen.blit(self.usc,(80,0))
        if self.search_algo == 2:
            self.screen.blit(self.dfs,(80,0))
        if self.search_algo == 3:
            self.screen.blit(self.dls,(80,0))
        if self.search_algo == 4:
            self.screen.blit(self.dls,(80,0))
        if self.search_algo == 5:
            self.screen.blit(self.a_star,(80,0))
        if self.search_algo == 6:
            self.screen.blit(self.gcs,(80,0))
        pygame.display.flip()
    def draw_random_dots(self):
        for _ in range(100):  # Number of dots
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            
            # Skip drawing dots inside any rectangle
            skip_dot = False
            for rect in self.rectangles:
                if rect.collidepoint(x, y):
                    skip_dot = True
                    break
            if not skip_dot:
                pygame.draw.circle(self.screen, 'White', (x, y), 1)

    def draw_path(self, path):
        if not path:
            return
        
        # Define starting point for circles
        start_x = 300
        start_y = 30
        spacing = 80  # Space between circles

        for i, text in enumerate(path):
            # Calculate the position for each circle
            point = (start_x, start_y + i * spacing)

            # Draw a circle around the point
            pygame.draw.circle(self.screen, CIRCLE_COLOR, point, 30)  # Increased radius for text visibility
            font = pygame.font.SysFont('arabic.ttf', 30)
            # Render the text inside the circle
            rendered_text = font.render(text, False, 'White')
            text_rect = rendered_text.get_rect(center=point)
            self.screen.blit(rendered_text, text_rect)

            # Draw lines to the next point
            if i < len(path) - 1:
                next_point = (start_x, start_y + (i + 1) * spacing)
                # Draw a vertical line to the next point
                pygame.draw.line(self.screen, LINE_COLOR[i % len(LINE_COLOR)], point, next_point, LINE_WIDTH)

    def buttons(self):
        for i, rect in enumerate(self.rectangles):
            pygame.draw.rect(self.screen, self.LINE_COLOR[i], rect, 3)
    
    def collision(self):
        for i, rect in enumerate(self.rectangles):
            if rect.collidepoint(self.mouse_x, self.mouse_y):
                pygame.draw.rect(self.screen, 'Green', rect, 3)
                return True, i
            else:
                pygame.draw.rect(self.screen, self.LINE_COLOR[i], rect, 3)
        pygame.display.flip()
        return False, None

    def show_graph(self):
        self.screen.fill('Black')
        self.draw_random_dots()
        self.screen.blit(self.graph, (80, 0))
        pygame.display.update()

    def text(self):
        text_rectangles = [
            pygame.Rect(100, 50, 500, 50),   
            pygame.Rect(100, 120, 500, 50),  
            pygame.Rect(100, 190, 500, 50),  
            pygame.Rect(100, 260, 500, 50),  
            pygame.Rect(100, 330, 500, 50),  
            pygame.Rect(100, 400, 500, 50),  
            pygame.Rect(100, 470, 500, 50)
        ]
        
        for i, text in enumerate(self.text_list):
            rendered_text = self.font.render(text, True, 'White')
            text_rect = text_rectangles[i]
            self.screen.blit(rendered_text, text_rect)

        in_bound, index = self.collision()
        if in_bound:
            rendered_text = self.font.render(self.text_list[index], True, 'Green')
            text_rect = text_rectangles[index]
            self.screen.blit(rendered_text, text_rect)
        pygame.display.flip()

    def algo_screen(self):
        self.screen2 = pygame.display.set_mode((self.width, self.height))
        self.draw_graph()

    def main_loop(self):
        self.draw_random_dots()  
        while self.run:
            if self.search_algo is None:
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                    
                self.buttons()  # Draw rectangles
                self.text()  # Draw text and handle rectangle clicks
                
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    collide, self.search_algo = self.collision()
                    
                    if collide:
                        if self.graph_shown:

                            self.algo_screen()
                        if not self.graph_shown:
                            self.show_graph()
                            self.graph_shown = True
                            print('why')
                        
                        
                        
              # Show graph only if graph_shown is True

            self.clock.tick(60)
            pygame.display.flip()  # Update the display

# Initialize and run the main loop
screen1 = Screen()
screen1.main_loop()

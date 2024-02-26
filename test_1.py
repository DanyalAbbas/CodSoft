import pygame
import sys

# Initialize Pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("To-Do List")

# Fonts
font = pygame.font.Font(None, 30)

# To-Do List
tasks = ["get bitches","ou"]

def draw_tasks():
    for i, task in enumerate(tasks):
        text = font.render(task, True, (0,0,0))
        screen.blit(text, (20, 40 + i * 40))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Add a new task when Enter key is pressed
                task_input = input("Enter task: ")
                tasks.append(task_input)

    # Clear the screen
    screen.fill((255,255,255))

    # Draw tasks
    draw_tasks()

    # Update the display
    pygame.display.flip()

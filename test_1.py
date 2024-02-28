import pygame
import sys
import webbrowser

# Initialize Pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("To-Do List")

# Fonts
font = pygame.font.Font(None, 30)

# To-Do List
clock = pygame.time.Clock()
tasks = ["hello","nah", "yo", "usu"]

def draw_tasks(tasks):
    for pos, task in enumerate(tasks):
        text = font.render(task, True, (0,0,0))
        screen.blit(text, (20, 80 + pos * 40))
        create_button(screen, 130, 77 + pos * 40, 40, 25, (0,225,0), "freesansbold.ttf", 12, (0,195,0), "DONE", (255,255,255), lambda: tasks.pop(pos)  )


def create_button(screen, x, y, width, height, def_color, textfont, size, hover_color, text, text_color, action):
        font = pygame.font.Font(textfont, size)
        button_rect = pygame.Rect(x, y, width, height)
        button_color = hover_color if button_rect.collidepoint(pygame.mouse.get_pos()) else def_color

        pygame.draw.rect(screen, button_color, button_rect)
        pygame.draw.rect(screen, (0,0,0), button_rect, 2)

        button_text = font.render(text, True, text_color)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

        if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            action()
            clock.tick(5)

def screen_changer():
    global main_menu
    main_menu = False


# Main loop
main_menu = True
credit_img = pygame.image.load("Assets/credits.png")
credit_rect = pygame.Rect(-3, -40, 120, 90)
main_font = pygame.font.Font("freesansbold.ttf", 50)
main_text = main_font.render("TO-DO LIST", True, (255,255,255))

while True:
    if main_menu:
        screen.fill((0,0,0))

        screen.blit(main_text, (260,150))
        screen.blit(pygame.transform.scale(credit_img, (150, 150)), (-3, -40))
        create_button(screen, 300, 220, 100, 50, (0,0,225), "freesansbold.ttf", 30, (0,0,195), "Start", (255,255,255), screen_changer )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if credit_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed:
                    webbrowser.open("https://github.com/DanyalAbbas")
    else:
        clock.tick(60)
        screen.fill((255,255,255))
        create_button(screen, 630, 30, 150, 50, (225,0,0), "freesansbold.ttf", 25, (195,0,0), "CLEAR ALL", (255,255,255), lambda : tasks.clear())

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
        

        # Draw tasks
        draw_tasks(tasks)

    # Update the display
    pygame.display.flip()

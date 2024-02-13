# # import pygame
# # import time
# # import random
# #
# # pygame.init()
# #
# # # Window dimensions
# # window_width = 800
# # window_height = 600
# #
# # # Colors
# # white = (255, 255, 255)
# # black = (0, 0, 0)
# # red = (213, 50, 80)
# # green = (0, 255, 0)
# # blue = (50, 153, 213)
# #
# # # Snake block size
# # block_size = 20
# # snake_speed = 20
# #
# # # Font
# # font_style = pygame.font.SysFont(None, 50)
# #
# # # Create a window
# # window = pygame.display.set_mode((window_width, window_height))
# # pygame.display.set_caption('Snake Game')
# #
# # # Clock
# # clock = pygame.time.Clock()
# #
# # # Snake
# # snake_block = 20
# # snake_list = []
# #
# #
# # def our_snake(snake_block, snake_list):
# #     for x in snake_list:
# #         pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])
# #
# #
# # def message(msg, color):
# #     mesg = font_style.render(msg, True, color)
# #     window.blit(mesg, [window_width / 6, window_height / 3])
# #
# #
# # def game_loop():
# #     global snake_length
# #     snake_length = 1
# #
# #     game_over = False
# #     game_close = False
# #
# #     x1 = window_width / 2
# #     y1 = window_height / 2
# #
# #     x1_change = 0
# #     y1_change = 0
# #
# #     food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
# #     food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
# #
# #     while not game_over:
# #
# #         while game_close == True:
# #             window.fill(blue)
# #             message("You Lost! Press Q-Quit or C-Play Again", red)
# #             pygame.display.update()
# #
# #             for event in pygame.event.get():
# #                 if event.type == pygame.KEYDOWN:
# #                     if event.key == pygame.K_q:
# #                         game_over = True
# #                         game_close = False
# #                     if event.key == pygame.K_c:
# #                         game_loop()
# #
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 game_over = True
# #             if event.type == pygame.KEYDOWN:
# #                 if event.key == pygame.K_LEFT:
# #                     x1_change = -block_size
# #                     y1_change = 0
# #                 elif event.key == pygame.K_RIGHT:
# #                     x1_change = block_size
# #                     y1_change = 0
# #                 elif event.key == pygame.K_UP:
# #                     y1_change = -block_size
# #                     x1_change = 0
# #                 elif event.key == pygame.K_DOWN:
# #                     y1_change = block_size
# #                     x1_change = 0
# #
# #         if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
# #             game_close = True
# #         x1 += x1_change
# #         y1 += y1_change
# #         window.fill(blue)
# #         pygame.draw.rect(window, green, [food_x, food_y, block_size, block_size])
# #         snake_head = []
# #         snake_head.append(x1)
# #         snake_head.append(y1)
# #         snake_list.append(snake_head)
# #         if len(snake_list) > snake_length:
# #             del snake_list[0]
# #
# #         for x in snake_list[:-1]:
# #             if x == snake_head:
# #                 game_close = True
# #
# #         our_snake(block_size, snake_list)
# #         pygame.display.update()
# #
# #         if x1 == food_x and y1 == food_y:
# #             food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
# #             food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
# #             snake_length += 1
# #
# #         clock.tick(snake_speed)
# #
# #     pygame.quit()
# #     quit()
# #
# #
# # game_loop()
#
#
# import pygame
# import random
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the window
# window_width = 800
# window_height = 600
# window = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("Blocks Game")
#
# # Define colors
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
#
# # Define block parameters
# block_width = 50
# block_height = 50
# block_speed = 5
#
# # Create a clock object to control the frame rate
# clock = pygame.time.Clock()
#
# # Function to draw a block
# def draw_block(x, y, color):
#     pygame.draw.rect(window, color, [x, y, block_width, block_height])
#
# # Main game loop
# def game_loop():
#     # Initial position of the block
#     x_block = window_width / 2 - block_width / 2
#     y_block = window_height / 2 - block_height / 2
#
#     # Movement direction of the block (initially stopped)
#     x_change = 0
#     y_change = 0
#
#     # Main loop flag
#     game_over = False
#
#     while not game_over:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             elif event.type == pygame.KEYDOWN:
#                 # Move the block based on arrow key input
#                 if event.key == pygame.K_LEFT:
#                     x_change = -block_speed
#                 elif event.key == pygame.K_RIGHT:
#                     x_change = block_speed
#                 elif event.key == pygame.K_UP:
#                     y_change = -block_speed
#                 elif event.key == pygame.K_DOWN:
#                     y_change = block_speed
#
#         # Clear the window
#         window.fill(white)
#
#         # Update block position
#         x_block += x_change
#         y_block += y_change
#
#         # Draw the block
#         draw_block(x_block, y_block, blue)
#
#         # Check if the block is going out of the window boundaries
#         if x_block < 0 or x_block + block_width > window_width or y_block < 0 or y_block + block_height > window_height:
#             game_over = True
#
#         # Refresh the display
#         pygame.display.update()
#
#         # Set the frame rate
#         clock.tick(60)
#
#     pygame.quit()
#     quit()
#
# # Start the game
# game_loop()

##
#
#
#
# game ---3

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Block Breaker")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define block parameters
block_width = 75
block_height = 20

# Ball parameters
ball_radius = 10
ball_speed = 5

# Paddle parameters
paddle_width = 100
paddle_height = 20
paddle_speed = 10

# Font
font_style = pygame.font.SysFont(None, 50)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Function to draw a block
def draw_block(x, y, color):
    pygame.draw.rect(window, color, [x, y, block_width, block_height])

# Function to draw the paddle
def draw_paddle(x, y, color):
    pygame.draw.rect(window, color, [x, y, paddle_width, paddle_height])

# Function to draw the ball
def draw_ball(x, y, color):
    pygame.draw.circle(window, color, (x, y), ball_radius)

# Function to display "Game Over" message and "Start Over" button
def game_over_message():
    message = font_style.render("Game Over", True, red)
    window.blit(message, [window_width / 3, window_height / 3])
    start_over_button = font_style.render("Start Over", True, green)
    window.blit(start_over_button, [window_width / 3, window_height / 2])

# Main game loop
def game_loop():
    # Initial position of the paddle
    paddle_x = window_width / 2 - paddle_width / 2
    paddle_y = window_height - 2 * paddle_height

    # Initial position of the ball
    ball_x = window_width // 2
    ball_y = window_height // 2
    ball_dx = random.choice([-1, 1]) * ball_speed
    ball_dy = -ball_speed

    # Blocks
    blocks = []
    block_colors = [red, green, blue]
    for i in range(6):
        for j in range(5):
            blocks.append([j * (block_width + 5) + 30, i * (block_height + 5) + 50, random.choice(block_colors)])

    # Main loop flag
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Clear the window
        window.fill(white)

        # Draw blocks
        for block in blocks:
            draw_block(block[0], block[1], block[2])

        # Draw the paddle
        draw_paddle(paddle_x, paddle_y, black)

        # Draw the ball
        draw_ball(ball_x, ball_y, black)

        # Update ball position
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collisions with window boundaries
        if ball_x <= ball_radius or ball_x >= window_width - ball_radius:
            ball_dx *= -1
        if ball_y <= ball_radius:
            ball_dy *= -1

        # Ball collisions with paddle
        if ball_y >= paddle_y - ball_radius and paddle_x <= ball_x <= paddle_x + paddle_width:
            ball_dy *= -1

        # Ball collisions with blocks
        for block in blocks:
            if block[0] <= ball_x <= block[0] + block_width and block[1] <= ball_y <= block[1] + block_height:
                ball_dy *= -1
                blocks.remove(block)
                break

        # Check if the ball is lost
        if ball_y >= window_height:
            game_over = True

        # Move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < window_width - paddle_width:
            paddle_x += paddle_speed

        # Refresh the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(60)

    # Display "Game Over" message and "Start Over" button
    game_over_message()

    # Check for "Start Over" button click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if window_width / 3 <= mouse_x <= window_width / 3 + 200 and window_height / 2 <= mouse_y <= window_height / 2 + 50:
                    game_loop()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# Start the game
game_loop()

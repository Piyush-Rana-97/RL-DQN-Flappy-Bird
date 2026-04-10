import gymnasium as gym
import flappy_bird_gymnasium
import pygame

# Create our env
env = gym.make("FlappyBird-v0", render_mode = "human")
state, info = env.reset()
done = False

# Initilize PyGame Keyword
pygame.init()
screen = pygame.display().get_surface()  # Gymnasium has already created a window

while not done:
    action = 0 # default -> 0 is no flip & 1 is flip
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                action = 1 # Flip
    
    state, reward, done, truncated, info = env.step(action)
    env.render()

env.close()
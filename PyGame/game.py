
import pygame , sys
def draw_floor():
    screen.blit(floor,(floor_x_pos,600))
    screen.blit(floor,(floor_x_pos+432,600))
def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop =(500,384))
    return new_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)

pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
gravity = 0.25
bird_movement = 0

#background
bg = pygame.image.load("FileGame/assets/background-night.png").convert()
bg = pygame.transform.scale2x(bg)
#sàn
floor = pygame.image.load("FileGame/assets/floor.png").convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#bird
bird = pygame.image.load("FileGame/assets/yellowbird-downflap.png").convert()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,384))
#pipe
pipe_surface = pygame.image.load("FileGame/assets/pipe-green.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
#time
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement =  -11
        if event.type == spawnpipe:
            pipe_list.append(create_pipe())
            print(create_pipe)
    screen.blit(bg,(0,0))
    #bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird,bird_rect)
    #pipe
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    #floor
    screen.blit(floor,(floor_x_pos,600))
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)
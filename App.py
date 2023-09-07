from zeno_paradoxes import *
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
X = 640
Y = 480

pygame.display.set_caption("Zeno Paradoxes")
background = pygame.Surface(screen.get_size())

"""Start screen"""
def start():
    font = pygame.font.Font(None, 36)
    background.fill((255, 255, 255))

    text = font.render("Zeno Paradoxes", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    text = font.render("1. Achille vs Tortue", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - 100
    background.blit(text, textpos)

    text = font.render("2. Dichotomie", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    text = font.render("3. Flying Arrow", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery + 100
    background.blit(text, textpos)

    text = font.render("Press a key number to start", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery + 200
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

"""Display Achille vs Tortue: Paradoxe 1"""
def display_achille_vs_tortue():

    """Achille and Turtoise sprite loading"""
    achille = pygame.image.load("sprites/achille.png").convert_alpha()
    achille = pygame.transform.scale(achille, (32, 32))
    turtoise = pygame.image.load("sprites/turtoise.png").convert_alpha()
    turtoise = pygame.transform.scale(turtoise, (32, 32))

    step = 0
    while step < 10:
        step += 1
        background.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        """Step's text drawing"""
        text_step = font.render(f"Step: {step}", 1, (10, 10, 10))
        text_step_pos = text_step.get_rect()
        text_step_pos.centerx = background.get_rect().centerx
        text_step_pos.centery = background.get_rect().centery - 50
        background.blit(text_step, text_step_pos)
        screen.blit(background, (0, 0))

        """Achille's position text drawing"""
        text_achille = font.render(f"Achille's position: {paradoxe_1.object_pos} m", 1, (10, 10, 10))
        text_achille_pos = text_achille.get_rect()
        text_achille_pos.centerx = background.get_rect().centerx
        text_achille_pos.centery = background.get_rect().centery + 100
        background.blit(text_achille, text_achille_pos)
        screen.blit(background, (0, 0))

        """Turtoise's position text drawing"""
        text_turtoise = font.render(f"Turtoise's position: {paradoxe_1.target_pos} m", 1, (0, 255, 0))
        text_turtoise_pos = text_turtoise.get_rect()
        text_turtoise_pos.centerx = background.get_rect().centerx
        text_turtoise_pos.centery = background.get_rect().centery + 150
        background.blit(text_turtoise, text_turtoise_pos)
        screen.blit(background, (0, 0))

        """Achille and Turtoise sprite drawing"""
        screen.blit(achille, (paradoxe_1.object_pos * 3, 50))
        screen.blit(turtoise, (paradoxe_1.target_pos * 3, 100))
        pygame.display.update()
        
        """Achille's position and Turtoise's position movement"""        
        distance = paradoxe_1.target_pos - paradoxe_1.object_pos
        delta =  distance / paradoxe_1.object_speed
        paradoxe_1.object_pos = paradoxe_1.target_pos
        paradoxe_1.target_pos = paradoxe_1.object_pos + paradoxe_1.target_speed * delta

        pygame.time.Clock().tick(1)
    
def display_dichotomie():

    """rock and tree sprite loading"""
    rock = pygame.image.load("sprites/rock.png").convert_alpha()
    rock = pygame.transform.scale(rock, (50, 50))
    tree = pygame.image.load("sprites/tree.png").convert_alpha()
    tree = pygame.transform.scale(tree, (150, 200))

    step = 0
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    paradoxe_2.target_pos = paradoxe_2.target_pos + 350
    while step < 10:
        step += 1
        
        font = pygame.font.Font(None, 36)

        """Step's text drawing"""
        text_step = font.render(f"Step: {step}", 1, (10, 10, 10))
        text_step_pos = text_step.get_rect()
        text_step_pos.centerx = background.get_rect().centerx
        text_step_pos.centery = background.get_rect().centery + 50
        background.blit(text_step, text_step_pos)
        screen.blit(background, (0, 0))
    
        """rock's position text drawing"""
        text_distance = font.render(f"Rock's distance from Tree: {paradoxe_2.target_pos - paradoxe_2.object_pos} m", 1, (0, 255, 0))
        text_distance_pos = text_distance.get_rect()
        text_distance_pos.centerx = background.get_rect().centerx
        text_distance_pos.centery = background.get_rect().centery + 150
        background.blit(text_distance, text_distance_pos)
        screen.blit(background, (0, 0))
        background.fill((255, 255, 255))

        """Rock and Tree sprite drawing"""
        screen.blit(tree, (450, 10))
        screen.blit(rock, (paradoxe_2.object_pos , 140))
        pygame.display.update()

        """Rock's position movement"""
        paradoxe_2.object_pos += (paradoxe_2.target_pos - paradoxe_2.object_pos) / 2

        pygame.time.Clock().tick(1)

def display_flying_arrow():
    
    """arrow and target sprite loading"""
    arrow = pygame.image.load("sprites/arrow.png").convert_alpha()
    arrow = pygame.transform.scale(arrow, (50, 50))
    target = pygame.image.load("sprites/target.png").convert_alpha()
    target = pygame.transform.scale(target, (50, 50))

    time = 0
    while paradoxe_3.object_pos <= paradoxe_3.target_pos:
        time += 1
        background.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)

        """Time's text drawing"""
        text_time = font.render(f"Time: {time-1} s", 1, (10, 10, 10))
        text_time_pos = text_time.get_rect()
        text_time_pos.centerx = background.get_rect().centerx
        text_time_pos.centery = background.get_rect().centery - 50
        background.blit(text_time, text_time_pos)
        screen.blit(background, (0, 0))

        """Info's position text drawing"""
        text_info = font.render(f"Speed: {paradoxe_3.object_speed} m/s to Destination: {paradoxe_3.target_pos}", 1, (10, 10, 10))
        text_info_pos = text_info.get_rect()
        text_info_pos.centerx = background.get_rect().centerx
        text_info_pos.centery = background.get_rect().centery + 50
        background.blit(text_info, text_info_pos)
        screen.blit(background, (0, 0))

        """Arrow's position text drawing"""
        text_arrow = font.render(f"Arrow's position: {paradoxe_3.object_pos} m", 1, (10, 10, 10))
        text_arrow_pos = text_arrow.get_rect()
        text_arrow_pos.centerx = background.get_rect().centerx
        text_arrow_pos.centery = background.get_rect().centery + 100
        background.blit(text_arrow, text_arrow_pos)
        screen.blit(background, (0, 0))

        """Achille and Turtoise sprite drawing"""
        screen.blit(target, (paradoxe_3.target_pos + 25 , 50))
        screen.blit(arrow, (paradoxe_3.object_pos , 50))
        pygame.display.update()

        """Arrow's position movement"""
        paradoxe_3.object_pos = time * paradoxe_3.object_speed

        pygame.time.Clock().tick(1)

continuer = 1

start()

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = 0
                pygame.quit()
            elif event.key == pygame.K_SPACE:
                start()
            elif event.key == pygame.K_1:
                paradoxe_1 = Paradoxe(0, 10, 100, 2)
                # paradoxe_1.achille_vs_turtoise()
                display_achille_vs_tortue()
            elif event.key == pygame.K_2:
                paradoxe_2 = Paradoxe(0, 0, 100, 100)
                # paradoxe_2.dichotomie()
                display_dichotomie()
            elif event.key == pygame.K_3:
                paradoxe_3 = Paradoxe(0, 50, 500, 0)
                # paradoxe_3.flying_arrow()
                display_flying_arrow()
pygame.quit()
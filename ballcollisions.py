import pygame
import sys

def bouncing_on_corners(position, velocity):
    if position.x > 800 - radius:
        position.x = 800 - radius
        if velocity.x < 0:
            velocity.x = abs(velocity.x * 1)
        elif velocity.x > 0:
            velocity.x = -abs(velocity.x * 1)

    if position.x <= 0 + radius:
        position.x = 0 +radius
        if velocity.x < 0:
            velocity.x = abs(velocity.x * 1)
        elif velocity.x > 0:
            velocity.x = -abs(velocity.x * 1)

    if position.y >= 600 - radius:
        position.y = 600 - radius
        if velocity.y < 0:
            velocity.y = abs(velocity.y * 1)
        elif velocity.y > 0:
            velocity.y = -abs(velocity.y * 1) 
    
    if position.y <= 0 + radius:
        position.y = 0 + radius
        if velocity.y < 0:
            velocity.y = abs(velocity.y * 1)
        elif velocity.y > 0:
            velocity.y = -abs(velocity.y * 1) 

def position_update(position, velocity):
    position += velocity

def collision_detection():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
             position_1 = positions[i]
             position_2 = positions[j]
             velocity_1 = velocities[i]
             velocity_2 = velocities[j]
             mass_1 = masses[i]
             mass_2 = masses[j]
             dist = pygame.math.Vector2(position_1 - position_2)
             if dist.magnitude() < (radius + radius):
                m_sum = mass_1 + mass_2
                impact = position_2 - position_1
                v_diff = velocity_2 - velocity_1

                deltaV1 = (((2 * mass_2) * (v_diff.dot(impact))) / (m_sum * dist.magnitude() * dist.magnitude())) * (impact)
                deltaV2 = (((2 * mass_1) * (-1 * v_diff.dot(-1 * impact))) / (m_sum * dist.magnitude() * dist.magnitude())) * (-1 * impact)

                velocities[i] += (deltaV1 * 1)
                velocities[j] += (deltaV2 * 1)
                print("hgsdvh")

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (30, 30, 30)
radius = 50

positions = [pygame.math.Vector2(100, 100), pygame.math.Vector2(200, 200), pygame.math.Vector2(300, 200), pygame.math.Vector2(400, 200)]
velocities = [pygame.math.Vector2(2, 3),pygame.math.Vector2(2, -5) , pygame.math.Vector2(4, -5), pygame.math.Vector2(8, -7)]
masses = [2, 3, 4, 5]

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Collisions🌹")

circle_surf_1 = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
circle_1 = pygame.draw.circle(circle_surf_1, (255, 255, 255), (radius, radius), radius)
circle_rect_1 = circle_surf_1.get_rect(center = (100, 100))
circle_mask_1 = pygame.mask.from_surface(circle_surf_1)

circle_surf_2 = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
circle_2 = pygame.draw.circle(circle_surf_2, (255, 0, 0), (radius, radius), radius)
circle_rect_2 = circle_surf_2.get_rect(center = (100, 100))
circle_mask_2 = pygame.mask.from_surface(circle_surf_2)

circle_surf_3 = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
circle_3 = pygame.draw.circle(circle_surf_3, (0, 255, 0), (radius, radius), radius)
circle_rect_3 = circle_surf_3.get_rect(center = (100, 100))
circle_mask_3 = pygame.mask.from_surface(circle_surf_3)

circle_surf_4 = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
circle_4 = pygame.draw.circle(circle_surf_4, (0, 0, 255), (radius, radius), radius)
circle_rect_4 = circle_surf_4.get_rect(center = (100, 100))
circle_mask_4 = pygame.mask.from_surface(circle_surf_4)

clock = pygame.time.Clock()

# Main loop
running = True
while running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logic update
    for i in range(0, 4):
        position_update(positions[i], velocities[i])
        
    # (Add game logic here)
    for i in range(0, 4):
        bouncing_on_corners(positions[i], velocities[i])
    collision_detection()
    
    circle_rect_1.center = (positions[0].x, positions[0].y)
    circle_rect_2.center = (positions[1].x, positions[1].y)
    circle_rect_3.center = (positions[2].x, positions[2].y)
    circle_rect_4.center = (positions[3].x, positions[3].y)

    # Drawing
    screen.fill(BG_COLOR)
    screen.blit(circle_surf_1, circle_rect_1)
    screen.blit(circle_surf_2, circle_rect_2)
    screen.blit(circle_surf_3, circle_rect_3)
    screen.blit(circle_surf_4, circle_rect_4)

    # (Add drawing here)

    pygame.display.update()
    clock.tick(FPS)

# Cleanup
pygame.quit()
sys.exit()

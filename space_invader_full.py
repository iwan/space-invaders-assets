# Write your code here :-)
import random
import time

WIDTH = 1000
HEIGHT = 800

player = Actor("my_spaceship", midbottom = (WIDTH/2, HEIGHT-20))
# player.midbottom = (WIDTH/2, HEIGHT-20)


lasers = []
enemies = []
enemies2 = []
enemies3 = []
enemies4 = []
enemies_vx = 2
enemies_vy = 20
enemy_missiles = []

for n in range(0, 500, 70):
    enemies.append(Actor("alien1", (n+100, 100)))
for n in range(0, 500, 70):
    enemies2.append(Actor("alien2", (n+95, 170)))
for n in range(0, 500, 70):
    enemies3.append(Actor("alien8", (n+110, 240)))
for n in range(0, 500, 70):
    enemies4.append(Actor("alien9", (n+100, 310)))

def update():
    global enemies_vx, enemies_vy
    if keyboard.a or keyboard.left:
        player.x -= 10
    if keyboard.d or keyboard.right:
        player.x += 10
    if player.right >= WIDTH:
        player.right = WIDTH
    if player.left <= 0:
        player.left = 0

    for laser in lasers:
        laser.y -= 20

    for laser in lasers[:]:
        if laser.y < -100:
            lasers.remove(laser)


    # Collisione tra laser e nemici?
    for laser in lasers[:]:
        # rect = Rect((laser['x'], laser['y']),(4,20))
        for enemy in enemies[:]:
            if laser.colliderect(enemy):
                lasers.remove(laser)
                enemies.remove(enemy)
        for enemy in enemies2[:]:
            if laser.colliderect(enemy):
                lasers.remove(laser)
                enemies2.remove(enemy)
        for enemy in enemies3[:]:
            if laser.colliderect(enemy):
                lasers.remove(laser)
                enemies3.remove(enemy)
        for enemy in enemies4[:]:
            if laser.colliderect(enemy):
                lasers.remove(laser)
                enemies4.remove(enemy)


    for enemy in enemies:
        enemy.x += enemies_vx
    for enemy in enemies2:
        enemy.x += enemies_vx
    for enemy in enemies3:
        enemy.x += enemies_vx
    for enemy in enemies4:
        enemy.x += enemies_vx
    if len(enemies)>0 and (enemies[-1].right >= WIDTH or enemies[0].left <= 0):
        alieni_toccano_bordo()
    if len(enemies2)>0 and (enemies2[-1].right >= WIDTH or enemies2[0].left <= 0):
        alieni_toccano_bordo()
    if len(enemies3)>0 and (enemies3[-1].right >= WIDTH or enemies3[0].left <= 0):
        alieni_toccano_bordo()
    if len(enemies4)>0 and (enemies4[-1].right >= WIDTH or enemies4[0].left <= 0):
        alieni_toccano_bordo()

    for m in enemy_missiles:
        m.y += 20


def alieni_toccano_bordo():
    global enemies_vx
    enemies_vx *= -1 # invertono la direzione x
    # si abbassano:
    for enemy in enemies:
        enemy.y += enemies_vy
    for enemy in enemies2:
        enemy.y += enemies_vy
    for enemy in enemies3:
        enemy.y += enemies_vy
    for enemy in enemies4:
        enemy.y += enemies_vy


def draw():
    screen.clear()
    screen.fill("black")
    for laser in lasers:
        laser.draw()
        # screen.draw.filled_rect(Rect((laser['x'], laser['y']),(5,50)), "red")
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for enemy in enemies2:
        enemy.draw()
    for enemy in enemies3:
        enemy.draw()
    for enemy in enemies4:
        enemy.draw()
    for m in enemy_missiles:
        m.draw()


def on_key_down(key):
    if key == keys.SPACE:
        lasers.append(Actor("player_missile", player.midbottom))

def nemico_spara():
    if enemies:
        enemy = random.choice(enemies)
        enemy_missiles.append(Actor("enemy_missile", enemy.midbottom))

clock.schedule_interval(nemico_spara, 4.0)

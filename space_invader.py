import random

WIDTH = 1000
HEIGHT = 800

player = Actor("my_spaceship")
player.midbottom = (WIDTH/2, HEIGHT-20)

lasers = []
enemies = []
for n in range(0, 500, 70):
    enemies.append(Actor("alien1", (n+100, 100)))
enemies_vx = 4
enemies_vy = 8
bombs = []
bombs_vy = 10


def update():
    global enemies_vx
    if keyboard.a:
        player.x -= 10
    if keyboard.d:
        player.x += 10
    if player.right >= WIDTH:
        player.right = WIDTH
    if player.left <= 0:
        player.left = 0

    for laser in lasers:
        laser.y -= 20

    for laser in lasers:
        if laser.y < -100:
            lasers.remove(laser)

    print(len(lasers))

    for e in enemies:
        e.x += enemies_vx
    if enemies and (enemies[0].left <= 0 or enemies[-1].right >= WIDTH):
        enemies_vx *= -1  # inverte la direzione x
        for e in enemies:
            e.y += enemies_vy  # scendono tutti

    for laser in lasers:
        for enemy in enemies:
            if enemy.colliderect(laser):
                print("Colpito")
                lasers.remove(laser)
                enemies.remove(enemy)

    for b in bombs[:]:
        b.y += bombs_vy  # la bomba scende
        if b.y > HEIGHT+100:
            bombs.remove(b)
        else:
            if b.colliderect(player):  # la bomba ha colpito il player?
                bombs.remove(b)


def draw():
    screen.clear()
    screen.fill("black")
    for laser in lasers:
        laser.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for b in bombs:
        b.draw()


def on_key_down(key):
    if key == keys.SPACE:
        print("fire")
        lasers.append(Actor("player_missile", center=player.midtop))

def nemico_spara():
    if enemies:
        enemy = random.choice(enemies)
        bombs.append(Actor("enemy_missile", center=enemy.center))
        print("bomba")


clock.schedule_interval(nemico_spara, 2.0)

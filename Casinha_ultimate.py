from pygame import *
import sys

def abrir_casinha():

    init()
    mixer.init()

    window = display.set_mode((1280, 720))

    borboleta = image.load("borboletinha.png").convert_alpha()
    borboleta = transform.scale(borboleta, (300, 300))

    fonte = font.Font("LobsterTwo.ttf", 40)
    texto = fonte.render("Uma borboleta!", True, (0, 0, 0))

    mixer.music.load("som_manha.mp3")
    mixer.music.play(-1)

    fase_do_dia = ""

    running = True
    clock = time.Clock()

    nuvem_x = 800
    nuvem_y = 150
    velocidade_nuvem = 2

    sol_x = 150
    sol_y = 150

    while running:

        clock.tick(60)

        for ev in event.get():
            if ev.type == QUIT:
                running = False

        dt = clock.get_time() / 1000
        keys = key.get_pressed()

        mouse_x, mouse_y = mouse.get_rel()
        sol_x += mouse_x
        sol_y += mouse_y
        mouse.set_pos((sol_x, sol_y))

        if keys[K_a]:
            sol_x -= 100 * dt
        if keys[K_d]:
            sol_x += 100 * dt
        if keys[K_w]:
            sol_y -= 100 * dt
        if keys[K_s]:
            sol_y += 100 * dt

        
        if sol_x < 1:
            sol_x = 1
        if sol_y < 1:
            sol_y = 1
        if sol_x > 1280:
            sol_x = 1280
        if sol_y > 710:
            sol_y = 710

       
        if 426 < sol_x < 852:
            proporcao = (sol_x - 426) / (852 - 426)

            r = 237 + (23 - 237) * proporcao
            g = 135 + (14 - 135) * proporcao
            b = 71 + (110 - 71) * proporcao

            if fase_do_dia != "tarde":
                mixer.music.load("som_tarde.mp3")
                mixer.music.play(-1)
                fase_do_dia = "tarde"

        elif sol_x > 852:
            r, g, b = 23, 14, 110

            if fase_do_dia != "noite":
                mixer.music.load("som_noite.mp3")
                mixer.music.play(-1)
                fase_do_dia = "noite"

        else:
            proporcao = sol_x / 426

            r = 135 + (237 - 135) * proporcao
            g = 237 + (135 - 237) * proporcao
            b = 237 + (71 - 237) * proporcao

            if fase_do_dia != "manha":
                mixer.music.load("som_manha.mp3")
                mixer.music.play(-1)
                fase_do_dia = "manha"

        
        r = max(0, min(255, int(r)))
        g = max(0, min(255, int(g)))
        b = max(0, min(255, int(b)))

        fill_color = (r, g, b)

        window.fill(fill_color)

        # Chão
        draw.rect(window, (28, 133, 33), (0, 550, 1280, 170))

        # Sol
        draw.circle(window, (255, 255, 0), (int(sol_x), int(sol_y)), 50)

        # Raios
        draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x, sol_y - 100), 8)
        draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x, sol_y + 100), 8)
        draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x - 100, sol_y), 8)
        draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x + 100, sol_y), 8)
        draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x - 70, sol_y - 70), 8)
        draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x + 70, sol_y - 70), 8)
        draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x - 70, sol_y + 70), 8)
        draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x + 70, sol_y + 70), 8)

        # Casa
        draw.rect(window, (252, 3, 198), (330, 350, 200, 200))

        # Telhado
        draw.polygon(window, (71, 13, 61), [(330, 350), (530, 350), (430, 180)])

        # Porta
        draw.rect(window, (158, 90, 147), (370, 430, 60, 120))
        draw.circle(window, (0, 0, 0), (420, 490), 5)

        # Janela
        draw.rect(window, (0, 0, 139), (450, 440, 50, 70))

        # Árvore
        draw.rect(window, (130, 67, 20), (750, 400, 40, 150))
        draw.circle(window, (28, 133, 33), (770, 350), 80)

        # Nuvem
        draw.circle(window, (255, 255, 255), (nuvem_x, nuvem_y), 50)
        draw.circle(window, (255, 255, 255), (nuvem_x + 60, nuvem_y), 50)
        draw.circle(window, (255, 255, 255), (nuvem_x + 100, nuvem_y), 50)
        draw.circle(window, (255, 255, 255), (nuvem_x + 160, nuvem_y), 50)

        # Borboleta
        window.blit(borboleta, (900, 300))

        # Texto
        window.blit(texto, (900, 270))

        # Movimento da nuvem
        nuvem_x += velocidade_nuvem

        if nuvem_x > 1120:
            velocidade_nuvem = -2
        elif nuvem_x < 1:
            velocidade_nuvem = 2

        display.update()
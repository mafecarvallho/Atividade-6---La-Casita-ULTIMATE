# FUNÇÕES

import Casinha_ultimate

def valida_email(email):
    return email[-8:] == '@puc.com'

def possuiMaiscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z':
            return True
    return False

def possuiMinuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z':
            return True
    return False

def possuiNumero(palavra):
    for caractere in palavra:
        if '0' <= caractere <= '9':
            return True
    return False

def valida_senha(senha):
    check_tamanho = len(senha) >= 8
    check_maisucula = possuiMaiscula(senha)
    check_minuscula = possuiMinuscula(senha)
    check_numero = possuiNumero(senha)

    return check_maisucula and check_minuscula and check_numero and check_tamanho


# Para conseguir criptografar, é necessário:
# 1 - Pegar a letra, e converter para descimal (ASCII)
# 2- Subtrair o valor decimal de 65 ("Z" -> 90 - 65 = 25)
# 3 - Somar 3 ao resultado de 2 ( 25 + 3 = 28)
# 4 - Obter o resto da divisão do resultado de 3 por 26 ( 28 % 26 = 2)
# 5 - Somar o resto a 65 e converter ovalor de volta p/ lista ( 2 + 65 = 67 -> letra C)


def criptografia_senha(senha):
    senha_cripto = ''
    # Verificando se é numero, letra maisucula , minusculo ou especial
    for char in senha:
        if char.isdigit():
            ref = ord('0') 
            ascci_char = ord(char) # Etapa 1 
            posicao_alpha = ascci_char - ref # Etapa 2
            posicao_cesar = posicao_alpha + 3 # Etapa 3 
            posicao_cesar =  posicao_cesar % 10 # Etapa 4
            letra_cesar = chr(ref + posicao_cesar) # Etapa 5 
            senha_cripto += letra_cesar

        elif 'A' <= char <= 'Z':
            ref = ord('A') # 65
            ascci_char = ord(char) # Etapa 1 
            posicao_alpha = ascci_char - ref # Etapa 2
            posicao_cesar = posicao_alpha + 3 # Etapa 3 
            posicao_cesar =  posicao_cesar % 26 # Etapa 4
            letra_cesar = chr(ref + posicao_cesar) # Etapa 5 
            senha_cripto += letra_cesar
        
        elif 'a' <= char <= 'z':
            ref = ord('a') 
            ascci_char = ord(char) # Etapa 1 
            posicao_alpha = ascci_char - ref # Etapa 2
            posicao_cesar = posicao_alpha + 3 # Etapa 3 
            posicao_cesar =  posicao_cesar % 26 # Etapa 4
            letra_cesar = chr(ref + posicao_cesar) # Etapa 5 
            senha_cripto += letra_cesar

        else: 
            senha_cripto += char
    return senha_cripto


# PYGAME

from pygame import *

init()

window = display.set_mode((900, 900))
fonte = font.Font(None, 40)
clock = time.Clock()

running = True

input_user_email = ""
input_user_senha = ""

etapa = "email"
mensagem = ""

while running:

    for ev in event.get():

        if ev.type == QUIT:
            running = False

        if ev.type == KEYDOWN:

            if ev.key == K_BACKSPACE:
                if etapa == "email":
                    input_user_email = input_user_email[:-1]
                elif etapa == "senha":
                    input_user_senha = input_user_senha[:-1]

            elif ev.key == K_RETURN:
                if etapa == "email":
                    if valida_email(input_user_email):
                        etapa = "senha"
                        mensagem = ""
                    else:
                        mensagem = "Email inválido"
                        input_user_email = ""

                elif etapa == "senha":
                    if valida_senha(input_user_senha):
                        senha_criptografada = criptografia_senha(input_user_senha)
                        print("Senha criptografada:", senha_criptografada)

                        mensagem = "Senha criptografada: " + senha_criptografada
                        etapa = "criptografia"

                    else:
                        mensagem = "Senha inválida"
                        input_user_senha = ""

            else:
                if etapa == "email":
                    input_user_email += ev.unicode
                elif etapa == "senha":
                    input_user_senha += ev.unicode


    window.fill((255, 255, 255))

    if etapa == "email":
        desenho_login = fonte.render("LOGIN:", True, (252, 58, 210))
        window.blit(desenho_login, (150, 200))

        desenho_email = fonte.render(input_user_email, True, (0, 0, 0))
        window.blit(desenho_email, (300, 200))

        instrucao = fonte.render("Digite o e-mail e aperte ENTER", True, (173, 35, 67))
        window.blit(instrucao, (150, 300))

        desenho_mensagem = fonte.render(mensagem, True, (173, 35, 67))
        window.blit(desenho_mensagem, (150, 400))

    elif etapa == "senha":
        desenho_senha = fonte.render("SENHA:", True, (252, 58, 210))
        window.blit(desenho_senha, (150, 200))

        desenho_input_senha = fonte.render(input_user_senha, True, (0, 0, 0))
        window.blit(desenho_input_senha, (300, 200))

        instrucao = fonte.render("Digite a senha e aperte ENTER", True, (173, 35, 67))
        window.blit(instrucao, (150, 300))

        desenho_mensagem = fonte.render(mensagem, True, (173, 35, 67))
        window.blit(desenho_mensagem, (150, 400))

    elif etapa == "criptografia":
        desenho_mensagem = fonte.render(mensagem, True, (173, 35, 67))
        window.blit(desenho_mensagem, (150, 300))

        display.update()
        time.delay(2000)

        running = False
        Casinha_ultimate.abrir_casinha()

    display.update()
    clock.tick(60)


quit()
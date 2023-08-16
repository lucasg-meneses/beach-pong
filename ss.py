import pygame

# Definir resolução da janela
largura_janela = 320
altura_janela = 180

# Inicializar Pygame
pygame.init()

# Criar janela
janela = pygame.display.set_mode((largura_janela, altura_janela), (pygame.SCALED | pygame.RESIZABLE| pygame.FULLSCREEN))

# Carregar sprite
sprite = pygame.image.load('asset/sprites/pad/pd.png')

# Definir posição inicial do sprite
pos_x = 0
pos_y = 0

# Definir velocidade de movimento
velocidade = 2

# Criar um objeto Clock para controlar a taxa de atualização
clock = pygame.time.Clock()

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Capturar teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Atualizar posição do sprite de acordo com as teclas pressionadas
    if teclas[pygame.K_LEFT]:
        pos_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        pos_x += velocidade
    if teclas[pygame.K_UP]:
        pos_y -= velocidade
    if teclas[pygame.K_DOWN]:
        pos_y += velocidade

    # Preencher a janela com uma cor de fundo (opcional)
    janela.fill((255, 0, 0))

    # Desenhar sprite na janela
    janela.blit(sprite, (pos_x, pos_y))

    pygame.display.flip()

    # Limitar a taxa de atualização do jogo para 60 FPS
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()

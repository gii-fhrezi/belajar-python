import pygame

# __init__
pygame.init()
# variable running game
isrun = True

window = pygame.display.set_mode((500,500)) # untuk membuat tmpilan wwindow

""" objectgame """
# letak object
x = 250
y = 250

# lebar object
lebar = 20
panjang = 20

#kecepatan
kecepatan = 1
# membuat agar tampilan window bisa tampil secara terus menerus
while isrun:
# user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrun = False
    # ambil semua key pressed keyboard
    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT] and x > 0:
        x -= kecepatan
    if keys [pygame.K_RIGHT] and x < 500 - lebar:
        x += kecepatan
    if keys [pygame.K_DOWN] and y < 500 - panjang:
        y += kecepatan
    if keys [pygame.K_UP] and y > 0:
        y -= kecepatan 
# update asset
    window.fill((255,255,255)) # membuat warna window menjadi putih
    pygame.draw.rect(window,(255,0,0),(x,y,lebar,panjang))
# render ke display
    pygame.display.update()
pygame.quit()
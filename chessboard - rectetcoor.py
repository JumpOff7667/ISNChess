import sys, pygame
pygame.init()

#Parametrages
size = width, height = 512, 512
sizepion = width, height = 64, 64
sizecarre = width, height = 64, 64
lignes, colonnes = 8, 8

#Variables
case = [[0] * colonnes for _ in range(lignes)]
tours = []
selection = 0

#Definir la taille de l'ecran
screen = pygame.display.set_mode(size)

#Charger l'image du damier et son rectangle
damier = pygame.image.load("Damier.gif")
damierect = damier.get_rect()

#Charger tour et son rectangle (avec redimension)
tourn = pygame.image.load("rook.png")
tourn = pygame.transform.scale(tourn, (sizepion))
tourN = tour_n.get_rect()
tours.append(tourN)

#Carres du damier
for i in range (0,8):
    for j in range (0, 8):
        case[i][j] = pygame.Rect(i*64, j*64, 64, 64)
        

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            r1, r2 = int(x/64), int(y/64)
            if case[r1][r2].colliderect(tourN):
                selection = tourN
                print("ok for selection")
            if selection in tours:
                r3, r4 = int(x/64), int(y/64)
                if not case[r3][r4].colliderect(selection):  
                    selection.clamp_ip(case[r3][r4])
                    selection = 0
                    print("ok for clamp")
                        
                        
                    
                
    screen.blit(damier, damierect)
    screen.blit(tourn, tourN)
    pygame.display.flip()

        

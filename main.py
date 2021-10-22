import pygame

from globalVar import WIDTH, FPS, clock

def draw_window():
    #player.currentScreen.screenUpdate()
    pygame.display.update()

def main():
    run = True
    
    while run:

        clock.tick(FPS)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
        
        #player.basicFunctions(WIDTH)

        draw_window()
        
    pygame.quit()

if __name__ == "__main__":
    main()
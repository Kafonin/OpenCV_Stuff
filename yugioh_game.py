
from PIL import Image
import cv2
import pytesseract
import pygame
import send2trash

#####################################################################################################
#####################################################################################################



def main():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Test_Window")
    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("Test_Window", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "sample{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()
    #im = Image.open("sample0.png")
    #text = pytesseract.image_to_string(im, lang = 'eng')

    #if "BLUE EYES WHITE DRAGON" or "Blue Eyes White Dragon"  in text:
    #    print("Place holder text -- read success.")
    #    send2trash.send2trash("sample0.png")
    #    return 1

    #if "DARK MAGICIAN" or "Dark Magician"  in text:
    #    print("Place holder text -- read success.")
    #    send2trash.send2trash("sample0.png")

#####################################################################################################
#####################################################################################################

def game():
     
    # initialize the pygame module
    pygame.init()
    
    window_width=1280
    window_height=745

    animation_increment=10
    clock_tick_rate=20

    # open a window
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size) # screen size here

    # Set title to the window
    pygame.display.set_caption("It's time to duel!")

    dead=False

    clock = pygame.time.Clock()
    background_image = pygame.image.load("bg.jpg").convert()
    background_image = pygame.transform.scale(background_image, (1280, 745))
    duelMonsterOne = pygame.image.load("be.jpg")
    duelMonsterTwo = pygame.image.load("dm.jpg")

    while(dead==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

        pygame.display.flip()
        clock.tick(clock_tick_rate)
        main()
        im = Image.open("sample0.png")
        text = pytesseract.image_to_string(im, lang = 'eng')
        screen.blit(background_image, [0, 0])

        if "BLUE EYES WHITE DRAGON" or "Blue Eyes White Dragon"  in text:
            #print("Place holder text -- read success.")
            send2trash.send2trash("sample0.png")
            screen.blit(duelMonsterOne, (500, 100))
            pygame.display.update()
            clock.tick(clock_tick_rate)

        if "DARK MAGICIAN" or "Dark Magician"  in text:
            #print("Place holder text -- read success.")
            send2trash.send2trash("sample0.png")
            screen.blit(duelMonsterTwo, (500, 500))
            pygame.display.update()
            clock.tick(clock_tick_rate)

#####################################################################################################
#####################################################################################################

if __name__=="__main__":
    # call the main function
    theGame = game()

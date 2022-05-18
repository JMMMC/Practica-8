import cv2
import numpy as np

# Laplaciano, Sobelx, Sobely, Canny.

def Impresion(namme,imagen,x,y):
    cv2.namedWindow(namme)
    cv2.moveWindow(namme, x,y)
    cv2.imshow(namme, imagen)
    
cap = cv2.VideoCapture('RAfrodita.mp4')

while(1):

    _, frame = cap.read()

    laplaciano = cv2.Laplacian(frame, cv2.CV_64F)
    laplaciano = np.uint8(np.absolute(laplaciano))
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobelx = np.uint8(np.absolute(sobelx))
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    sobely = np.uint8(np.absolute(sobely))
    border = cv2.Canny(frame, 200, 150)

    Impresion('frame',frame,50,10)
    Impresion('laplaciano',laplaciano,550,10)
    Impresion('sobel x', sobelx,1050,10)
    Impresion('sobel y', sobely,550,270)
    Impresion('canny', border,1050,270)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

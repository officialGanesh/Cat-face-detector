
# import required modules
import cv2 as cv
from random import randrange


def Detect_face():
    """This function is used to detect faces of cat from an image and convert into grayscale"""

    img = cv.imread('cat-face.jpg')
    cv.imshow("Cat",img)

    gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    cv.imshow('Gray-cat',gray)

    


if __name__ == "__main__":

    Detect_face()

    cv.waitKey(0)
    cv.destroyAllWindows()
    print("Code Completed 🔥")

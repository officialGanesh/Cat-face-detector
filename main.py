
# import required modules
import cv2 as cv
from random import randrange

cat_face_data_set = cv.CascadeClassifier('Cat_dataSet.xml')

def Detect_face():
    """This function is used to detect faces of cat from an image and convert into grayscale"""

    img = cv.imread('cat-face.jpg')
    cv.imshow("Cat",img)

    gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    cv.imshow('Gray-cat',gray)

    def rect_face():
        '''This function will draw rectangles across face coordinates'''

        cat_face_coordinates  = cat_face_data_set.detectMultiScale(gray)
        for (a,b,c,d) in cat_face_coordinates:
            rect_cat = cv.rectangle(img,(a,b),(a+c,b+d),(randrange(256),randrange(256),randrange(256)))
        cv.imshow("Cat-face-detected",rect_cat)
    rect_face()


if __name__ == "__main__":

    Detect_face()

    cv.waitKey(0)
    cv.destroyAllWindows()
    print("Code Completed 🔥")

import cv2
import glob


cascade = cv2.CascadeClassifier("haarcascade.xml")

image = cv2.imread('a4.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rects = cascade.detectMultiScale(
gray,
scaleFactor=1.1,
minNeighbors=5,
minSize=(30, 30),
flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)


if len(rects) > 0:
        for (x, y, w, h) in rects:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print "Image scan result: Alert, Nudity Content Found"
            cv2.imshow("Rects found", image)
else:
                print "Image scan result: No Nudity Content Found"
                cv2.imshow("Rects found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2 as cv
capture = cv.VideoCapture(r'C:\Users\Aditya\OneDrive\Desktop\Practice\OpenCV\Videos\Video1.mov')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(10) & 0xFF == 'd':
        break
capture.release()
cv.destroyAllWindows()

import cv2
video_capture = cv2.VideoCapture('Sample.mp4')

cv2.namedWindow("Window")

while True:
    ret, frame = video_capture.read()
    cv2.imshow("Window", frame)

video_capture.release()
cv2.destroyAllWindows()

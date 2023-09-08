import cv2
import os

print(os.getcwd())
os.chdir(os.path.dirname(__file__))

video_path = "bunny.mp4"

capture = cv2.VideoCapture(video_path)

while cv2.waitKey(33) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES,0)

    ret, frame = capture.read()
    cv2.imshow("VideoFrame",frame)

capture.release()
cv2.destroyAllWindows()
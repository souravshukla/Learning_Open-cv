import cv2 as cv

def rescaledFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)


capture = cv.VideoCapture("Video/dog.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaledFrame(frame)

    cv.imshow("Video_resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
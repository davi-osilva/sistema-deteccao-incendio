import cv2

camera = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(
     cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

while True:
    sucesso, frame = camera.read()
    if not sucesso:
        break

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Frame: ", frame)

    if cv2.waitKey(1) == 27:
        break
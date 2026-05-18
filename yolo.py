from ultralytics import YOLO
import cv2

camera = cv2.VideoCapture(0)
modelo = YOLO("yolov8n.pt")

while True:
    sucesso, frame = camera.read()

    if not sucesso:
        print("Erro ao usar a câmera")
        break

    inferencia = modelo(frame, conf=0.6)
    resultado = inferencia[0]
    nomes = resultado.names

    box_do_frame = resultado.plot()

    cv2.imshow("YOLO", box_do_frame)

    for box in resultado.boxes:
        id_cls = int(box.cls[0])
        conf = float(box.conf[0]) * 100

        print(f"{nomes[id_cls]} - {conf:.2f}%")

    if cv2.waitKey(1) == 27:
        break

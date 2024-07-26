from ultralytics import YOLO

model = YOLO("yolov10n.yaml")

model.train(data="PATH TO data.yaml\data.yaml", epochs=100, imgsz=640)

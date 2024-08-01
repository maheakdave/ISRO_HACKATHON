from ultralytics import YOLO

model = YOLO("yolov10n.yaml")

model.train(data="Crater and boulder detection.v2i.yolov9/data.yaml", epochs=100, imgsz=640, workers=0)
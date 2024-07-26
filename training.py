from ultralytics import YOLO

model = YOLO("yolov10n.yaml")

model.train(data="dataset\CreaterBoulder-4\data.yaml", epochs=100, imgsz=640)

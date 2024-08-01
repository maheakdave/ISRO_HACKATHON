import cv2
import streamlit as st
import numpy as np
from ultralytics import YOLOv10 as YOLO
import matplotlib.pyplot as plt
from glob import glob
import matplotlib.pyplot as plt



model = YOLO('yolov10l.yaml')
model = YOLO("runs\\detect\\train21\weights\\best.pt")



def predict(chosen_model, img): 
    __ = chosen_model.predict(img, save=True, imgsz=640, conf=0.001, iou = 0.5, save_txt=True, save_conf=True,save_dir='D:\isro_hack\predictions')


st.title("Upload the Image for Detections!!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    
    image_bytes = uploaded_file.getvalue()
    orig_image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    predict(model, orig_image)
    img_file = glob('runs\\detect\\predict*\\*.jpg')[-1]
    result_img = plt.imread(img_file)
    st.subheader("Original Image")
    st.image(orig_image, caption='Original Image', use_column_width=True)

    st.subheader("Detected Objects")
    st.image(result_img, caption='Detected Objects', use_column_width=True)
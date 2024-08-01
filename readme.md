# **nyxNOVA: Lunar Navigation and Visualization**
This project is part of the ISRO Hackathon, focusing on developing a safe navigation route and implementing a 3D model for lunar visualization. The application utilizes YOLOv10 for object detection and Streamlit for the user interface.
## **Features**
Our application aims to provide the following capabilities in three stages:
### **Visual Imagery & 3D Models**

Accurate displays and geometric figures of lunar imagery, terrain, and place names of known locations
Ability to accurately measure and profile terrain elevation
Georeferenced imagery

### **Navigation and Analysis**

Calculate and display lunar terrain intersections from a central viewpoint
Run sophisticated viewshed analysis showing line of sight obstructions due to terrain
Viewshed analysis for optimal route planning

### **Data Handling**

Import/Export functionality for KML, CSV, ESRI shape, and GeoTIFF files

## **Getting Started**
### **Prerequisites**

Python 3.x
pip (Python package manager)

### **Installation**

Clone the repository:
``git clone https://github.com/maheakdave/ISRO_HACKATHON-.git``
```cd ISRO_HACKATHON-```

Install the required Python packages:
```pip install -r requirements.txt```


## **Usage**
### **Training the Model**
To start training the YOLOv10 model, run:
```python3 training.py```
You can view the model's evaluations in the runs folder, which will appear in the working directory during training.
### **Running the Application**
To launch the Streamlit app, execute:
```streamlit run app.py```

## **In Brief**
- Get started by installing all the python packages by running ```pip install -r requirements.txt``` in your terminal.
- To start training the YOLOv10 model run ```python3 training.py``` command  in the terminal.
- View the model's evaluations in the runs folder which pops up while training the model in the working directory.
- To run streamlit app simply type ```streamlit run app.py``` in your terminal.

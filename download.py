from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY_HERE")
project = rf.workspace("craters-qfjw2").project("createrboulder")
version = project.version(4)
dataset = version.download("yolov8")

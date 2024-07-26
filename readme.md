Welcome!

- To download dataset paste your API key in the ```rf = Roboflow(api_key="YOUR_API_KEY_HERE")``` in the download.py and  run  `python3 download.py` in the CLI.
- To start training the YOLOv10 model use the data.yaml file's directory in your own computer in the training.py file by replacing the path in the line ```model.train(data="PATH TO data.yaml\data.yaml", epochs=100, imgsz=640)```
  and run ```python3 training.py``` in the CLI.
-  View the model's evaluations in the runs folder which pops up while training the model in the working directory.

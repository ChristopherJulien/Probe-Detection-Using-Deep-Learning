# Probe Detection Models

This repository provides the implementation of various deep learning models for probe detection, including YOLOv8, YOLO-NAS, and RT-DETR. It includes preprocessed datasets, Jupyter notebooks for each model, and a script to convert data into the YOLO format. Follow the instructions below to set up and run the project.

## Repository Structure
.
├── notebook
│   ├── data
│   │   ├── coco-yolo.py
│   │   ├── labels_yolo_Probe
│   │   ├── probe_dataset.zip
│   │   ├── probe_labels.json
│   │   ├── probe_preprocessed_RT-DETR.zip
│   │   ├── probe_preprocessed_YOLO-NAS.zip
│   │   └── probe_preprocessed_YOLOv8.zip
│   ├── RT-DETR.ipynb
│   ├── YOLO-NAS.ipynb
│   └── YOLOv8.ipynb
├── README.md
└── requirements.txt

## Setup Instructions

1. **Clone the Repository**
   Use `git` to clone this repository:
   ```bash
   git clone https://github.com/ChristopherJulien/Probe-Detection-Using-Deep-Learning.git
   cd ~/Probe-Detection-Using-Deep-Learning/data

2. **Install Requirements**
 Ensure you have the necessary classes:
 ```bash
 pip install -r requirements.txt

```

 3. **Unzip preprocessed data**
  ```bash
  cd notebook/data
unzip probe_preprocessed_RT-DETR.zip
unzip probe_preprocessed_YOLO-NAS.zip
unzip probe_preprocessed_YOLOv8.zip
```
 
 4. **Run Jupyter Notebooks** To explore and run the models, start a Jupyter Notebook server:
   ```bash
   jupyter notebook


```
Open the desired notebook (RT-DETR.ipynb, YOLO-NAS.ipynb, or YOLOv8.ipynb) in your browser and execute the cells.
# Probe Detection Models

This repository provides the implementation of various deep learning models for probe detection, including YOLOv8, YOLO-NAS, and RT-DETR. It includes preprocessed datasets, Jupyter notebooks for each model, and a script to convert data into the YOLO format. Follow the instructions below to set up and run the project.

## Repository Structure

. ├── notebook │ ├── data │ │ ├── coco-yolo.py # Script for converting data to YOLO format │ │ ├── labels_yolo_Probe # Directory containing YOLO-formatted labels │ │ ├── probe_dataset.zip # Raw dataset │ │ ├── probe_labels.json # JSON file with probe annotations │ │ ├── probe_preprocessed_RT-DETR.zip # Preprocessed data for RT-DETR │ │ ├── probe_preprocessed_YOLO-NAS.zip # Preprocessed data for YOLO-NAS │ │ ├── probe_preprocessed_YOLOv8.zip # Preprocessed data for YOLOv8 │ ├── RT-DETR.ipynb # Jupyter notebook for RT-DETR implementation │ ├── YOLO-NAS.ipynb # Jupyter notebook for YOLO-NAS implementation │ └── YOLOv8.ipynb # Jupyter notebook for YOLOv8 implementation ├── README.md # Documentation ├── requirements.txt # List of dependencies


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
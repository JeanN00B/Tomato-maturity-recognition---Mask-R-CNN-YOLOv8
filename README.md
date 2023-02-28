# Mask-R-CNN and YOLOv8 comparison to perform maturity recognition task

See the related paper to this code [here](https://www.overleaf.com/read/qkczrvzzkwnt)

Original YOLOv8 repo from ultralytics [here](https://github.com/ultralytics/ultralytics)

Original Mask R-CNN repo from MMdetection [here](https://github.com/open-mmlab/mmdetection)

Original tomato dataset repo [here](https://github.com/laboroai/LaboroTomato)


Tomato detection and classification is an important task that big farms might have, where manual harvest is not scalable, 
and automatic machine harvesting may not be accurate. Some works in the precision agriculture field propose a color-based 
maturity detection technique or machine learning techniques; however, these methodologies have low accuracy. Even the use of some 
image classifier architecture has become popular. However, these models need large datasets and training times, and the accuracy may remain low. 
Also, one of the main challenges to achieving this task is to get a suitable dataset containing high-quality images and annotations and adequate for 
the correct architecture.
This work explores the segmentation and detection of tomatoes in different maturity states for harvesting prediction 
by using the laboro tomato dataset to train a mask R-CNN and a YOLOv8 architecture. 


## Repo description

The repository is divided into:
  - [Google colab notebooks with the YOLOv8 implementation.](https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/YOLOv8%20-%20custom.ipynb)
  - [Google colab notebooks with the Mask R-CNN implementation.](https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/MMdetection%20-%20mask-RCNN.ipynb)
  - [Folder containig the tomato dataset in the COCO format](https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/tree/main/Tomato-Dataset/Big_tomatoes-dataset-2)
  - [Folder with the YOLOv8 code](https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/tree/main/Tomato-Dataset/YOLOv8)
  - [Folder with the Mask R-CNN code](https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/tree/main/Tomato-Dataset/mmdetection)
  - [Folder with the color analysis python scripts](https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/tree/main/Color%20analysis)
 
 It is highly recommendabe to access the original repos to read the whole documentation and modify the colab notebooks.
 
 To work with this repo, it recommendable to do this in google colab. Download the Tomato-Dataset folder and upload to your own drive 
 directory, or only by cloning the repo.
 
```
#clone on google colab
!git clone https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8.git

#normal clone on your pc
git clone https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8.git
```

## Results

<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/YOLO-green.jpg" width="30%"></img>
<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/YOLO-half-ripened.jpg" width="30%"></img>
<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/YOLO-fully-ripened.jpg" width="30%"></img>

<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/MRCNN-green.jpg" width="30%"></img>
<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/MRCNN-half-ripened.jpg" width="30%"></img>
<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/MRCNN-fully-ripened.jpg" width="30%"></img>

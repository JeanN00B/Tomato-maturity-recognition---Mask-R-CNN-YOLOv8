# Mask-R-CNN and YOLOv8 comparison to perform maturity recognition task

See the related paper to this code [here](http://dx.doi.org/10.1007/978-3-031-45438-7_26)

Original YOLOv8 repo from ultralytics [here](https://github.com/ultralytics/ultralytics)

Original Mask R-CNN repo from MMdetection [here](https://github.com/open-mmlab/mmdetection)

Original tomato dataset repo [here](https://github.com/laboroai/LaboroTomato)


This work explores the segmentation and detection of tomatoes in different maturity states for harvesting prediction by using the laboro tomato dataset to train a mask R-CNN and a YOLOv8 architecture. The laboro tomato dataset contains two tomato classes, normal and cherry, and it detects three ripeness states, ripe, half-ripe, and green, but only the normal class will be used. This work aims to test a state-of-the-art model to compare the results against the mask R-CNN architecture proposed on the benchmark paper [[1]](https://doi.org/10.1145/3508259.3508262). The evaluation metric intersection over union (IoU) 0.5 showed an average precision of 67.2\% with a recall of 78.9\% over the laboro tomato dataset and an IoU average precision of 92.1\% with a recall of 91.4\% over the same dataset once data augmentation was performed and generated synthetic images with a proposed algorithm. Nevertheless, this work will focus on improving the detection over the original dataset, where the benchmark paper author's do this in a separate process by color analysis algorithms, and uses $R^{2}$ for how accurately the tomato was set into the three maturity classes.

The results are that the state-of-the-art YOLOv8, having a $R^2$ of 0.809, 0.897, and 0.968 in the ripe, half-ripe and green categories respectively. However the Mask R-CNN results are acceptable, with a 0.819, 0.809, and 0.893 in the ripe, half-ripe and green categories respectively. YOLOv8 model performed better than the one used in the benchmark paper by detecting and segmenting the tomatoes, as well as classifying them. And the color-analysis technique used in the benchmark paper is considered inefficient, because the classification results showed that there is not even a linear relation between the predictions and the real values.


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

**Important:** While executing the colab notebooks an the python scripts as well, it is mandatory to change the directions from the directories to match to the location of the respective required files. The notebooks contains more information about how to use them, but basically it is needed to execute all the cells and get the results.
 
```
#clone on google colab
!git clone https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8.git

#normal clone on your pc
git clone https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8.git
```

## Results

Images from the original dataset, the predicted with YOLOv8, and Mask R-CNN from left to right respectively.

<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/YOLO-green.jpg" width="30%"></img>
<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/YOLO-half-ripened.jpg" width="30%"></img>
<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/YOLO-fully-ripened.jpg" width="30%"></img>

<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/MRCNN-green.jpg" width="30%"></img>
<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/MRCNN-half-ripened.jpg" width="30%"></img>
<img src="https://github.com/JeanN00B/Tomato-maturity-recognition---Mask-R-CNN-YOLOv8/blob/main/Color%20analysis/Results/MRCNN-fully-ripened.jpg" width="30%"></img>

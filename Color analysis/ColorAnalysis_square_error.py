import numpy as np
from PIL import Image, ImageDraw
import os
import json
import ast

directory = os.path.abspath("/home/jean/MEGA/YACHAY/9no SEMESTRE/TESIS/Database & Code/Authors methodology/")

# Mask R-CNN
mrcnn_dir_json = os.path.join(directory, 'MASK predict/mask-RCNN.json')
mrcnn_dir_img = os.path.join(directory, 'MASK predict/images/')
# YOLO
yolo_dir_json = os.path.join(directory, 'YOLO predict/YOLOv8.json')
yolo_dir_masks = os.path.join(directory, 'YOLO predict/masks/')
yolo_dir_img = os.path.join(directory, 'YOLO predict/images/')
# Original
original_dir_json = os.path.join(directory, 'tomatoes-dataset/annotations/test.json')
original_dir_img = os.path.join(directory, 'tomatoes-dataset/test/')

categories = {
    0 : 'b_fully_ripened',
    1 : 'b_green',
    2 : 'b_half_ripened'}

# Read the .json files
with open(mrcnn_dir_json, 'r') as read_mrcnn:
    data_mrcnn = json.load(read_mrcnn)
with open(original_dir_json, 'r') as read_original:
    data_original = json.load(read_original)
with open(yolo_dir_json, 'r') as read_yolo:
    data_yolo = json.load(read_yolo)

color_pred = []
with open('YOLO predict/tmp.txt', 'r', ) as file:
    for lines in file:
        tmp = lines.split(":")
        list_values = ast.literal_eval((tmp[1].replace("], \n","]")).replace(' [', '['))
        color_pred.append([tmp[0].replace("'", ""), list_values])

# Store in dictionary img_ids and img_names
images_ids = {}
for image in data_original['images']:
    images_ids[image['id']] = image['file_name'].replace('.jpg', '')
    final_names = image['file_name'].replace('.jpg', '')

#replace ids = ints into ids = name.
for image in data_mrcnn:
    image['image_id'] = images_ids[image['image_id']]


#iterate over total predictions in color analysis and get
#total true values from real data
real_values = []
for image in range(len(color_pred)):
    name = str(color_pred[image][0])
    prediction_id = [i for i in range(len(data_original['images'])) if data_original['images'][i]['file_name'] == name][0]
    #got name and id
    predictions_list = []
    for prediction_annotated in data_original['annotations']:
        if prediction_annotated['image_id'] == prediction_id:
            predictions_list.append(prediction_annotated['category_id']-1)
    real_values.append([name, predictions_list])

#for image in range(len(real_values)):
#    print(str(color_pred[image]) + '\n' + str(real_values[image]))

    p_ripe = [] #0
    t_ripe = [] #0
    p_half = [] #2
    t_half = [] #2
    p_green = [] #1
    t_green = [] #1

for image in range(len(real_values)):
    p_ripe.append(real_values[image][1].count(0))
    t_ripe.append(color_pred[image][1].count(0))
    p_half.append(real_values[image][1].count(2))
    t_half.append(color_pred[image][1].count(2))
    p_green.append(real_values[image][1].count(1))
    t_green.append(color_pred[image][1].count(1))

def square_err(y, x):
    SE_line = sum((y-x)**2)
    SE_mean = sum((y-y.mean())**2)
    r2 = 1-(SE_line/SE_mean)
    return r2

R_ripe = square_err(np.array(p_ripe), np.array(t_ripe))
R_half = square_err(np.array(p_half), np.array(t_half))
R_green = square_err(np.array(p_green), np.array(t_green))

print('ripe R2: {}\n half R2: {}\n green R2: {}\n'.format(
    R_ripe, R_half, R_green))
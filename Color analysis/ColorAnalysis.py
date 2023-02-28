import numpy as np
from PIL import Image, ImageDraw, ImageOps
import os
import json
import colorsys

directory = os.path.abspath("/home/jean/MEGA/YACHAY/9no SEMESTRE/TESIS/Database & Code/Authors methodology/")

# Mask R-CNN
mrcnn_dir_json = os.path.join(directory, 'MASK predict/mask-RCNN.json')
mrcnn_dir_img = os.path.join(directory, 'MASK predict/images/')
# YOLO
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

# Store in dictionary img_ids and img_names
images_ids = {}
for image in data_original['images']:
    images_ids[image['id']] = image['file_name'].replace('.jpg', '')
    final_names = image['file_name'].replace('.jpg', '')

#replace ids = ints into ids = name.
for image in data_mrcnn:
    image['image_id'] = images_ids[image['image_id']]


def color_predictor(color_array):
    c = color_array
    if ((c[0] >= 0) and (c[1] >= 140) and (c[2] >= 145)) and ((c[0] <= 5) and (c[1] <= 255) and (c[2] <= 255)):
        label = 0 #full ripe
    elif ((c[0] >= 174) and (c[1] >= 120) and (c[2] >= 135)) and ((c[0] <= 179) and (c[1] <= 255) and (c[2] <= 255)):
        label = 0 #full ripe
    elif ((c[0] >= 3) and (c[1] >= 144) and (c[2] >= 155)) and ((c[0] <= 18) and (c[1] <= 255) and (c[2] <= 255)):
        label = 2 #half ripe
    else:
        label = 1 #green
    return label
#========================================================
# Read original images folder
# Read masks images names [:-5]
predictions_dictionary = {}
tmp_dir_masks = os.path.join(directory, 'YOLO predict/tmpExperiment/')
for image in os.listdir(yolo_dir_masks):
    try:
        org_img = Image.open(os.path.join(original_dir_img, image[:-5]))
        img_name = image[:-5]
    except:
        org_img = Image.open(os.path.join(original_dir_img, image[:-6]))
        img_name = image[:-6]

    mask = Image.open(os.path.join(yolo_dir_masks, image))
    inverted_mask = ImageOps.invert(mask)
    # original image is masked, only tomato in a white background --> ignore white background on analysis
    org_img.paste(inverted_mask, (0,0), mask = inverted_mask)
    org_img.load()

    color_vals = []
    for i in range(640):
        for j in range(640):
            if not ((org_img.getpixel((i,j))[0] == 255) and (org_img.getpixel((i,j))[1] == 255) and (org_img.getpixel((i,j))[2] == 255)):
                color_vals.append([org_img.getpixel((i,j))[0], org_img.getpixel((i,j))[1], org_img.getpixel((i,j))[2]])

    average_color = np.nanmean(color_vals, axis=0)
    print(average_color)
    hsv_vector = colorsys.rgb_to_hsv(round(average_color[0])/255, round(average_color[1])/255, round(average_color[2])/255)
    hsv_vector = [round(hsv_vector[0]*179), round(hsv_vector[1]*255), round(hsv_vector[2]*255)]
    print(hsv_vector)
    #With the name of the file... store: the filename, array with the original values, array with the predictions
    result_prediction = color_predictor(hsv_vector)

    if img_name in predictions_dictionary.keys():
        predictions_dictionary[img_name].append(result_prediction)
    else:
        predictions_dictionary[img_name] = [result_prediction]

print(predictions_dictionary)
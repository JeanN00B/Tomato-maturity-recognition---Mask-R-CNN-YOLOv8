# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp
import warnings
from collections import OrderedDict

import mmcv
import numpy as np
from mmcv.utils import print_log
from terminaltables import AsciiTable
from torch.utils.data import Dataset

from mmdet.core import eval_map, eval_recalls
from .builder import DATASETS
from .pipelines import Compose


@DATASETS.register_module()
class MyDataset(Dataset):

    CLASSES = ('b_fully_ripened', 'b_green', 'b_half_ripened')

    PALETTE = [(246, 57, 16), (90, 246, 16), (240, 161, 31)]

    def load_annotations(self, ann_file):
        ann_list = mmcv.list_from_file(ann_file)

        data_infos = []
        for i, ann_line in enumerate(ann_list):
            if ann_line != '#':
                continue

            img_shape = ann_list[i + 2].split(' ')
            width = int(img_shape[0])
            height = int(img_shape[1])
            bbox_number = int(ann_list[i + 3])

            anns = ann_line.split(' ')
            bboxes = []
            labels = []
            for anns in ann_list[i + 4:i + 4 + bbox_number]:
                bboxes.append([float(ann) for ann in anns[:4]])
                labels.append(int(anns[4]))

            data_infos.append(
                dict(
                    filename=ann_list[i + 1],
                    width=width,
                    height=height,
                    ann=dict(
                        bboxes=np.array(bboxes).astype(np.float32),
                        labels=np.array(labels).astype(np.int64))
                ))

        return data_infos
        
#***************************************

dataset_A_train = dict(
    type='MyDataset',
    ann_file = 'image_list.txt',
    pipeline=train_pipeline
)
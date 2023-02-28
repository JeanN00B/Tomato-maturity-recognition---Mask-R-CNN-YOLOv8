_base_ = './mask_rcnn_r101_fpn_1x_coco.py'
model = dict(
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups = 32,
        base_width = 8,
        num_stages = 4,
        out_indices = (0, 1, 2, 3),
        frozen_stages = 1,
        style='pytorch',
        init_cfg=dict(
            type='Pretrained',
            checkpoint='open-mmlab://detectron2/resnet101_32x8d')),
    
    roi_head = dict(
        bbox_head = dict(num_classes = 3),

        mask_head = dict(num_classes = 3)))
    
runner = dict(type='EpochBasedRunner', max_epochs=30)
workflow = [('train', 10)]
dataset_type = 'CocoDataset'
classes = ('b_fully_ripened', 'b_green', 'b_half_ripened',)

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Resize', img_scale=(640, 640), keep_ratio=True),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(640, 640),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
            
data = dict(
     train=dict(
         type=dataset_type,
        img_prefix='/content/drive/MyDrive/Tomato-Dataset/Big_tomatoes_dataset-2/train/',
        classes=classes,
        ann_file='/content/drive/MyDrive/Tomato-Dataset/Big_tomatoes_dataset-2/annotations/train.json'),
    val=dict(
        type='OccludedSeparatedCocoDataset',
        img_prefix='/content/drive/MyDrive/Tomato-Dataset/Big_tomatoes_dataset-2/valid/',
        classes=classes,
        ann_file='/content/drive/MyDrive/Tomato-Dataset/Big_tomatoes_dataset-2/annotations/valid.json'),
    test=dict(
        type='OccludedSeparatedCocoDataset',
        img_prefix='/content/drive/MyDrive/Tomato-Dataset/Big_tomatoes_dataset-2/test/',
        classes=classes,
        ann_file='/content/drive/MyDrive/Tomato-Dataset/Big_tomatoes_dataset-2/annotations/test.json'),
        
    samples_per_gpu = 2,
    workers_per_gpu = 2)
    
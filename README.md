# pytorch-yolov7

https://blog.csdn.net/qq_45194640/article/details/125952860

https://github.com/qiaofengsheng/pytorch-yolov7

https://www.bilibili.com/video/BV1kU4y1i7Ts

使用yolov7训练自己的数据集

参考：https://github.com/WongKinYiu/yolov7

模型下载

https://ghproxy.com/https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt

# voc转yolo

```shell
python3 voc_to_yolo.py
```

# 修改

![](assets/20220822_145556_image.png)

# 使用官方的默认模型跑数据

1. 添加需要识别的图片或者视频到`inference/images`文件夹里。
2. 运行以下脚本

```shell


python3 detect.py
```

下面可以指定自己训练的模型文件

![](assets/20220822_173133_image.png)

3. 结果在下图

![](assets/20220822_152936_image.png)

traced_model.pt 这个文件是在运行 `python3 detect.py` 自动生成的记录文件，不是模型文件。


# 自己准备数据，训练模型

## 安装labelImg

https://github.com/heartexlabs/labelImg

```shell
pip3 install labelImg
labelImg
```

![](assets/20220822_211126_image.png)


![](assets/20220822_211309_image.png)



将自己标记的数据，整理好放到对应文件夹


![](assets/20220822_211430_image.png)


0 0.571000 0.637931 0.470000 0.494929

1 表示对应的分类，这里是两种cat和dog，cat是1，dog是0

第2，3个值表示识别的物体的中心点和图片的比例。

第2，3个值表示识别的物体的高度与宽度和原图的比例。

# 调参

## 针对特定的类别识别处理

https://blog.csdn.net/frcbob/article/details/123440979

![img.png](assets/special.png)

## 设置识别的准确度阈值

默认0.25

> 如果自己打标的数据，训练出来的模型，怎么也无法检测出目标，那么可以尝试修改下面阈值，改到比较低的值试试。

![img.png](assets/threshold.png)

# 应用场景

1. [判断带没带头盔](https://zhuanlan.zhihu.com/p/547878330)

# Refer

1. [YoloV7:训练自己得数据集详细教程](https://blog.csdn.net/zhangdaoliang1/article/details/125719437)
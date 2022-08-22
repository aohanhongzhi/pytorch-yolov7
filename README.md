# pytorch-yolov7

使用yolov7训练自己的数据集

参考：https://github.com/WongKinYiu/yolov7

模型下载

https://ghproxy.com/https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt

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

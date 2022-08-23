#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import cv2
from torchvision import transforms
import numpy as np
from utils.datasets import letterbox
from utils.general import non_max_suppression_kpt
from utils.plots import output_to_keypoint, plot_skeleton_kpts

# In[2]:


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# device = torch.device("cpu")
# torch.backends.cudnn.enabled = False
weigths = torch.load('/home/eric/Project/Python/pytorch-yolov7/yolov7-w6-pose.pt')
model = weigths['model']
model = model.half().to(device)
_ = model.eval()

# In[3]:


image = cv2.imread('/home/eric/Project/Python/pytorch-yolov7/2022-08-23_18-39.png')
image = letterbox(image, 960, stride=64, auto=True)[0]
image_ = image.copy()
image = transforms.ToTensor()(image)
image = torch.tensor(np.array([image.numpy()]))
image = image.to(device)
image = image.half()

output, _ = model(image)

# In[6]:


output = non_max_suppression_kpt(output, 0.25, 0.65, nc=model.yaml['nc'], nkpt=model.yaml['nkpt'], kpt_label=True)
output = output_to_keypoint(output)
nimg = image[0].permute(1, 2, 0) * 255
nimg = nimg.cpu().detach().numpy().astype(np.uint8)

# TODO 保留图片的原色
nimg = cv2.cvtColor(nimg, cv2.COLOR_RGB2BGR)
for idx in range(output.shape[0]):
    plot_skeleton_kpts(nimg, output[idx, 7:].T, 3)

# 将结果保存下来
cv2.imwrite('person4.jpg', nimg)

# In[12]:


# get_ipython().run_line_magic('matplotlib', 'inline')
# plt.figure(figsize=(8,8))
# plt.axis('off')
# plt.imshow(nimg)
# plt.show()


# In[ ]:

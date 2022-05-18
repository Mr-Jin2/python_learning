# 1. 熟悉vgg16的网络结构
# 2. 观察其每一层的输出shape
# 结论：
# PIL.Image读入图片格式为PIL.JpegImagePlugin.JpegImageFile， shape是(W, H)
# cv2 读入图片格式为ndarray， shape是(H, W, C)

import torch
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np
from PIL import Image


img_pil = Image.open('demo.jpg')
img_pil.show()
print(f'img_pil type is:{type(img_pil)}, img_pil shape is {img_pil.size}') #(W, H)

img_cv = cv2.imread('demo.jpg')
cv2.imshow('img_cv',img_cv)
cv2.waitKey(0) # 按0关闭窗口
print(f'img_cv type is:{type(img_cv)}, img_cv shape is {img_cv.shape}') #(H, W, C)


conv = nn.Conv2d(in_channels=3,out_channels=64,kernel_size=3,padding=1) # 构造卷积
img_reshape = np.reshape(img_cv, (-1, 3, 427, 640)) # reshape成nn需要的shape
img_tensor = torch.tensor(img_reshape).float() # 转化为Tensor格式
img_conv = conv(img_tensor)
print(f'img_conv type is:{type(img_conv)}, img_conv shape is {img_conv.shape}')
img_array = img_conv[0,:3].reshape(427, 640, 3).detach().numpy()
cv2.imshow('img_array',img_array)
cv2.waitKey(0)


class VGG16(nn.Module):

    def __init__(self):
        super(VGG16, self).__init__()

        # 输入img大小为：3 * 224 * 224
        # block1
        self.conv1_1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)  # 64 * 224 * 224
        self.conv1_2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3) # 64 * 224 * 224
        self.maxpool1 = nn.MaxPool2d((2, 2), padding=(1, 1)) # 64 * 112 * 112

        # block2
        self.conv2_1 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3)  # 128 * 112 * 112
        self.conv2_2 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3)
        self.maxpool2 = nn.MaxPool2d((2, 2), padding=(1, 1))

        # block3
        self.conv3_1 = nn.Conv2d(128, 256, 3)  # 256 * 54 * 54                             (56 - 3 + 2*0)/1 + 1 = 54
        self.conv3_2 = nn.Conv2d(256, 256, 3, padding=(1, 1))  # 256 * 54 * 54             (54 - 3 + 2*1)/1 + 1 = 54
        self.conv3_3 = nn.Conv2d(256, 256, 3, padding=(1, 1))  # 256 * 54 * 54             (54 - 3 + 2*1)/1 + 1 = 54
        self.maxpool3 = nn.MaxPool2d((2, 2), padding=(1, 1))  # pooling 256 * 28 * 28      (54 - 2 + 2*1)/2 + 1 = 28

        # block3
        self.conv4_1 = nn.Conv2d(256, 512, 3)  # 512 * 26 * 26                             (28 - 3 + 2*0)/1 + 1 = 26
        self.conv4_2 = nn.Conv2d(512, 512, 3, padding=(1, 1))  # 512 * 26 * 26             (26 - 3 + 2*1)/1 + 1 = 26
        self.conv4_3 = nn.Conv2d(512, 512, 3, padding=(1, 1))  # 512 * 26 * 26             (26 - 3 + 2*1)/1 + 1 = 26
        self.maxpool4 = nn.MaxPool2d((2, 2), padding=(1, 1))  # pooling 512 * 14 * 14      (26 - 2 + 2*1)/2 + 1 = 14

        # block4
        self.conv5_1 = nn.Conv2d(512, 512, 3)  # 512 * 12 * 12                             (14 - 3 + 2*0)/1 + 1 = 12
        self.conv5_2 = nn.Conv2d(512, 512, 3, padding=(1, 1))  # 512 * 12 * 12             (12 - 3 + 2*1)/1 + 1 = 12
        self.conv5_3 = nn.Conv2d(512, 512, 3, padding=(1, 1))  # 512 * 12 * 12             (12 - 3 + 2*1)/1 + 1 = 12
        self.maxpool5 = nn.MaxPool2d((2, 2), padding=(1, 1))  # pooling 512 * 7 * 7        (12 - 2 + 2*1)/2 + 1 =7

        # view

        self.fc1 = nn.Linear(512 * 7 * 7, 4096)  # 512 * 7 * 7 = 25088 ————> 4096
        self.fc2 = nn.Linear(4096, 4096)  # 4096 ————> 4096
        self.fc3 = nn.Linear(4096, 1000)  # 4096 ————> 1000
        # softmax 1 * 1 * 1000

        def forward(self, x):
            # x.size(0)即为batch_size
            in_size = x.size(0)

            out = self.conv1_1(x)  # 222
            out = F.relu(out)
            out = self.conv1_2(out)  # 222
            out = F.relu(out)
            out = self.maxpool1(out)  # 112

            out = self.conv2_1(out)  # 110
            out = F.relu(out)
            out = self.conv2_2(out)  # 110
            out = F.relu(out)
            out = self.maxpool2(out)  # 56

            out = self.conv3_1(out)  # 54
            out = F.relu(out)
            out = self.conv3_2(out)  # 54
            out = F.relu(out)
            out = self.conv3_3(out)  # 54
            out = F.relu(out)
            out = self.maxpool3(out)  # 28

            out = self.conv4_1(out)  # 26
            out = F.relu(out)
            out = self.conv4_2(out)  # 26
            out = F.relu(out)
            out = self.conv4_3(out)  # 26
            out = F.relu(out)
            out = self.maxpool4(out)  # 14

            out = self.conv5_1(out)  # 12
            out = F.relu(out)
            out = self.conv5_2(out)  # 12
            out = F.relu(out)
            out = self.conv5_3(out)  # 12
            out = F.relu(out)
            out = self.maxpool5(out)  # 7

            # 展平
            out = out.view(in_size, -1)

            out = self.fc1(out)
            out = F.relu(out)
            out = self.fc2(out)
            out = F.relu(out)
            out = self.fc3(out)

            out = F.log_softmax(out, dim=1)

            return out





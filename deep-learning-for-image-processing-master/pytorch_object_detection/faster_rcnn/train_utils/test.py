import torch
# from torch.backends import cudnn
# a = torch.Tensor([1.])
# print(a.cuda())
# print(cudnn.is_acceptable(a.cuda()))
image_mean = [0.485, 0.456, 0.406]
mean = torch.as_tensor(image_mean)
mean = mean[:, None, None]
print(mean)

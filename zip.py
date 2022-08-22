import torch
state_dict = torch.load("./traced_model.pt")#加载原来的模型
torch.save(state_dict, "./traced.pt", _use_new_zipfile_serialization=False)#不是zip 
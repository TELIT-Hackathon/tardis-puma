from torch.utils.data import Dataset
import json
import torch




class MyDataset(Dataset):
    def __init__(self):
        with open("./combined-data-with-latency2-ready.json", "r") as f:
            data = json.load(f)
        
        self.data = []
        self.target = []
        for d in data:
            if "h" in d.keys() and "b" in d.keys() and "c" in d.keys() and "s" in d.keys():
                self.data.append([d["b"], d["c"], d["s"]])
                self.target.append(d["h"])
        # self.data = torch.randn(10, 3, 24, 24)
        # self.target = torch.randint(0, 10, (10,))
        
    def __getitem__(self, index):
        x = self.data[index]
        y = self.target[index]
        
        return {'data': x, 'target': y}
    
    def __len__(self):
        return len(self.data)

# dataset = MyDataset()
# loader = DataLoader(
    # dataset,
    # batch_size=2,
    # num_workers=2
# )

# for batch in loader:
    # data = batch['data']
    # target = batch['target']
    # print(data.shape)
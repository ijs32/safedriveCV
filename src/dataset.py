import cv2
from torch.utils.data import DataLoader, Dataset

class ImgDataset(Dataset):
    def __init__(self, images, transform=None):
        self.images = images
        self.transform = transform
        
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        # print(self.images[idx])
        img = cv2.imread(f"../training_data/classification_training_data/{self.images[idx]}")
        
        label = self.images[idx].split("_")[0]
        if label == "blacklist":
            label = 1
        elif label == "whitelist":
            label = 0

        if self.transform:
            img = self.transform(img)
        return img, label
    
    def get_dataloader(self):
        """Get a dataloader for the dataset."""
        return DataLoader(
            self, batch_size=16, shuffle=True)
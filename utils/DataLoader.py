import torch
import torch.utils.data as data
import torchvision.transforms as transforms
import PIL.Image as Image

import glob
import os
import random


class Loader(data.DataLoader):
    def __init__(self, dataset_dir, styles, transforms):
        super(Loader, self).__init__(self)
        self.dataset_dir = dataset_dir
        self.styles = styles
        self.image_path_A = glob.glob(f'{os.path.join(dataset_dir, styles[0])}/*')
        self.image_path_B = glob.glob(f'{os.path.join(dataset_dir, styles[1])}/*')
        self.transform = transforms

    def __getitem__(self, index_A):
        index_B = random.randint(0, len(self.image_path_B)-1)

        item_A = self.transform(Image.open(self.image_path_A[index_A]))
        item_B = self.transform(Image.open(self.image_path_B[index_B]))

        return [item_A, item_B, self.image_path_A[index_A]]

    def __len__(self):
        return len(self.image_path_A)
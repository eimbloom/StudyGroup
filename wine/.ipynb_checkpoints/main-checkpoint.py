import sklearn
import torch
import torchvision
import pandas as pd
import lightning as pl


class WineDataset(pl.LightningDataModule):
    def __init__(self, batch_size: int):
        super().__init__()
        self.data_dir = "coursework_resit_other.csv"
        self.batch_size = batch_size

    def setup(self, stage: str):
        dataset = pd.read_csv('coursework_resit_other.csv')


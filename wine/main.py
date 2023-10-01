import pandas as pd
import lightning as pl
from sklearn.model_selection import train_test_split


class WineDataset(pl.LightningDataModule):
    def __init__(self, batch_size: int):
        super().__init__()
        self.data_dir = "coursework_resit_other.csv"
        self.batch_size = batch_size

    def setup(self, stage: str):
        dataset = pd.read_csv('coursework_resit_other.csv')
        x_train, x_test, y_train, y_test = train_test_split(
            dataset.drop(['quality'], axis=1),
            dataset['quality'],
            test_size=0.1,
            random_state=42
        )



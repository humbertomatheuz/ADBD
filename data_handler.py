import pandas as pd

class DataHandler:
    def load_data(self, file_path):
        df = pd.read_excel(file_path)
        return df

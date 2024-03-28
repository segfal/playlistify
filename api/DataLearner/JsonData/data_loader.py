import os
import json
import random
class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data
    
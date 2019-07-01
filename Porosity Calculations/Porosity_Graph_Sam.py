import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib






def graph(path):
    print(path)
    data = pd.read_csv(path)
    print(data.shape)
    print(data[0].max())




if __name__ == "__main__":
    path = "/media/samschickler/1F6D-D692/Porosity"
    graph(path)
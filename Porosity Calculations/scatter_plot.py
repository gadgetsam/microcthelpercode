import pandas as pd
from concat_csv import concat_csv
import matplotlib.pyplot as plt
def scatter_plot(path, index):
    data = concat_csv(path)
    data.columns = ["porosity", "slice", "time"]
    print(data.shape)
    number_of_graphs = 10
    max_slice = 600
    fig, axs = plt.subplots(1, 1)
    df_filtered_0 = data[(data.slice == 100)].sort_values("time")

    for index in range(number_of_graphs):
        slice_number = (index+1)*max_slice/number_of_graphs
        df = data[(data.time == slice_number)].sort_values("slice")
        color = plt.cm.Blues((index+4)/(number_of_graphs+3))
        axs.plot(df.slice, df.porosity, color=color)
        axs.set_xlim(0, 1300)
        axs.set_ylim(0, .3)
        axs.set_xlabel('Slice')
        axs.set_ylabel("Porosity")
        axs.grid(True)
    # fig.tight_layout()
    fig.set_size_inches(20,20)
    plt.show()
    # plt.savefig(str(index)+'.png')
scatter_plot('/media/samschickler/1F6D-D692/Porosity',0)
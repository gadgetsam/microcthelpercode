import pandas as pd
from concat_csv import concat_csv
import matplotlib.pyplot as plt
def scatter_plot(path, index, title):
    data = concat_csv(path)
    data.columns = ["porosity", "slice", "time"]
    print(data.shape)
    data_t = data.sort_values('time')
    number_of_graphs = 4
    max_slice = data_t.time.unique()[-1]
    fig, axs = plt.subplots(1, 1)
    df_filtered_0 = data[(data.slice == 100)].sort_values("time")
    print(data_t.time.unique())
    for index in range(number_of_graphs):
        slice_number = round((index+1)*max_slice/number_of_graphs)
        print(slice_number)
        df = data[(data.time == slice_number)].sort_values("slice")
        print(df.shape)
        color = plt.cm.Blues((index+4)/(number_of_graphs+3))
        axs.plot(df.slice, df.porosity, linewidth=index, color=color)
        axs.set_xlim(0, 1300)
        axs.set_ylim(0, .04)
        axs.set_xlabel('Slice')
        axs.set_ylabel("Porosity")
        axs.set_title(title)
        axs.grid(True)
    # fig.tight_layout()
    fig.set_size_inches(20,20)
    # plt.savefig(str(index)+'.png')
scatter_plot('/home/samschickler/Desktop/csvs_first_try/csvs/csvs0',0,"FiberForm_13A_air_200torr")
scatter_plot('/home/samschickler/Desktop/csvs_first_try/csvs/csvs1',0,"FiberForm_15A_air_200torr")

scatter_plot('/home/samschickler/Desktop/csvs_first_try/csvs/csvs2',0,"FiberForm_18A_air_200torr")


plt.show()

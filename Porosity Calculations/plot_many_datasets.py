import pandas as pd
from concat_csv import concat_csv
import matplotlib.pyplot as plt
def scatter_plot(paths,  titles):
    fig, axs = plt.subplots(1, 1)
    colors = ["Blues", "Reds", "Greens"]
    for set_number, _ in enumerate(paths):
        print(paths[set_number])
        data = concat_csv(paths[set_number])
        data.columns = ["porosity", "slice", "time"]
        print(data.shape)
        data_t = data.sort_values('time')
        number_of_graphs = 4
        max_slice = data_t.time.unique()[-1]

        df_filtered_0 = data[(data.slice == 100)].sort_values("time")
        print(data_t.time.unique())
        for index in range(1,number_of_graphs):
            slice_number = int(round((index+1)*max_slice/number_of_graphs))
            print(slice_number)
            df = data[(data.time == slice_number)].sort_values("slice")
            print(df.shape)
            color = plt.get_cmap(colors[set_number])((index+4)/(number_of_graphs+3))
            axs.plot( df.porosity, df.slice*.81,linewidth=index/2, color=color, label=titles[set_number]+" Time point: "
                                                                                  +str(slice_number))

        axs.legend()
        axs.set_xlim(0, .075)
        axs.set_ylim(0, 2016*.81)
        axs.labelsize = 50
        axs.set_xlabel("Porosity", size=20)
        axs.set_ylabel('Depth in um', size=20)
        axs.set_title("Changing Porosity in Terms of Slice and Time")
        axs.grid(True)
    # fig.tight_layout()
    fig.set_size_inches(20,20)
    # plt.savefig(str(index)+'.png')
paths = ['/home/samschickler/Desktop/csvs_first_try/csvs/csvs0', '/home/samschickler/Desktop/csvs_first_try/csvs/csvs1',
         '/home/samschickler/Desktop/csvs_first_try/csvs/csvs2']
names = ["FiberForm_13A_air_200torr","FiberForm_15A_air_200torr","FiberForm_18A_air_200torr"]
scatter_plot(paths, names)



plt.show()

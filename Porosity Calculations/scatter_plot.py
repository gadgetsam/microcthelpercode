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
        axs.plot(df.slice, df.porosity, linewidth=(index+1)/2, color="blue")
        axs.set_xlim(0, 1300)
        axs.set_ylim(0, .3)
        axs.set_xlabel('Slice')
        axs.set_ylabel("Porosity")
        axs.grid(True)
    # fig.tight_layout()
    fig.set_size_inches(20,20)
    plt.savefig(str(index)+'.png')
# plt.figure(figsize=(16,10), dpi= 80)
# fig, axes = joypy.joyplot(data, column=["porosity", "time"], by="slice", ylim='own', figsize=(14,10))
#
# # Decoration
# plt.title('Joy Plot of City and Highway Mileage by Class', fontsize=22)
# plt.show()
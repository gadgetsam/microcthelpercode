import pandas as pd
from concat_csv import concat_csv
import matplotlib.pyplot as plt
from fwhm import fwhm_calc
def scatter_plot(paths, data_set_names, time_point=80, inverted_depth=True, num_time_points=1, rolling_mean =1,
                 save=False, save_path = None, title=False, multidataset = False, axs_inverted=False,
                 time_spaceing=False, legend =False, size_1 =50, size_2 =50, differences=False, fiber_max = .075):
    fig, axs = plt.subplots(1, 1)
    colors = ["Blues", "Reds", "Greens"]
    for set_number, _ in enumerate(paths):
#         print(paths[set_number])
        data = concat_csv(paths[set_number])
        data.columns = ["fiber_density", "slice", "time"]
        data.time = data.time.apply(lambda x: int(x[17:22]))
#         print(data.shape)
        data_t = data.sort_values('time')

        data_s = data.sort_values('slice')
        max_time = data_t.time.iloc[-1]
        max_slice = data_s.slice.iloc[-1]
        # print(data_t.loc[data_t["slice"]==200].head(180))
        if differences:
#

            for x in range(1, max_slice):
                data_t.loc[data_t["slice"]==x, "fiber_density"] = data_t.loc[data_t["slice"]==x, "fiber_density"].diff()
            data = data_t
#             print(data_t.loc[data_t["slice"]==200].head(180))

        if time_spaceing:
            spaceing = time_spaceing
        else:
            spaceing = max_time / (num_time_points-1)-1
        axs_select_x = 0 if axs_inverted else 1
        axs_select_y = 1 if axs_inverted else 0


#         df_filtered_0 = data[(data.slice == 100)].sort_values("time")
#         print(data_t.time.unique())
        for index in range(1, num_time_points+1):
            time_point = time_point if num_time_points == 1 else int(round((index-1)*spaceing+1))
            if index == 1:
                time_point = 10
            print(time_point)
            df = data[(data.time == time_point)].sort_values("slice")
#             print(df.shape)
            if rolling_mean >1:
                df.fiber_density = df.fiber_density.rolling(window=rolling_mean).mean()
            color = plt.get_cmap(colors[set_number])((index+3)/(num_time_points+3))
            slice_axs = [df.slice * .81/1000,"Depth (mm)", max_slice*.81 / 1000 if inverted_depth else 0, 0 if inverted_depth else max_slice * .81/1000] #Fiber Volume Ratio Decay Per Second'
            fiber_axs = [df.fiber_density if not differences else -1 * df.fiber_density,'Fiber Volume Ratio' if not differences else '', 0, fiber_max]
            combined_axs = [slice_axs, fiber_axs]
            # print(len(df.slice), combined_axs[axs_select_y][0])
            # fwhm_calc(df)
            axs.plot(combined_axs[axs_select_x][0], combined_axs[axs_select_y][0], linewidth=index + 1 if num_time_points > 1 else 1, color=color,
                     label=data_set_names+", %s Sec" % time_point*4 if multidataset else str((time_point-1)*4)+" Sec" )

        if legend:
            axs.legend(prop={'size': size_1})
        axs.set_xlim(combined_axs[axs_select_x][2],combined_axs[axs_select_x][3])
        axs.set_ylim(combined_axs[axs_select_y][2],combined_axs[axs_select_y][3])
        plt.xticks(fontsize=size_1)

        plt.yticks(fontsize=size_1)
        xticks = axs.xaxis.get_major_ticks()
        xticks[0].set_visible(False)
        axs.labelsize = size_1
        plt.locator_params(axis='y', nbins=3)
        plt.locator_params(axis='x', nbins=4)

        axs.set_xlabel(combined_axs[axs_select_x][1], size=size_2)
        axs.set_ylabel(combined_axs[axs_select_y][1], size=size_2)
        # axs.set_title("Changing Porosity in Terms of Slice" + (" and Time" if num_time_points != 1 else
        #                                                        " at Time Point: "+str(time_point))
        #                                                     + (" (With Rolling Average Over " + str(rolling_mean)
        #                                                        + " Slices)" if rolling_mean >1 else ""))
        if title:
            axs.set_title(data_set_names[0])
    # fig.tight_layout()
    fig.set_size_inches(40,20 if not differences else 8)
    if(save):
        save=(save_path +"NASA_Ablation_Graph" + ("_"+data_set_names[0] if not multidataset else "")+("_inverted" if inverted_depth else "") +
              ("_time_point_" +str(time_point) if num_time_points == 1 else "_time_points_" +str(num_time_points)) +
              ("_rolling_mean_"+str(rolling_mean) if rolling_mean>1 else "") +'.png')
        print(save)
        plt.savefig(save)





# paths = ['/home/samschickler/Desktop/csvs_first_try/csvs/csvs0', '/home/samschickler/Desktop/csvs_first_try/csvs/csvs1',
#          '/home/samschickler/Desktop/csvs_first_try/csvs/csvs2']
# names = ["FiberForm_13A_air_200torr","FiberForm_15A_air_200torr","FiberForm_18A_air_200torr"]
# time_point_list =[9,5,5]
# # for x in range(10,100,5):
# for x in range(1):
#     scatter_plot([paths[x]], [names[x]], time_point=2, inverted_depth=False, num_time_points=5, rolling_mean=200, save=True,
#                  save_path="/home/samschickler/Desktop/graphs/", multidataset=False, title=True, axs_inverted=True,
#                  time_spaceing=20, legend=False, size_1=50, size_2=50, differences=True, fiber_max=.001)

paths = ['/home/samschickler/Desktop/graphs_7_17/test/Fiber_13A_200_05', '/home/samschickler/Desktop/graphs_7_17/test/Fiber_15A_200_07',
         '/home/samschickler/Desktop/graphs_7_17/test/Fiber_18A_200_08']
names = ["FiberForm_13A_air_200torr","FiberForm_15A_air_200torr","FiberForm_18A_air_200torr"]
time_point_list =[3,3,3]
# for x in range(10,100,5):
for x in range(0,1):

    scatter_plot([paths[x]], [names[x]], time_point=2, inverted_depth=False, num_time_points=time_point_list[x], rolling_mean=100, save=True,
                 save_path="graphs/dif/", multidataset=False, title=False, axs_inverted=True,
                 time_spaceing=False, legend=False, size_1=70, size_2=70, differences=True, fiber_max=.004)
plt.show()
# time_point_list =[3,3,3]
# # for x in range(10,100,5):
# for x in range(3):
#     scatter_plot([paths[x]], [names[x]], time_point=5, inverted_depth=False, num_time_points=time_point_list[x], rolling_mean=40, save=True,
#                  save_path="graphs/", multidataset=False, title=False, axs_inverted=True,
#                  time_spaceing=False, legend=False, size_1=70, size_2=70, fiber_max=.3)
#
#
#
# plt.show()
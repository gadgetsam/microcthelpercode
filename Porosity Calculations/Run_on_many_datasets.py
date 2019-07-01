from Run_Porosity_Multithread import run_on
import os
from scatter_plot import scatter_plot
from calculate_porosity import calculate_porosity

def input_function(image):  # this is used to specify all the parameters to crop
    return calculate_porosity(image, circle_mask=True, circle_mask_size=.8, image_loaded=True)



folders=["/data/nasa-ablation/FiberForm_13A_air_200torr_05/FiberForm_13A_air_200torr_05",
         "/data/nasa-ablation/FiberForm_13A_air_200torr_05/FiberForm_15A_air_200torr_07",
         "/data/nasa-ablation/FiberForm_13A_air_200torr_05/FiberForm_18A_air_200torr_08"]
for index, folder in enumerate(folders):
    os.mkdir("csvs"+str(index))
    print(index)
    run_on(input_function, folder, "csvs"+str(index))
    scatter_plot("csvs"+str(index), index)


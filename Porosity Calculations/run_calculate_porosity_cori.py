import os
import time
import numpy as np
from calculate_porosity import calculate_porosity
import cv2
import re
import csv

def run_on_files(input_path, output_path, id, directory):
    pattern = re.compile(r"([0-9]+)\.rec")
    f = open(output_path + "/" + str(id) + ".csv", "w")
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    file_list = os.listdir(input_path)
    image_files = [os.path.join(input_path, f) for f in file_list]
    info = zip(image_files, file_list)
    for in_file, file_name in info:
        porosity_calc = input_function(in_file)
        id_file = pattern.search(str(file_name)).group(1)
        id_directory = directory[-5:]

        data = [porosity_calc, id_file, id_directory]
        out = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        out.writerow(data)
    return


def input_function(image):  # this is used to specify all the parameters to crop
    return calculate_porosity(image, circle_mask=True, circle_mask_size=.8, image_loaded=False)

def job_array_run(whole_datasets, whole_datasets_out, base_folder, padding=5, test = False):

    if test:
        id =70
    else:
        id = os.environ['SLURM_ARRAY_TASK_ID']
        print(id)
    folder_list = []
    for dataset, path_out in zip(whole_datasets, whole_datasets_out):
        if not os.path.isdir(path_out):
            os.mkdir(path_out)
        folders = os.listdir(dataset)
        folder_list += [[x, dataset, path_out] for x in folders]
    print(len(folder_list))
    folder = folder_list[int(id)]
    if base_folder in folder[0] and os.path.isdir(os.path.join(folder[1], folder[0])):
        print(folder)
        run_on_files(os.path.join(folder[1], folder[0]), folder[2], id, folder)
whole_datasets= ["/global/cscratch1/sd/sschickl/data/FiberForm_13A_air_200torr_05",
         "/global/cscratch1/sd/sschickl/data/FiberForm_15A_air_200torr_07",
         "/global/cscratch1/sd/sschickl/data/FiberForm_18A_air_200torr_08"]
whole_datasets_out = ["Fiber_13A_200_05", "Fiber_15A_200_07", "Fiber_18A_200_08"]
base_folder = "rec_8bit_phase_"
job_array_run(whole_datasets, whole_datasets_out, base_folder, test=False)
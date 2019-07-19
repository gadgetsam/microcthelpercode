import os
import time
import numpy as np

import cv2
def crop_custom(img_file, out_file, circle_mask=False, radius=1, center=[0,0], square_mask=False, square_mask_dim=[100,1000,100,1000]):
    if("tif" in img_file):
        crop_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
        x,y = crop_img.shape[0], crop_img.shape[1]
        center_x, center_y = x/2 + center[0], y/2 - center[1] # treat like origin
        if circle_mask:
            X,Y = np.ogrid[:x,:y]
            #have list of points on the image, check if the distance from center > radius
            mask = np.add(np.square(X - center_y), np.square(Y - center_x)) >= radius**2
            crop_img[mask] = 0
        cv2.imwrite(out_file, crop_img)
        return None
def run_on_files(input_path, output_path):
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    file_list = os.listdir(input_path)
    image_files = [os.path.join(input_path, f) for f in file_list]
    cropped_files = [os.path.join(output_path, f) for f in file_list]
    filenames = zip(image_files,cropped_files)
    filenames = zip(image_files,cropped_files)
    for in_file, out_file in filenames:
        input_function(in_file, out_file)
    return
def input_function(in_file, out_file):
    crop_custom(in_file, out_file, True, radius=340, center=[12,-7])

def job_array_run(whole_dataset, whole_dataset_out, base_folder, padding=5, test = False):
    if not os.path.isdir(whole_dataset_out):
        os.mkdir(whole_dataset_out)
    if test:
        id =70
    else:
        id = os.environ['SLURM_ARRAY_TASK_ID']
        print(id)

    folder = os.listdir(whole_dataset)[int(id)]
    if base_folder in folder and os.path.isdir(os.path.join(whole_dataset, folder)):
        print(folder)
        run_on_files(os.path.join(whole_dataset, folder), os.path.join(whole_dataset_out, folder))






# scratch_path = id = os.environ['SCRATCH']
# whole_dataset = "/media/samschickler/1F6D-D692/FiberForm_19A_air_760torr_13_fast"
# whole_dataset_out = "/media/samschickler/1F6D-D692/FiberForm_19A_air_760torr_13_fast_cropped"


whole_dataset= "/global/cscratch1/sd/sschickl/data/FiberForm_19A_air_760torr_13_fast"
whole_dataset_out = "/global/cscratch1/sd/sschickl/data/FiberForm_19A_air_760torr_13_fast_cropped"
base_folder = "rec_8bit_phase_"
job_array_run(whole_dataset, whole_dataset_out, base_folder, test=False)
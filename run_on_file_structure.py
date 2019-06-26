""""Author: Sam Schickler"""
import os
from skimage.external import tifffile as tiff
from crop import crop
import multiprocessing
import time
def run_on(function, folder_path, output_path, num_threads = 16):
    folder_path_len = len(folder_path)
    directory_list = [x[0] for x in os.walk(folder_path)]
    queue = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    for directory in directory_list:
        if 'rec' in directory:

            queue.put(directory)
    process_list = []
    for _ in range(num_threads):
        temp = multiprocessing.Process(target=run_on_files, args=(function,folder_path_len, queue, queue2))
        temp.start()
        process_list.append(temp)
    while not queue.empty():
        print(queue.qsize())
        time.sleep(1)
    while queue2.qsize != num_threads:
        time.sleep(1)
    for process in process_list:
        process.stop()



def run_on_files(function, folder_path_len, queue, queue2):
    while not queue.empty():
        directory = queue.get()
        try:
            os.rmdir(output_path + directory[folder_path_len:])
        except:
            pass
        os.mkdir(output_path + directory[folder_path_len:])
        file_list = [x[2] for x in os.walk(directory)]
        for file in file_list[0]:
            image = tiff.imread(directory + "/" + file)
            out_image = function(image)
            tiff.imsave(output_path + directory[folder_path_len:] + "/" + file, image)
            # print(file)
    queue2.put(1)






folder_path = '/media/samschickler/1F6D-D692/FiberForm_19A_air_760torr_13_fast'
output_path = '/media/samschickler/1F6D-D692/Output'
def input_function(image):
    crop(image, circle_mask=True, circle_mask_size=1, square_mask=True, square_mask_dim=[100,1000,100,1000])
run_on(input_function, folder_path, output_path)


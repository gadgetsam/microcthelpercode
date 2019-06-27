""""Author: Sam Schickler"""
import os
from skimage.external import tifffile as tiff
from calculate_porosity import calculate_porosity
import multiprocessing
import time
import csv
import re

""""
Definition: run_on runs function on all the images in all the folders inside a folder and then outputs the images into an output directory while keeping the file structure the same. It does this in parallel 

Input: 
	function is a function with 1 input which is the image I recommend wrapping it in another function so you can customize it more like below
	folder_path is a path to the highest level folder you want to run it on
	output_path is to an already created empty directory that you want it to output to
	num_threads is the number of workers that it will spawn 
	"""


def run_on(function, folder_path, output_path, num_threads=4):
    """
    Definition: run_on_files is a worker function that takes a directory and then runs a function on all the files in a directory
    inputs:
        queue is the main queue that holds all the directories that the workers need to process
        queue2 is used for stopping the processes when done
    """

    def run_on_files(function, folder_path_len, output_path, process_num,queue, queue2):
        pattern = re.compile(r"([0-9]+)\.rec")
        f = open(output_path + "/porosity" + str(process_num) + ".csv", "w")
        while not queue.empty():  # runs until the queue is empty
            directory = queue.get()  # gets a directory and removes it from the queue
             # makes a new folder in the output path for the directory


            file_list = [x[2] for x in os.walk(directory)]
            for file in file_list[0]:
                # print(file)
                if ".tif" in file:
                    image = tiff.imread(directory + "/" + file)  # loads file
                    porosity_calc = function(image)
                    id_file = pattern.search(str(file)).group(1)
                    id_directory = directory[-5:]

                    data = [porosity_calc, id_file, id_directory]
                    out = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
                    out.writerow(data)

                # saves file
                # print(file)
        queue2.put(1)  # tells the main process that it is done



    ## START of run_on()


    folder_path_len = len(folder_path)
    directory_list = [x[0] for x in os.walk(folder_path)]  # creates list of directories
    queue = multiprocessing.Queue()  # creates a main queue for storing all the directories
    queue2 = multiprocessing.Queue()  # creates a queue for communicating when all the processes are done
    for directory in directory_list:
        if 'rec' in directory:  # filters the directories to only the ones with rec in the title

            queue.put(directory)  # adds the directory to the queue
    process_list = []
    for x in range(num_threads):  # spawns each of the processes with the run_on_files functions
        temp = multiprocessing.Process(target=run_on_files, args=(function, folder_path_len, output_path,x, queue, queue2))
        temp.start()
        process_list.append(temp)
    while not queue.empty():  # waits until all the queue is empty processes might still be processing their final function
        print(queue.qsize())
        time.sleep(1)
    while queue2.qsize != num_threads:  # this is a final check to make sure all the processes are really done
        time.sleep(1)
    for process in process_list:
        process.stop()

if __name__ == "__main__":
    folder_path = '/media/samschickler/1F6D-D692/FiberForm_19A_air_760torr_13_fast'
    output_path = '/media/samschickler/1F6D-D692/Porosity'


    def input_function(image):  # this is used to specify all the parameters to crop
        return calculate_porosity(image, circle_mask=True, circle_mask_size=.8, image_loaded=True)


    run_on(input_function, folder_path, output_path)

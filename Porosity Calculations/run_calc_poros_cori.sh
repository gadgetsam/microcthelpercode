#!/bin/bash
#SBATCH --qos=shared
#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --time=20:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --array=0-402


module load python/3.6-anaconda-4.4
source activate crop
srun python run_calculate_porosity_cori.py
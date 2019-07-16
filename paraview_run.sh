#!/bin/bash
#SBATCH --qos=debug
#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --time=1:00
#SBATCH --array=0-2


module load ParaView
start_pvbatch.sh 1 1 haswell 00:1:00 default debug `pwd`/pv-test.py


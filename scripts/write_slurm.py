#!/usr/bin/env python3


walltime=1 

job_name = "watermelon_blast"
hours = "00:01:00"
queue_name = "cloud72"
email = "vjindal@uark.edu"

print("#!/bin/bash")
print("#SBATCH --job-name=" + job_name)
print("#SBATCH --time=" + hours)
print("#SBATCH -p " + queue_name)
print("#SBATCH -q cloud")
print("#SBATCH -N 1")
print("#SBATCH -n 1")
print("#SBATCH -c 1")
print("#SBATCH --output=%x.%j.out")
print("#SBATCH --error=%x.%j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=" + email)
print("")
print("module purge")
print("module load blast")
print("")
print("cd $SLURM_SUBMIT_DIR")
print("blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn")

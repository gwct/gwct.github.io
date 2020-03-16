#!/bin/bash
#SBATCH --job-name=[job name]
#SBATCH --mail-user=[your email]
#SBATCH --mail-type=ALL
#SBATCH --partition=good_lab_cpu
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --mem=96000
#SBATCH --time=2:30:00 # How long should they run
## This is all information for SLURM. It should all appear at the top of
## the script before your commands to run. SLURM understands lines 
## beginning with ## as a comment.

## Command(s) to run:

source ~/bin/anaconda3/bin/activate
conda activate biotools
# Make sure the environment with the software you need is activated.

cd /mnt/beegfs/gt156213e/
wgsim -N1000 -S1 genomes/NC_008253_1K.fna simulated_reads/sim_reads.fq /dev/null
bowtie2 -x indexes/e_coli -U simulated_reads/sim_reads.fq -S alignments/sim_reads_aligned.sam
samtools view -b -S -o alignments/sim_reads_aligned.bam alignments/sim_reads_aligned.sam
samtools view -c -f 4 alignments/sim_reads_aligned.bam
samtools view -q 42 -c alignments/sim_reads_aligned.bam
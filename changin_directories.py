#!/bin/python3

import re
import os
import shutil
import glob
import subprocess

my_file = open('/localdisk/home/s1962988/Assignment2/aves1/fasta/aves.fasta')
file_contents = my_file.read()


group_birds=[]
seq=[]
dict_birds={}

seq2=re.split('[>]', file_contents)

for line in seq2:
	group_birds.append(line)
	for group in group_birds:
		seq.append(group.split(sep="\n"))
		for group in seq:
			group[0]=re.sub(' ','_',group[0])
			dict_birds[group[0]]=''.join(group[1:])
			dict_birds={k: dict_birds[k] for k in dict_birds.keys()-{''}}

print(dict_birds)

if not os.path.isdir("/localdisk/home/s1962988/Assignment2/aves1/sequence_fasta/"):
	os.mkdir("/localdisk/home/s1962988/Assignment2/aves1/sequence_fasta/")

new_directory="/localdisk/home/s1962988/Assignment2/aves1/sequence_fasta/"

os.chdir("%s" %(new_directory))

for group,seq in dict_birds.items():
	output_file=open("%s.fasta" % group, "w")
	output_file.write(str(">" + group) + "\n" + str(seq))
	subprocess.call('patmatmotifs -sequence %s -outfile %s.patmatmotifs -auto' %(output_file, group), shell=True)

#if not os.path.isdir("/localdisk/home/s1962988/Assignment2/aves1/patmatmotifs/"):
#        os.mkdir("/localdisk/home/s1962988/Assignment2/aves1/patmatmotifs/")

#new_directory_2="/localdisk/home/s1962988/Assignment2/aves1/patmatmotifs/"

#fveor every_file in new_directory:
#	subprocess.call('patmatmotifs -sequence %s -outfile ' %(every_file), shell=True)


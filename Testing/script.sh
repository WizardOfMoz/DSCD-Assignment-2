#!/bin/bash

# Define an array of Python scripts to run
scripts=("child1.py" "child2.py")

# Define an array of input files to pass to each Python script
input_files=("input1.txt" "input2.txt")

# Loop through the scripts and input files
for i in "${!scripts[@]}"; do
  script="${scripts[$i]}"
  input_file="${input_files[$i]}"
  
  # Run the Python script in the background with the input file passed as standard input
  xterm -e "python $script < $input_file" &
done

# Wait for all background processes to finish
wait
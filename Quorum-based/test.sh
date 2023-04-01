N=5
Nw=3
Nf=3
python regserver.py $N $Nw $Nf &
sleep 1
for i in $(seq 1 $N); do
    python server.py $i &
    sleep 1
done
wait


#!/bin/bash

# Define an array of Python scripts to run
# scripts=("child1.py" "child2.py")

# # Define an array of input files to pass to each Python script
# input_files=("input1.txt" "input2.txt")

# # Loop through the scripts and input files
# for i in "${!scripts[@]}"; do
#   script="${scripts[$i]}"
#   input_file="${input_files[$i]}"
  
#   # Run the Python script in the background with the input file passed as standard input
#   xterm -e "python $script < $input_file" &
# done

# # Wait for all background processes to finish
# wait
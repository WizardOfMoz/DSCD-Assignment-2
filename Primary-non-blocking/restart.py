import shutil
import os
#remove all directories in data directory
if os.path.exists("data"):
    shutil.rmtree("data")
os.mkdir("data")
__author__ = "Francesco Mussati"
__version__ = "01.01 15/11/2022"

import os
from time import time
import logging
from sys import argv, path

import tensorflow as tf
import PIL

def gpu_set():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    for gpu in gpus: 
        tf.config.experimental.set_memory_growth(gpu, True)
    tf.config.list_physical_devices('GPU')

def main():
    gpu_set()

    os.chdir(path[0])
    for files in os.walk("../img"):
        for file in files[2]:
            logging.info(f"analized -> {file}")
            PIL.Image.open(str(f"../img/{file}"))
    return

if __name__ == "__main__":
    
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info("Start")
    start = time()

    main()

    end = time()
    logging.info(f"End {str(end - start)}")
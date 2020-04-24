import os
from multiprocessing import Pool

process={'uart_arduino.py','recognizer.py'}
def run_process(process):
    os.system('python3 {}'.format(process))

pool=Pool(processes=2)
pool.map(run_process,process)
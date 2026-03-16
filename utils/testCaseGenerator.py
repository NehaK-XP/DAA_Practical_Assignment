import random
from tqdm import tqdm
import os

STEP_SIZE = 50
START = 50
END = 2000

def increasingGenerator(element_count):     # generate element_count numbers in increasing order
    return list(range(1, element_count + 1))

def decreasingGenerator(element_count):     # generate element_count numbers in decreasing order
    return list(range(element_count, 0, -1))

def randomGenerator(element_count, seed=51):     # generate element_count numbers in random order
    arr = list(range(1, element_count + 1))
    random.seed(seed)
    random.shuffle(arr)
    return arr

def write_array(arr, filename):     # write array to file
    save_dir = 'testcases/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"Directory \'{save_dir}\' created")
    filename = os.path.join(save_dir, filename)
    with open(filename, "a") as file:
        file.write(f"{len(arr)}\n")
        for num in arr:
            file.write(f"{num}\n")

def read_array(filename):
    arrays = []
    try:
        with open(filename, "r") as file:
            while True:
                line = file.readline()
                if line == '':
                    break
                n = int(line.strip())
                arr = []
                for i in range(n):
                    arr.append(int(file.readline().strip()))
                arrays.append(arr)
    except FileNotFoundError:
        print(f"File ${file} not found\n")
    return arrays

def clear_datasets():
    for filename in ['ascending_dataset.txt', 'descending_dataset.txt', 'random_dataset.txt']:
        path = os.path.join('testcases/', filename)
        if os.path.exists(path):
            os.remove(path)


if __name__ == '__main__':
    clear_datasets()
    for element_count in tqdm(range(START, END + 1, STEP_SIZE), desc='Progress Bar'):

        arr = increasingGenerator(element_count)
        write_array(arr, 'ascending_dataset.txt')
        # write_array(arr, 'complete_dataset.txt')


        arr = decreasingGenerator(element_count)
        write_array(arr, 'descending_dataset.txt')
        # write_array(arr, 'complete_dataset.txt')
    

        for arr_num in range(5):
            arr = randomGenerator(element_count, seed=arr_num)
            write_array(arr, 'random_dataset.txt')
            # write_array(arr, 'complete_dataset.txt')

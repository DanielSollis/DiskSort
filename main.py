import sys
import os
from random import seed, randint
from time import time



def walking():
    start = time()
    i = 0
    for root, dirs, files in os.walk("C:/"):
        for f in files:
            if os.path.isfile(root + '/' + f):
                print f, os.path.getsize(root + '/' + f)
    print time() - start
    print i


def get_dirs(path, dirs_list):
    dir_size_list = [0, path]
    for f in os.listdir(path):
        new_path = path + '/' + f
        if os.path.isdir(new_path):
            try:
                dir_size_list[0] += get_dirs(new_path, dirs_list)
            except WindowsError:
                pass
        if os.path.isfile(new_path):
            dir_size_list[0] += os.path.getsize(new_path)
    ordered_insert(dirs_list, dir_size_list)
    return dir_size_list[0]



def ordered_insert(sorted_list, dir_list):
    val = dir_list[0]
    if not sorted_list:
        sorted_list.append(dir_list)
    elif sorted_list[len(sorted_list) - 1] <= val:
        sorted_list.append(dir_list)
    elif sorted_list[0] >= val:
        sorted_list.insert(0, dir_list)
    elif len(sorted_list) == 2:
        sorted_list.insert(1, dir_list)
    elif len(sorted_list) >= 3:
        binary_search(sorted_list, dir_list, 0, len(sorted_list))

def binary_search(sorted_list, dir_list, begin, end):
        val = dir_list[0]
        done = False
        while not done:
            mid = (end - begin) / 2 + begin
            if sorted_list[mid] <= val <= sorted_list[mid + 1]:
                sorted_list.insert(mid + 1, dir_list)
                done = True
            elif sorted_list[mid] > val:
                end = mid
            elif sorted_list[mid] < val:
                begin = mid


if __name__ == '__main__':
    dirs_list = []
    start = time()
    get_dirs("C:/", dirs_list)
    end = time()
    print end - start




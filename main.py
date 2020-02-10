import os
from time import time


def increment_readable_size(first_val, second_val):
    first_val = byte_size(first_val)
    second_val = byte_size( second_val)
    result_val = first_val + second_val
    return readable_size(result_val)


def readable_size(size):
    kb = 1024
    int_size = int(size)
    if int_size in range(0, kb):
        return str(size) + " B"
    elif kb  < int_size <= kb ** 2:
        return str(float(int_size)/kb) + " KB"
    elif kb ** 2 < int_size <= kb**3:
        return str(float(int_size) / kb ** 2) + " MB"
    elif kb**3 < int_size <= kb**4:
        return str(float(int_size) / kb ** 3) + " GB"
    elif kb ** 4 < int_size <= kb ** 5:
        return str(float(int_size) / kb ** 4) + " TB"
    return size


def byte_size(size):
    kb = 1024
    val, magnitude = size.split(" ")
    val = float(val)
    if magnitude == "B":
        return val
    elif magnitude == "KB":
        return val * kb
    elif magnitude == "MB":
        return val * kb ** 2
    elif magnitude == "GB":
        return val * kb ** 3
    elif magnitude == "TB":
        return val * kb ** 4


def get_dirs(path, dirs_list):
    print path
    dir_size_list = [0, path]
    for f in os.listdir(path):
        new_path = path + '/' + f
        if os.path.isdir(new_path):
            try:
                dir_size_list[0] +=get_dirs(new_path, dirs_list)
            except WindowsError:
                pass
        if os.path.isfile(new_path):
            dir_size_list[0] += os.path.getsize(new_path)
    if dir_size_list[0] != 0:
        ordered_insert(dirs_list, dir_size_list)
    return dir_size_list[0]


def ordered_insert(sorted_list, dir_list):
    val = dir_list[0]
    if not sorted_list:
        sorted_list.append(dir_list)
    elif sorted_list[len(sorted_list) - 1][0] >= val:
        sorted_list.append(dir_list)
    elif sorted_list[0][0] <= val:
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
            if sorted_list[mid][0] >= val >= sorted_list[mid + 1][0]:
                sorted_list.insert(mid + 1, dir_list)
                done = True
            elif sorted_list[mid][0] < val:
                end = mid
            elif sorted_list[mid][0] > val:
                begin = mid


if __name__ == '__main__':
    dirs = []
    start = time()
    get_dirs("E:/", dirs)
    print time() - start
    print "foo"

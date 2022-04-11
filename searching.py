import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]



def linear_search(sequence,number):
    search_res = {"positions":[], " count":0}
    for i, value in enumerate(sequence):
        if number == value:
            search_res["positions"].append(i)
            search_res[" count"] = search_res[" count"] + 1
    return search_res


"""
def pattern_search(sequence, pattern):
    positions = set()
    i = 0
    while i < len(sequence) - len(pattern):
        for letter in sequence[i:i + len(pattern)]:
            if letter != pattern[i]:
                break
            else:
                i = i + 1
        if i == len(pattern):
            positions.add(i)
        i = i + 1
    return positions
"""


def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1
    while left < right:
        middle = (left + right) // 2
        if sequence[middle] == number:
            return middle
        elif sequence[middle] < number:
            left = middle + 1
        elif sequence[middle] > number:
            right = middle - 1
    return None



    """
    search_res = {"positions": []}
    for i, value in enumerate(sequence):
        if number == value:
            search_res["positions"].append(i)
    return search_res
    """




def main():
    sequential_data = read_data("sequential.json","unordered_numbers")
    dna_data = read_data("sequential.json", "dna_sequence")
    ordered_numbers = read_data("sequential.json", "ordered_numbers")
    print(sequential_data)
    print(dna_data)
    print(ordered_numbers)

    results = linear_search(sequential_data, 0)
    print(results)

    #dna_results = pattern_search(dna_data,"ATA")
   # print(dna_results)

    result = binary_search(ordered_numbers, 14)
    print(result)




if __name__ == '__main__':
    main()
# Binary Search
def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Linear Search
def linear_search(data, target):
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1


# Hash Table
def create_hash_table(data):
    hash_table = {}
    for i, item in enumerate(data):
        hash_table[item] = i
    return hash_table

def hash_table_search(hash_table, target):
    return hash_table.get(target, -1)




# Load data from the file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

file_path = 'usernames.txt'
data = load_data(file_path)
print(f"Loaded {len(data)} usernames from the database.")

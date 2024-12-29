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


# Binary Search Tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_balanced_bst(data):
    if not data:
        return None
    mid = len(data) // 2
    root = TreeNode(data[mid])
    root.left = build_balanced_bst(data[:mid])
    root.right = build_balanced_bst(data[mid+1:])
    return root

def search_tree(root, target):
    if root is None or root.key == target:
        return root
    if target < root.key:
        return search_tree(root.left, target)
    return search_tree(root.right, target)


# Bloom Filter
class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            index = self.hash(item, i)
            self.bit_array[index] = 1

    def check(self, item):
        for i in range(self.hash_count):
            index = self.hash(item, i)
            if self.bit_array[index] == 0:
                return False
        return True

    def hash(self, item, seed):
        return int(sha256((str(item) + str(seed)).encode()).hexdigest(), 16) % self.size



# Load data from the file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

file_path = 'usernames.txt'
data = load_data(file_path)
print(f"Loaded {len(data)} usernames from the database.")

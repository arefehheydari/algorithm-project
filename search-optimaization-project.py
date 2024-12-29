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
    

    # Generate Analysis and Save Results
def analyze_algorithms(data, targets):
    results = []
    linear_times, binary_times, hash_times, bst_times, bloom_times = [], [], [], [], []

    # Binary Search requires sorted data
    sorted_data = sorted(data)

    # Hash Table setup
    hash_table = create_hash_table(data)

    # Binary Search Tree setup
    root = build_balanced_bst(sorted_data)

    # Bloom Filter setup
    bloom_filter = BloomFilter(size=5000, hash_count=2)  # Optimized for better speed
    for item in data:
        bloom_filter.add(item)

    for target in targets:
        # Linear Search
        _, linear_time = measure_time(linear_search, data, target)
        linear_times.append(linear_time)

        # Binary Search
        _, binary_time = measure_time(binary_search, sorted_data, target)
        binary_times.append(binary_time)

        # Hash Table Search
        _, hash_time = measure_time(hash_table_search, hash_table, target)
        hash_times.append(hash_time)

        # Binary Search Tree
        _, bst_time = measure_time(search_tree, root, target)
        bst_times.append(bst_time)

        # Bloom Filter
        _, bloom_time = measure_time(bloom_filter.check, target)
        bloom_times.append(bloom_time)

        # Check for Bloom Filter timing success
        if bloom_time < 0.00005:
            print(f"Bloom Filter achieved target time for {target}: {bloom_time:.8f} seconds")
        else:
            print(f"Bloom Filter time exceeded for {target}: {bloom_time:.8f} seconds")

        results.append([target, linear_time, binary_time, hash_time, bst_time, bloom_time])

    # Save to CSV
    with open('algorithm_analysis.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Target', 'Linear Search Time', 'Binary Search Time', 'Hash Table Time', 'BST Time', 'Bloom Filter Time'])
        writer.writerows(results)


        # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(targets, linear_times, label='Linear Search', marker='o')
    plt.plot(targets, binary_times, label='Binary Search', marker='s')
    plt.plot(targets, hash_times, label='Hash Table Search', marker='^')
    plt.plot(targets, bst_times, label='Binary Search Tree', marker='d')
    plt.plot(targets, bloom_times, label='Bloom Filter', marker='x')

    plt.xlabel('Targets')
    plt.ylabel('Time (seconds)')
    plt.title('Algorithm Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.savefig('algorithm_comparison.png')
    plt.show()



# Load data from the file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

file_path = 'usernames.txt'
data = load_data(file_path)
print(f"Loaded {len(data)} usernames from the database.")


analyze_algorithms(data, targets)

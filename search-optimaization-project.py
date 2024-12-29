# Load data from the file
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

file_path = 'usernames.txt'
data = load_data(file_path)
print(f"Loaded {len(data)} usernames from the database.")

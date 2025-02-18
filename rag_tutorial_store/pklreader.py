import pickle

# Replace 'path_to_your_file.pkl' with the actual path to your PKL file
file_path = './nodes.pkl'

# Open the file in binary mode and load the data
try:
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except pickle.UnpicklingError:
    print("Error: The file content is not a valid pickle format.")
except EOFError:
    print("Error: The file is incomplete or corrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Now 'data' contains the deserialized Python object
print(data)

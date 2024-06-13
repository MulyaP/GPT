import datasets
from tqdm import tqdm

# Load the dataset
dataset = datasets.load_dataset('openwebtext/openwebtext.py', split='train')

# Print some examples
# for example in dataset.take(5):
#     print(example)


unique_characters = set()

# Define a batch size
batch_size = 1000

# Process the dataset in batches with tqdm progress bar
for i in tqdm(range(0, len(dataset)), desc="Processing Batches"):
    text = dataset[i]['text']
    unique_characters.update(text)

# Convert the set to a sorted list
sorted_characters = sorted(unique_characters)

# Print the sorted list of unique characters
# print("Number of unique characters:", len(sorted_characters))
# print("Unique characters:", sorted_characters)

vocab_file_path = 'openwebtext/character_vocab.txt'
with open(vocab_file_path, 'w', encoding='utf-8') as vocab_file:
    for char in sorted_characters:
        vocab_file.write(char + '\n')

split_dataset = dataset.train_test_split(test_size=0.1)
train_dataset = split_dataset['train']
val_dataset = split_dataset['test']

def write_dataset_to_file(dataset, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for example in tqdm(dataset, desc=f"Writing to {file_path}", total=len(dataset)):
            text = example['text']
            file.write(text + '\n')

# Define file paths
train_file_path = 'openwebtext/train.txt'
val_file_path = 'openwebtext/val.txt'

# Write the datasets to files
write_dataset_to_file(train_dataset, train_file_path)
write_dataset_to_file(val_dataset, val_file_path)

print(f"Training data written to: {train_file_path}")
print(f"Validation data written to: {val_file_path}")

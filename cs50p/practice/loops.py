# Loop through a list of items
files = ["document.txt", "image.jpg", "data.csv"]

for file in files:
    print(f"Processing: {file}")

# Output:
# Processing: document.txt
# Processing: image.jpg
# Processing: data.csv

# Range function - generate numbers
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Count: {i}")

# Loop with index
for index, file in enumerate(files):
    print(f"{index}: {file}")

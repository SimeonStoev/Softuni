file_path = input().split("\\")
file_name = file_path[-1]
file_data = file_name.split(".")

print(f"File name: {file_data[0]}")
print(f"File extension: {file_data[1]}")

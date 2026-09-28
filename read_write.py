# to read file
file_path = r"C:\Users\Admin\PycharmProjects\PythonProject3\input.txt"

with open(file_path, "r") as file:
    data = file.read()

print(data)

#
file_path = r"C:\Users\Admin\PycharmProjects\PythonProject3\input.txt"
output_path = r"C:\Users\Admin\PycharmProjects\PythonProject3\output.txt"

with open(file_path, "r") as file:
    data = file.read()

with open(output_path, "w") as file:
    file.write(data)

print("File copied successfully!")
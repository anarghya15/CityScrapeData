import os
import pandas as pd

# Main directory containing subfolders
#main_directory = r"D:\\IIIT\\AI705 - RS\\City Images"
main_directory = r"/media/dell/New Volume/IIIT/AI705 - RS/City Images"

# Load the Excel file
excel_file_path = "/home/dell/Downloads/all_city_data.xlsx"
df = pd.read_excel(excel_file_path)

# Extract city names from the 'city' column
city_names = df['city'].tolist()

# Check if a folder with the same name as each city exists
i=0
for city in city_names:
    city_folder_path = os.path.join(main_directory, city)
    if os.path.isdir(city_folder_path):
        #print(f"Folder '{city}' exists at: {city_folder_path}")
        i += 1
    else:
        print(f"Folder '{city}' does not exist in the main directory.")


# Iterate over each subfolder in the main directory
for root, dirs, files in os.walk(main_directory):
    num_files = len(files)
    if num_files < 5:
        print(f"Folder '{root}' has less than 5 files: {num_files} files")
    for file in files:
        if file.endswith('.avif'):
            file_path = os.path.join(root, file)
            print(f"File '{file}' found at: {file_path}")
        file_path = os.path.join(root, file)
        if '&' in file:
            # Replace '&' with 'and' in the file name
            new_file_name = file.replace('&', 'and')
            # Rename the file
            os.rename(file_path, os.path.join(root, new_file_name))
            print(f"Renamed '{file}' to '{new_file_name}' in '{root}'.")

print("All files processed successfully.")
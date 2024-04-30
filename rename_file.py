import os

# Main directory containing subfolders
main_directory = r"D:\\IIIT\\AI705 - RS\\City Images"

# Iterate over each subfolder in the main directory
for root, dirs, files in os.walk(main_directory):
    for file in files:
        file_path = os.path.join(root, file)
        if '&' in file:
            # Replace '&' with 'and' in the file name
            new_file_name = file.replace('&', 'and')
            # Rename the file
            os.rename(file_path, os.path.join(root, new_file_name))
            print(f"Renamed '{file}' to '{new_file_name}' in '{root}'.")
        else:
            print(f"No '&' found in '{file}' in '{root}', skipping renaming.")

print("All files processed successfully.")
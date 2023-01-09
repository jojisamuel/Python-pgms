import pathlib

# Set the root directory where the files are located
root_dir = pathlib.Path('./source-files')

# Create a dictionary mapping file extensions to folder names
ext_to_folder = {
    '.txt': 'Text Files',
    '.docx': 'Word Files',
    '.doc': 'Word Files',
    '.pdf': 'PDFs',
    '.png': 'Images',
    '.jpg': 'Images',
    '.jpeg': 'Images'
}

# Iterate through all the files in the root directory
for file in root_dir.iterdir():
    # Get the file extension
    ext = file.suffix.lower()
    # If the file extension is in the dictionary, move the file to the corresponding folder
    if ext in ext_to_folder:
        folder_name = ext_to_folder[ext]
        folder_path = root_dir / folder_name
        # Create the folder if it doesn't already exist
        folder_path.mkdir(exist_ok=True)
        # Move the file to the folder
        print(folder_path)
        file.rename(folder_path / file.name)
import os

def rename_images(directory, base_name):
    # List all files in the directory
    files = sorted(os.listdir(directory))
    
    # Counter to append to the base name
    counter = 1
    
    # Loop through each file in the directory
    for file in files:
        # Get the file extension
        file_ext = os.path.splitext(file)[1]
        
        # Only process files that are images (you can add more extensions here)
        if file_ext.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']:
            # Create the new filename
            new_name = f"{base_name}-{counter:02d}{file_ext}"
            
            # Build the full paths
            old_file_path = os.path.join(directory, file)
            new_file_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            
            print(f"Renamed: {file} -> {new_name}")
            
            # Increment the counter
            counter += 1

if __name__ == "__main__":
    # Get the directory and base name from the user
    directory = input("Enter the path to the directory containing the images: ")
    base_name = input("Enter the base name for the images (e.g., img): ")
    
    # Rename the images
    rename_images(directory, base_name)

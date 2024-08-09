import os
import shutil
from collections import defaultdict

def rename_and_copy_frames(input_folder, output_folder, video_name, video_date, sample_rate=25):
    """
    Renames and copies extracted frames to a new folder with the specified format.
    
    :param input_folder: Folder containing the original extracted frames
    :param output_folder: Folder to save the renamed frames
    :param video_name: Original name of the video file (without extension)
    :param video_date: Date of the video in the format "DD-MM-YY"
    :param sample_rate: Frame capture rate (frames per second)
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all files in the input folder
    files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

    # Dictionary to track how many images per frame time
    frame_count_dict = defaultdict(int)
    
    # Count the number of images per frame time
    for file_name in files:
        frame_time_str = file_name.split('_')[-1].replace('.png', '')
        frame_count_dict[frame_time_str] += 1

    # Iterate over each file in the input folder
    for file_name in sorted(files):
        # Extract the frame time from the original file name
        frame_time_str = file_name.split('_')[-1].replace('.png', '')
        frame_time = float(frame_time_str)
        
        # Calculate the frame number
        frame_number = int(frame_time * sample_rate)
        
        # Create the new file name
        new_file_name = f"{video_date}_video1_{video_name}_{frame_number}.png"
        
        # Define the full paths for the input and output files
        original_file_path = os.path.join(input_folder, file_name)
        new_file_path = os.path.join(output_folder, new_file_name)
        
        # Copy the file to the new location with the new name
        shutil.copy2(original_file_path, new_file_path)
    
    print(f"Renamed and copied {len(files)} frames to {output_folder}")

if __name__ == "__main__":
    # Parameters
    input_folder = "extracted_data/frames/"
    output_folder = "extracted_data/frames/"
    video_name = "00000000205000400"
    video_date = "01-08-24"
    sample_rate = 25  # Frames per second

    # Execute the renaming and copying process
    rename_and_copy_frames(input_folder, output_folder, video_name, video_date, sample_rate)

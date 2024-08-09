import cv2
import os
import numpy as np
import time
from tqdm.notebook import tqdm

def extract_frames(video_path, output_folder, video_date, video_index, sample_rate=1, start_time=0, end_time=None, max_frames=None):
    """
    Extract frames from a specified interval of a video file with detailed progress tracking.
    Frames are saved as PNG files in the specified format.
    
    :param video_path: Path to the input video file
    :param output_folder: Base folder to save extracted frames
    :param video_date: Date of the video in the format "DD-MM-YY"
    :param video_index: Index of the video (e.g., 1, 2, 3...)
    :param sample_rate: Extract every nth frame (e.g., 1 = every frame, 2 = every other frame)
    :param start_time: Start time in seconds to begin extraction (default: 0)
    :param end_time: End time in seconds to stop extraction (default: None, meaning end of video)
    :param max_frames: Maximum number of frames to extract (None for all frames in the interval)
    :return: List of paths to saved frames
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    video = cv2.VideoCapture(video_path)
    
    fps = int(video.get(cv2.CAP_PROP_FPS))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    total_duration = total_frames / fps
    
    # Set video to start_time
    video.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)
    start_frame = int(video.get(cv2.CAP_PROP_POS_FRAMES))
    
    # Calculate end frame
    end_frame = total_frames if end_time is None else min(int(end_time * fps), total_frames)
    
    frames_to_process = end_frame - start_frame
    duration = frames_to_process / fps
    
    print(f"Video FPS: {fps}")
    print(f"Total video duration: {total_duration:.2f} seconds")
    print(f"Processing from {start_time:.2f}s to {end_time:.2f}s" if end_time else f"Processing from {start_time:.2f}s to end")
    print(f"Interval duration: {duration:.2f} seconds")
    print(f"Frames to process: {frames_to_process}")
    print(f"Extracting every {sample_rate} frame(s)")
    print(f"Saving frames to: {output_folder}")
    
    effective_fps = fps / sample_rate
    print(f"Effective frame rate: {effective_fps:.2f} FPS")
    
    frame_count = 0
    saved_count = 0
    saved_frames = []
    
    # Adjust max_frames if set
    if max_frames:
        frames_to_process = min(frames_to_process, max_frames * sample_rate)
    
    start_time_processing = time.time()
    
    # Get the video name without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    crop_count = 1  # Start crop count at 1
    with tqdm(total=frames_to_process, unit='frame', desc="Extracting frames") as pbar:
        while frame_count < frames_to_process:
            ret, frame = video.read()
            if not ret:
                break
            
            if frame_count % sample_rate == 0:
                # Calculate the time of this frame
                frame_time = start_time + (frame_count / fps)
                
                # Calculate the frame number
                frame_number = int(frame_time * fps)
                
                # Generate filename in the requested format
                frame_filename = os.path.join(output_folder, f"{video_date}_video{video_index}_{video_name}_{frame_number}_{crop_count}.png")
                
                # Use cv2.imwrite with PNG compression
                cv2.imwrite(frame_filename, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])
                saved_frames.append(frame_filename)
                saved_count += 1
                
                crop_count += 1  # Increment crop count after saving each frame
                
                if max_frames and saved_count >= max_frames:
                    break
            
            frame_count += 1
            pbar.update(1)
            
            # Update estimated time
            elapsed_time = time.time() - start_time_processing
            estimated_total_time = (elapsed_time / frame_count) * frames_to_process
            estimated_remaining_time = estimated_total_time - elapsed_time
            
            pbar.set_postfix({
                'Saved': saved_count,
                'Elapsed': f'{elapsed_time:.2f}s',
                'Remaining': f'{estimated_remaining_time:.2f}s'
            })
    
    video.release()
    print(f"\nExtracted {saved_count} frames to {output_folder}")
    print(f"Total time: {time.time() - start_time_processing:.2f} seconds")
    return saved_frames

if __name__ == "__main__":
    # Example usage
    video_path = r"C:\Users\2dgod\Downloads\00000000205000400.mp4"
    output_folder = "extracted_data"
    video_date = "01-08-24"
    video_index = 1
    sample_rate = 15  # Extract 2 frames per second for a 30 fps video
    start_time = 0
    end_time = None
    max_frames = None

    saved_frames = extract_frames(video_path, output_folder, video_date, video_index, sample_rate, start_time, end_time, max_frames)
import multiprocessing
from moviepy.editor import VideoFileClip

# Change to your own large file path
# For Mac OS: the Mobile Hard Drive(MHD) path starts with /Volumes/...
# For Windows OS: the MHD path start with drive letter "D:/"" or "E:/" ...
VIDEO_PATH = "/Volumes/<MobileHardDrivePath>/<LargeFileName>.mp4"

# Save directory for clipped files 
SAVE_DIR = "/Volumes/<MobileHardDrivePath>/clips/"  


# Read large video file
video = VideoFileClip(VIDEO_PATH)

# Define a function to cut video clips and save
def cut_video(start, end, filename):
    
    # Cut the video clips
    clip = video.subclip(start, end)
    # Save the video clips
    clip.write_videofile(SAVE_DIR + filename, codec='libx264', audio_codec='aac')



# Create a list to store the cutting parameters and file names
tasks = []

# Calculate the total duration and number of segments, assuming 10 minutes per segment, in seconds
total_duration = video.duration
segment_duration = 10 * 60
segment_count = int(total_duration / segment_duration) + 1

# Loop to generate the parameters and file names for each segment and add to the list
for i in range(segment_count):
    # Calculate the start time and end time for each segment
    start = i * segment_duration
    end = min((i + 1) * segment_duration, total_duration)
    # Generate the file name for each segment, in the format of "video_<number>.mp4" 
    filename = f"video_{i + 1}.mp4"
    # Form tuples with the parameters and file names and add to the list
    tasks.append((start, end, filename))

if __name__ == '__main__':
    # Create a process pool, with the number of processes as a parameter. 
    # Adjust based on your computer performance and number of tasks.
    pool = multiprocessing.Pool(8)
    # Use the map method of the process pool to pass in the function and 
    # list of parameters, to automatically assign tasks to processes for execution. 
    pool.starmap(cut_video, tasks)

    # Close the process pool and wait for all processes to complete their tasks. 
    pool.close()
    pool.join()


import os 
import subprocess
from multiprocessing import Pool

# 1. Obtain video information and calculate the number of segments needed, the process is the same as above.
# 2. Define a split_video function to execute a single video splitting task.
# 3. Use Pool to create 8 processes, and use p.map to assign n_segments video splitting tasks to 8 processes for execution.
# 4. Wait for all processes to complete execution, then the video will be split into n_segments segments.

# Change to your own large file path
# For Mac OS: the Mobile Hard Drive(MHD) path starts with /Volumes/...
# For Windows OS: the MHD path start with drive letter "D:/"" or "E:/" ...
VIDEO_PATH = "/Volumes/<MobileHardDrivePath>/<LargeFileName>.mp4"

video_info = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of',  
                             'default=noprint_wrappers=1:nokey=1', VIDEO_PATH], 
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
duration = float(video_info.stdout)
n_segments = int(duration / 600)
def split_video(i):
    if i < n_segments - 1:  
        start_time = i * 600
        end_time = (i + 1) * 600
    else:  
        start_time = i * 600
        end_time = duration  
    output_file = f'{VIDEO_PATH.rsplit(".")[0]}_{i + 1}.mp4'
    command = ['ffmpeg', '-i', VIDEO_PATH, '-ss', str(start_time), '-t', str(end_time - start_time), 
               '-c', 'copy', output_file]
    subprocess.run(command)


if __name__ == '__main__':
    //You can change the concurrent process number. 3-8 recommended.
    p = Pool(8)
    p.map(split_video, range(n_segments))


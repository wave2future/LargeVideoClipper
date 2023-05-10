# LargeVideoClipper

Large Video Clipper

**Method 1：**
LargeVideoClipper1.py

Install ffmpeg and ffprobe. You can follow these steps:

- Download ffmpeg: You can download it from https://ffmpeg.org/download.html, choose the Mac OSX version
- Unzip the downloaded file, and run in the terminal:
  
  ```
  # bash
  sudo mv ffmpeg /usr/local/bin 
  sudo mv ffprobe /usr/local/bin
  ```
- Then you can call ffmpeg and ffprobe in Python. 

I have experimented with cutting a 2G video file, which took 2-3 minutes.

**方法一：**
LargeVideoClipper1.py

安装ffmpeg和ffprobe。可以按照以下步骤进行:

- 下载ffmpeg:可以从https://ffmpeg.org/download.html下载,选择Mac OSX版本
- 解压下载的文件,在终端运行:
  
  ```
  # bash
  sudo mv ffmpeg /usr/local/bin
  sudo mv ffprobe /usr/local/bin
  ```
- 然后就可以在Python中调用ffmpeg和ffprobe了

实验了下切割2G左右的视频文件，用时2-3分钟。

---

**Method 2：**
LargeVideoClipper2.py
Use the MoviePy video processing library instead of ffmpeg and ffprobe. 
I have experimented with method two to cut a 1.5G video file, which took about 20 minutes.
```
# bash
pip install moviepy
```

**方法二：**
LargeVideoClipper2.py

使用视频处理库MoviePy代替ffmpeg和ffprobe。
实验了用方法二下切割1.5G左右的视频文件，用时20分钟。

```
# bash
pip install moviepy
```
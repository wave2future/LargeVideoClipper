# LargeVideoClipper

Large Video Clipper



The original intention of the tool:

A friend of mine got a 90G video file in a mobile hard drive that needs to be edited. Due to the large file size, most general purpose computers cannot edit it. The large file needs to be cut into smaller video files.
With the help of Anthropic's **Claude**, two methods were used to achieve the function of cutting large video files.
Please modify the path of the video file yourself; the code tentatively cuts the video into 10-minute segments.



**Method 1：**
**LargeVideoClipper1.py**

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



**Method 2：**
**LargeVideoClipper2.py**

Use the MoviePy video processing library instead of ffmpeg and ffprobe. 
I have experimented with method two to cut a 1.5G video file, which took about 20 minutes.

```
# bash
pip install moviepy
```

---

分割大视频文件工具



工具制作初衷：
一个朋友有一个存在移动硬盘中的90G左右的视频文件需要剪辑，由于文件太大，一般配置的电脑都剪辑不了。需要将大文件剪辑成小的视频文件。
借助Anthropic的**Claude**的帮助，用了两种方法来实现切割大视频文件的功能。
视频文件的路径请自行修改；代码中暂定切割成10分钟一段视频。



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

- 然后就可以在Python中调用ffmpeg和ffprobe了。

- 

实验了下切割2G左右的视频文件，用时2-3分钟。





**方法二：**
LargeVideoClipper2.py

使用视频处理库MoviePy代替ffmpeg和ffprobe。


实验了用方法二下切割1.5G左右的视频文件，用时20分钟左右。

```
# bash
pip install moviepy
```

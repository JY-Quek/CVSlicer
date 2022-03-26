CV Slicer - Python3 Package
=================
<a href="https://pypi.org/project/cvslicer/"><img src="https://badge.fury.io/py/cvslicer@2x.png" alt="PyPI version" height="18"></a><br>

Handling the slicing of enormously large image without compromising quality or information. Specially made for computer vision object detection.

Usage
--------
#### To install this package:
*Online Method*
- Run:
```shell
pip install cvslicer
```

*Offline Method*
- Clone this repo -or- Download the zipped file and extract.
- Change your directory into the downloaded folder/repo.
- Run:
```shell
pip install .
```
<br><hr><br>
#### To import:
```shell
import cvslicer
```

#### To use:
- We need to have 2 parameters ( in pixels ), 
1) The maximum size of image after sliced.
2) The maximum size of object for detection.

```python
# 100, 100: Image CutOff Height and Width
# 40, 40: Object Maximum Height and Width
img_slicer = cvslicer.CVSlicer(img_path, 100, 100, 40, 40)  

# Below function gives you a 2D array with the below elements 
# [ image file path, [x-coordinate to shift, y-coordinate to shift]  ]
print(img_slicer.slice_img()) 
```

*You may refer the folder <a href="sample/">"sample/"</a> for sample usage.*
*Note: To run sample, please install the extra dependencies by running "pip install cvslicer[extra]"*

Overview
--------
<br>
<p align="center">
  <img height="300px" align="middle" src="doc/image/Logo CVSlicer Transparent.png"/>
</p>
<br>
Say, you have extremely large dimension images like floor plans, maps, building layout, etc. You want to use them with your object detection model. Sometimes, it might have some compatibility issues with some models or some programs might not be taking images in such an enormous dimension.
<br><br>
There are some workarounds, ie. <br>
(1) Downsize the image dimension by losing quality.
<br>
(2) Crop/Slice the image into smaller pieces.
<br><br>
Both the above methods will cause you to lose information. Particularly for (2), if your object gets sliced in half within the borders of cropped image, it will not be detected.

Thus, here comes the purpose of CV Slicer. It is a Python-3 package which is made to handle the issues mentioned in (1) and (2) above. It is made to be compatible with OpenCV.

On the other hand, CV Slicer may also help those who wish to load large image in OpenCV. OpenCV limits the size of image up to a certain constant ( you may refer here: https://github.com/opencv/opencv/blob/8eba3c1e7e8975ff1d263a41a5753efaa51d54fc/modules/imgcodecs/src/loadsave.cpp#L61). 

To bypass that limit, you have to apply some hacks by changing the environment variable (for newer version only) or by redefining the constants and recompile the whole OpenCV package again. But if you wish to avoid or are unable to do that, you may use CV Slicer too. 


Concepts
--------

In brief, if we are to sliced the image below into smaller pieces, we are going to slice it into 9 smaller pieces. The 4 pieces are the main pieces. While for the 5th - 9th pieces, they are strips above the borders, their width and height are determined by the size of the object that you are detecting. Those strips are to prevent the case where your object gets sliced in half within the borders of the first 4 pieces that we sliced.

For more details please refer <a href="doc/INDEX.MD">*"doc/INDEX.MD"*</a>
<br><br><br>
<p align="center">
  <img height="300px" align="middle" src="doc/image/slicing-steps.gif"/>
</p>
<br><br><br><hr>

License
--------

MIT License

Author
------
Quek JY
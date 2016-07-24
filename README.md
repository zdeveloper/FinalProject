# Snapchat like Glasses Filter

This is a Snapchat like Glasses Filter that was developed using OpenCV and Python as a final project for the Georgia Tech CS-6475 final project. The project is broken in to two main files.
  - ```Video.py``` This file contains capture code the gets live frame from webcam and displays it after applying the enhance glasses additions.
  - ```Enhance.py``` This file contains glasses filter addition code that runs face eye detection to determine glasses size and location and then it merges it with the original image.

### Installation
```sh
 python video.py
```

### Tech

Dillinger uses a number of open source projects to work properly:

* [OpenCV] - a library of programming functions mainly aimed at real-time computer vision,
* [Python] - a widely used high-level, general-purpose, interpreted, dynamic programming language.
* [NumPy] -  an extension to the Python programming language, adding multi-dimensional arrays and matrices.
* [Scipy] - an open source Python library used by scientists, analysts, and engineers doing scientific computing and technical computing.

### Examples
|Input| Output|
| ------------- |:-------------:|
| ![Input](https://c7.staticflickr.com/8/7310/28240905910_2346f6dbeb_o.jpg)| ![Output](https://c5.staticflickr.com/9/8880/28240899820_91c3b695ce_o.jpg) |


### Todos

 - Write Tests
 - Rethink Github Save
 - Add Code Comments
 - Add Night Mode


### Version
3.2.7

License
----
MIT


   [OpenCV]: <http://opencv.org>
   [Python]: <https://www.python.org>
   [NumPy]: <http://www.numpy.org>
   [Scipy]: <https://www.scipy.org>

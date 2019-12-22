# Face Anonymizer
This repostory contains code to hide a face from images, Videos. It uses HaarCascade for face detection, which is a basic face detection mechanism, and with some image processing operations it replace the face with a mask.

#### Author: [Ravin Kumar](https://mr-ravin.github.io)

### Modes of utility:
- Images to Masked Images
```
import facemask
facemask.image_mask("inputfile_name.jpg","outputfile_name.jpg","maskfile_used.jpg")
```
- Videos to Masked Videos
```
import facemask
facemask.video_mask("inputfile.avi","outputfile.avi","maskfile_used.jpg")
```
- Live Camera to Masked Video.
```
import facemask
facemask.camera_mask(1,0,"outputfile.avi","maskfile_used.jpg") # 1 represents 1 minutes, 0 represents camera no. 0
```
### Sample Output for Videos: 
[![Working Demonstration](https://github.com/mr-ravin/Face-Anonymizer/blob/master/camvid.gif)](https://youtu.be/S0JjZsSSq6w)



### Sample Output for Images:
- Original Image:

[![Working Demonstration](https://github.com/mr-ravin/Face-Anonymizer/blob/master/original.jpg)](https://github.com/mr-ravin/facemask/blob/master/original.jpg)

- Mask Image Used:

[![Working Demonstration](https://github.com/mr-ravin/Face-Anonymizer/blob/master/mask.jpg)](https://github.com/mr-ravin/facemask/blob/master/mask.jpg)

- Output Masked Image:

[![Working Demonstration](https://github.com/mr-ravin/Face-Anonymizer/blob/master/maskedoutput.jpg)](https://github.com/mr-ravin/facemask/blob/master/maskedoutput.jpg)

### Important: In videos it skip some frames for applying mask. And while processing Videos, it loss audio sound of Video.

```python
Copyright (c) 2018 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

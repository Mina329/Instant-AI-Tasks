# Session : 22/10/2023

## 5 Python libraries for computer vision

1. OpenCV
2. Pillow
3. Scikit-Image
4. Dlib
5. TensorFlow and Keras
6. PyTorch
7. SimpleCV
8. Mahotas
9. Imutils
10. Face Recognition

## All image extensions OpenCV can read

- Windows bitmaps - _.bmp, _.dib
- JPEG files - _.jpeg, _.jpg, \*.jpe
- JPEG 2000 files - \*.jp2
- Portable Network Graphics - \*.png
- WebP - \*.webp
- AVIF - \*.avif
- Portable image format - _.pbm, _.pgm, _.ppm _.pxm, \*.pnm
- PFM files - \*.pfm
- Sun rasters - _.sr, _.ras
- TIFF files - _.tiff, _.tif
- OpenEXR Image files - \*.exr
- Radiance HDR - _.hdr, _.pic
- Raster and Vector geospatial data supported by GDAL

## What is Active contour module ?

The Active Contour Model, also known as the Snakes model, is a computer vision and image processing technique used for contour detection and object boundary delineation in images. It was introduced by Michael Kass, Andrew Witkin, and Demetri Terzopoulos in 1987. Active Contour Models are particularly useful in tasks such as image segmentation, object tracking, and shape analysis.

Active Contour Models are particularly effective in scenarios where traditional edge detection or thresholding methods may fail. They can adapt to the object's shape, handle noise, and concavities, and are widely used in medical image analysis, object tracking, and image segmentation tasks. However, they require careful parameter tuning, and their performance can be sensitive to initialization and noise in the image.

## What is Image dailation and eroding?

`Dilation` makes things bigger in an image. In a black-and-white image, it expands white areas.

`Erosion` makes things smaller in an image. In a black-and-white image, it shrinks white areas.

## How to read video (image and sound) stored video or realtime?

[Code](read_video.ipynb)

## types of filters and when to use each

1. `Low-Pass Filter`:

- `Purpose`: Allows low-frequency components to pass while attenuating high-frequency components.
- `Use Case`: Smoothing or noise reduction in signals or images.

2. `High-Pass Filter`:

- `Purpose`: Allows high-frequency components to pass while attenuating low-frequency components.
- `Use Case`: Edge detection in images, noise reduction in audio.

3. `Band-Pass Filter`:

- `Purpose`: Allows a specific range of frequencies to pass while attenuating frequencies outside that range.
- `Use Case`: Filtering specific frequency components in signals or images.

4. `Band-Stop Filter (Notch Filter)`:

- `Purpose`: Attenuates a specific range of frequencies while allowing frequencies outside that range to pass.
- `Use Case`: Removing interference frequencies from signals, such as power line noise.

5. `Gaussian Filter`:

- `Purpose`: Smooths and blurs an image by applying a Gaussian function.
- `Use Case`: Image blurring for noise reduction or to create artistic effects.

6. `Median Filter`:

- `Purpose`: Replaces each pixel's value with the median value in its neighborhood.
- `Use Case`: Removing salt-and-pepper noise in images.

7. `Mean Filter (Box Filter)`:

- `Purpose`: Replaces each pixel's value with the average value in its neighborhood.
- `Use Case`: Smoothing or noise reduction in images.

8.  `Sobel Filter`:

- `Purpose`: Detects edges in images by calculating the gradient.
- `Use Case`: Edge detection in computer vision applications.

9. `Kalman Filter`:

- `Purpose`: Estimates the state of a dynamic system with noisy measurements over time.
- `Use Case`: Predictive tracking in robotics, aerospace, and control systems.

10. `Butterworth Filter`:

- `Purpose`: A type of analog filter that provides a relatively flat frequency response in the passband.

- `Use Case`: Analog filter design in electronics.

11. `FIR Filter (Finite Impulse Response)`:

- `Purpose`: Filters data based on the weighted sum of past input samples.
- `Use Case`: Digital signal processing, noise reduction, and audio processing.

12. `IIR Filter (Infinite Impulse Response)`:

- `Purpose`: Filters data based on a recursive combination of past input and output samples.
- `Use Case`: Audio processing, feedback control systems.

13. `Wavelet Transform`:

- `Purpose`: Decomposes a signal into its components at different scales.
- `Use Case`: Signal denoising, feature extraction in image and signal analysis.

14. `Matched Filter`:

- `Purpose`: Maximizes the signal-to-noise ratio to detect a specific signal in the presence of noise.
- `Use Case`: Radar systems, communication systems, and target detection.

## Libraries that automate Image processing

1. Pillow
2. OpenCV
3. Scikit-Image (skimage)
4. imageio
5. PyTesseract
6. Mahotas
7. SimpleCV

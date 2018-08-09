# UI Droid Comparator
Finds UI changes between different versions of apps using Appium and OpenCV. Written in Python and it is based on this [tutorial](https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/).

## Installation
- `npm install -g appium`
- `pip install opencv-python`
- `pip install selenium`
- `pip install imutils`
- `pip install scikit-image`
- `pip install Appium-Python-Client`

## Run existing Test
- The existing test is for Google Maps. 
- Ideally for your own solution, you will want to have taken the original screenshots beforehand. 
  - Each time you take a screenshot with Appium, you call the `ci.compare_image` function and pass to it the new screenshot as well as the original one that you derived before.
- Run: `python appium_script.py -m com.google.android.maps.MapsActivity -c com.google.android.apps.maps`
  - By default it finds the first device from `adb devices`. If you want to pass another one use: `-d <device id>`

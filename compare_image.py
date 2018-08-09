import cv2
import imutils
from skimage.measure import compare_ssim

def compare_image(derived_image, original_image, display = True, waitFor = 20000):
  image0 = cv2.imread(derived_image)
  image0_gray = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)
  image1 = cv2.imread(original_image)
  image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  
  (score, diff) = compare_ssim(image0_gray, image1_gray, full=True)
  diff = (diff * 255).astype("uint8")
  
  threshold = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
  cnts = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if imutils.is_cv2() else cnts[1]
  
  for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(image0, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 0, 255), 2)
  
  if display is True:
    image0 = cv2.resize(image0, (0,0), fx=0.5, fy=0.5) 
    image1 = cv2.resize(image1, (0,0), fx=0.5, fy=0.5) 
    cv2.imshow("Derived", image0)
    cv2.imshow("Original", image1)
    cv2.waitKey(waitFor)
    cv2.destroyAllWindows()

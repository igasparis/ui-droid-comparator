from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import compare_image as ci
import os

class ScriptCl(object):
  def __init__(self, package, activity):
    self._package = package
    self._activity = activity
  
  def get_package_name(self): 
    return self._package
  
  def get_activity_name(self):
    return self._activity
  
  def findElementByIdAndSendText(self, driver, id, text):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
    element.clear()
    element.send_keys(text)
    driver.hide_keyboard()
  
  def run(self, driver):
    # do nothing
    pass


class GoogleMapsScriptCl(ScriptCl):
  def run(self, driver):
    time.sleep(10)
    
    self.findElementByIdAndSendText(driver, 'com.google.android.apps.maps:id/search_omnibox_text_box', 'Tinos, Greece')
    
    # press enter
    driver.press_keycode(66)
    time.sleep(10)
    
    # take screenshot
    driver.save_screenshot('screenshot.png')
    
    # press enter
    driver.back()
    time.sleep(3)
    driver.save_screenshot('other.png')
    
    ci.compare_image('screenshot.png', 'other.png', True, 21000)
    
    os.remove('other.png')
    os.remove('screenshot.png')

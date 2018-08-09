from appium import webdriver
from script import *
import getopt
import sys
import subprocess

def runAppium(ip, port, deviceId, scriptCl):
  desired_caps = {
    'appPackage' : scriptCl.get_package_name(),
    'appActivity' : scriptCl.get_activity_name(),
    'platformName' : 'Android',
    'udid' : deviceId,
    'deviceName' : 'Android',
    'autoLaunch' : True,
    'autoGrantPermissions' : True,
    'autoWebview': False
  }
  
  driver = webdriver.Remote('http://' + ip + ':' + port + '/wd/hub', desired_caps)
  scriptCl.run(driver)
  driver.quit()
  

def usage(): 
  print "Usage: python appium_script.py <-h help> [-a address] [-p port] [-d device id] <-m main activity> <-c package>"
  

if __name__ == "__main__":
  address = '0.0.0.0'
  port = '4723'
  deviceId = ''
  mainActivity = ''
  package = ''
  
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:p:d:m:c:e", ["help", "ip=", "port=", "device=", "main_activity=", "package="])
  except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit(2)
      
  for o, a in opts:
      if o in ("-h", "--help"):
        usage()
        sys.exit()
      elif o in ("-i", "--ip"):
        address = a
      elif o in ("-p", "--port"):
        port = a
      elif o in ("-d", "--device"):
        deviceId = a
      elif o in ("-m", "--main_activity"):
        mainActivity = a
      elif o in ("-c", "--package"):
        package = a        
      else:
          assert False, "unhandled option"
  
  if mainActivity == '' or package == '':
    usage()
    sys.exit(2)
  
  if deviceId == '':
    p = subprocess.Popen(["adb devices | sed '1,1d' | sed '$d' | cut -f 1 | sort | head -1"], shell=True, stdout=subprocess.PIPE)
    deviceId, err = p.communicate()
    deviceId = deviceId.rstrip()
    if deviceId == '':
      usage()
      sys.exit(2)
  
  scriptCl = GoogleMapsScriptCl(package, mainActivity)
  runAppium(address, port, deviceId, scriptCl)

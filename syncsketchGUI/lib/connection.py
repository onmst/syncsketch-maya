
import urllib2
import path


def is_connected():
  try:
    urllib2.urlopen(path.api_host_url)
    return True
  except:
     pass
  return False

def open_url(self):
    webbrowser.open(url)
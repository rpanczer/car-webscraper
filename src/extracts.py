# This file holds generic and reuseable formatting functions to be used in each configurations site_formatting.py file
def replaceNewlineExtract(element):
  if element is not None and len(element) > 0:
    element = element.replace('\n', '\\n')
    element = element.replace('\r','\\r')
    return element
  else:
    return None
    
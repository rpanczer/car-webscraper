
# Used to extract text from a list of tags. This function does not do any type of filtering or formatting
def textExtract(tag_list):
    extracted_text = []
    for tag in tag_list:
      extracted_text.append(tag.get_text())
    return extracted_text

# Used to extract numbers from a list.
def numberExtract(tag_list,tag_name):
    extracted_text = []
    for tag in tag_list:
      extracted_text = tag.get(tag_name)
    for element in extracted_text:
      if not element.isdigit():
        del element
    return extracted_text

def replaceNewlineExtract(tag_list):
  extracted_text = textExtract(tag_list)
  for element in extracted_text:
    if len(element) > 0:
      element = element.replace('\n', '\\n')
    else: 
      del element
    return extracted_text
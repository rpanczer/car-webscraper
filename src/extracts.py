
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

# uses a list of 2 or 3 cut_words
def spliceExtract(tag_list,cut_words):
  if len(cut_words) != 2 or len(cut_words) !=3:
    return False
  extracted_text = textExtract(tag_list)
  for text in extracted_text:
    if cut_words[0] in text:
      cut_locations = []
      for cut_word in cut_words:
        if cut_word in text:
          start = text.find(cut_word)
          cut_location = start + len(cut_word)
          cut_locations.append(cut_location)
      text = text[cut_locations[0]:cut_locations[1]]
    else:
      del text
  return extracted_text
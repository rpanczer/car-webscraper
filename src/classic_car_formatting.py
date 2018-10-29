from extracts import replaceNewlineExtract

def idParse(row,attribute):
    tag_list = row.find_all('a')
    for tag in tag_list:
      tag = tag.get(attribute)
      if tag is not None and tag.isdigit():
        return tag
    return None

def authorParse(row,_class):
  tag_list = row.select(_class)
  if len(tag_list) != 0:
    tag = tag_list[0].get_text()
    return tag
  else:
    return None

def createdAtParse(row,cut_words):
    if len(cut_words) != 2 and len(cut_words) !=3:
      print("Cut word list is not the correct length!")
      return False
    tag_list = row.select('.postdetails')
    if len(tag_list) > 0:
      for text in tag_list:
        text = text.get_text()
        if cut_words[0] in text:
          cut_locations = []
          for cut_word in cut_words:
            if cut_word in text:
              start = text.find(cut_word)
              cut_location = start + len(cut_word)
              cut_locations.append(cut_location)
          text = text[cut_locations[0]:cut_locations[1]]
          if len(text) > 0:
            return text
    else:
      return None

def bodyParse(row):
  row = row.select('.postbody')
  if row is not None and len(row) > 0:
    row = row[0].get_text()
    body_text = replaceNewlineExtract(row)
    if body_text is not None:
      return body_text
  else:
    return None

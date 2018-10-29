from extracts import textExtract, numberExtract, replaceNewlineExtract, spliceExtract

def idParse(row,attribute):
    tag_list = row.find_all('a')
    for tag in tag_list:
      tag = tag.get(attribute)
      if tag is not None and tag.isdigit():
        return tag
    return None

def authorParse(row,_class):
  tag_list = row.select(_class)
  tag = tag_list[0].get_text()
  if tag is not None:
    return tag
  else:
    return None

def createdAtParse(row,cut_words):
    tag_list = row.select('.postdetails')
    extracted_text = ''
    if len(cut_words) != 2 and len(cut_words) !=3:
      return False
    tag_list_text = textExtract(tag_list)
    if tag_list_text is not None:
      for text in tag_list_text:
        if cut_words[0] in text:
          cut_locations = []
          for cut_word in cut_words:
            if cut_word in text:
              start = text.find(cut_word)
              cut_location = start + len(cut_word)
              cut_locations.append(cut_location)
          text = text[cut_locations[0]:cut_locations[1]]
      return extracted_text
    else:
      return None

def bodyParse(row):
  row = row.select('.postbody')
  body_text = replaceNewlineExtract(row)
  return body_text

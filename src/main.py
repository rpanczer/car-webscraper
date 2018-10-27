import requests, bs4, csv
from scrubbers import textExtract, numberExtract, replaceNewlineExtract

site = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&postdays=0&postorder=asc&start=0'
site_src = requests.get(site)
site_src.raise_for_status()

bs4_obj = bs4.BeautifulSoup(site_src.text)

post_id = bs4_obj.find_all('a')
post_author = bs4_obj.select('.name')
post_details = bs4_obj.select('.postdetails')
post_body = bs4_obj.select('.postbody')

scrubbed_body = []
scrubbed_ids = []
scrubbed_authors = []
scrubbed_details = []
with open('thread.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, dialect='excel', quotechar=' ', doublequote=False, delimiter=' ', escapechar='\\')

    scrubbed_ids = numberExtract(post_id,'name')

    scrubbed_authors = textExtract(post_author)

    scrubbed_body = replaceNewlineExtract(post_body)

    cut_words = ['Posted: ','am','pm']
    for detail in post_details:
      if 'Posted:' in detail.get_text():
        detail = detail.get_text()   
        cut_locations = []
        for cut_word in cut_words:
          if cut_word in detail:
            start = detail.find(cut_word)
            cut_location = start + len(cut_word)
            cut_locations.append(cut_location)
        detail = detail[cut_locations[0]:cut_locations[1]]
        scrubbed_details.append(detail)
        
    if (len(scrubbed_body) == len(scrubbed_ids) == len(scrubbed_authors) == len(scrubbed_details)) :
      post_length = len(scrubbed_ids)
      i = 0
      while i < post_length:
        row = scrubbed_ids[i] + ",'" + scrubbed_authors[i] + "','" + scrubbed_details[i] + "','" + scrubbed_body[i] + "'"
        print(row)
        csv_writer.writerow(row)
        i += 1
    

    

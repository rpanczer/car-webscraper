import requests, bs4, csv
from extracts import textExtract, numberExtract, replaceNewlineExtract, spliceExtract

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

    # scrubbed_details = spliceExtract(post_details)

    # scrubbed_details = regexExtract(post_details)

    cut_words = ['Posted: ','am','pm']

        
    if (len(scrubbed_body) == len(scrubbed_ids) == len(scrubbed_authors) == len(scrubbed_details)) :
      post_length = len(scrubbed_ids)
      i = 0
      while i < post_length:
        row = scrubbed_ids[i] + ",'" + scrubbed_authors[i] + "','" + scrubbed_details[i] + "','" + scrubbed_body[i] + "'"
        print(row)
        csv_writer.writerow(row)
        i += 1
    

    

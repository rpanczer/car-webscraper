import requests, bs4, csv

site = requests.get('http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&postdays=0&postorder=asc&start=0')
site.raise_for_status()

bs4_obj = bs4.BeautifulSoup(site.text)

post_id = bs4_obj.find_all('a')
post_author = bs4_obj.select('.name')
post_details = bs4_obj.select('.postdetails')
post_body = bs4_obj.select('.postbody')

scrubbed_ids = []
scrubbed_authors = []
scrubbed_details = []
with open('thread.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    post = ''
    print('----------')
    print(len(post_id))
    print(len(post_author))
    print(len(post_details))
    print(len(post_body))
    print('----------')

    for num_id in post_id:
      num_id = num_id.get('name')
      if num_id is not None and num_id.isdigit():
        print(num_id)


    for author in post_author:
      scrubbed_authors.append(author.get_text())
    print(scrubbed_authors)

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
    print(scrubbed_details)
    # <a name="87131">
    # for body in post_body:
    #   print(body.get_text())
    #   print('@@@@@@@@@@@@@@@@@@@@')



    csv_writer.writerow(['Spam'])

import requests, bs4, csv

site = requests.get('http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&postdays=0&postorder=asc&start=0')
site.raise_for_status()

bs4_obj = bs4.BeautifulSoup(site.text)

# post_id = bs4_obj.select('.id')
post_author = bs4_obj.select('.name')
post_details = bs4_obj.select('.postdetails')
post_body = bs4_obj.select('.postbody')

with open('thread.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    post = ''
    print('----------')
    print(len(post_author))
    print(len(post_details))
    print(len(post_body))
    print('----------')

    csv_writer.writerow(['Spam'])

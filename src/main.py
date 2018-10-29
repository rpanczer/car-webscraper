import requests, bs4, csv
import json
from extracts import textExtract, numberExtract, replaceNewlineExtract, spliceExtract

def main():
  post = 0
  posts = []
  continue_scraping = True
  while continue_scraping:
    url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&postdays=0&postorder=asc&start=' + str(post)
    bs4_obj = make_soup(url)
    page_post_list = create_post_objects(bs4_obj)
    if len(page_post_list) > 0:
      for post in page_post_list:
        posts.append(post)
        post = len(posts) + 1  
    else:
      continue_scraping = False
      write_posts_to_csv(posts)

def make_soup(url):
  print("cooking some soup...")
  print(url)
  site_src = requests.get(url)
  site_src.raise_for_status()
  bs4_obj = bs4.BeautifulSoup(site_src.text, 'html.parser')
  return bs4_obj
  
def create_post_objects(bs4_obj):
  errors = {}
  page_post_list = []
  page_rows = bs4_obj.find_all('tr')
  for row in page_rows:
    post_id = row.find_all('a')
    post_author = row.select('.name')
    post_details = row.select('.postdetails')
    post_body = row.select('.postbody')
    if post_id is not None and post_author is not None and post_details is not None and post_body is not None:
      post_details_cut_words = ['Posted: ','am','pm']
      post = {}
      post['id'] = numberExtract(post_id,'name')
      post['author'] = textExtract(post_author)
      post['created_at'] = spliceExtract(post_details,post_details_cut_words)
      post['body'] = replaceNewlineExtract(post_body)
      print(json.dumps(post, indent=2))
      page_post_list.append(post)
  return page_post_list, errors

def write_posts_to_csv(posts):
  with open('thread.csv', 'w', newline='') as csvfile:
      csv_writer = csv.writer(csvfile, dialect='excel', quotechar=' ', doublequote=False, delimiter=' ', escapechar='\\')
      for post in posts:
        row = post['id'] + ",'" + post['author'] + "','" + post['created_at'] + "','" + post['body'] + "'"
        csv_writer.writerow(row)

if __name__ == '__main__':
    main()
    

    

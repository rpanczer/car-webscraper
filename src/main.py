import requests, bs4, csv
import json
from classic_car_formatting import idParse, authorParse, createdAtParse, bodyParse

def main():
  post_number = 0
  posts = []
  continue_scraping = True
  while continue_scraping:
    url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&postdays=0&postorder=asc&start=' + str(post_number)
    bs4_obj = make_soup(url)
    page_post_list = create_post_objects(bs4_obj)
    if len(page_post_list) > 0:
      for post in page_post_list:
        posts.append(post)
      post_number = len(posts) 
    else:
      continue_scraping = False
      write_posts_to_csv(posts)

def make_soup(url):
  print("cooking some soup with...", url)
  site_src = requests.get(url)
  site_src.raise_for_status()
  bs4_obj = bs4.BeautifulSoup(site_src.text, 'html.parser')
  return bs4_obj
  
def create_post_objects(bs4_obj):
  page_post_list = []
  page_rows = bs4_obj.find_all('tr')
  post_details_cut_words = ['Posted: ','am','pm']
  i = 0
  for row in page_rows:
    post_id = idParse(row,'name')
    post_author = authorParse(row,'.name')
    post_created_at = createdAtParse(row,post_details_cut_words)
    post_body = bodyParse(row)

    if post_id is not None and post_author is not None and post_created_at is not None and post_body is not None:
      post = {}
      post['id'] = post_id
      post['author'] = post_author
      post['created_at'] = post_created_at
      post['body'] = post_body
      
      page_post_list.append(post)
      i += 1
  return page_post_list

def write_posts_to_csv(posts):
  with open('thread.csv', 'w', newline='') as csvfile:
      csv_writer = csv.writer(csvfile, dialect='excel', quotechar=' ', doublequote=False, delimiter=' ', escapechar='\\')
      for post in posts:
        print(json.dumps(post, indent=2))
        row = post['id'] + "," + post['author'] + "," + post['created_at'] + "," + post['body']
        csv_writer.writerow(row)

if __name__ == '__main__':
    main()

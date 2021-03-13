# Code Snippet for Reading online hosted book, fast!
# decided to add this script for persons not able to work with notebooks
import urllib3
http = urllib3.PoolManager()
little_women_url = 'https://www.inferentialthinking.com/data/little_women.txt'
#little_women_text = print(little_women_url)
little_women_text = http.request('GET','https://www.inferentialthinking.com/data/little_women.txt') #returns http request 200 if all is ok

#read the whole book
little_women_text_content = little_women_text.read()
print(little_women_text_content)

#code to read online book
import urllib3
http = urllib3.PoolManager()
book = http.request('GET', 'https://www.inferentialthinking.com/data/little_women.txt')
read_book_content = book.data
print(read_book_content)

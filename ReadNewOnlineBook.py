#code to read online book
import urllib3
http = urllib3.PoolManager()
book = http.request('GET', 'https://www.inferentialthinking.com/data/little_women.txt')
read_Little_Women_Book = book.data
print(read_Little_Women_Book)

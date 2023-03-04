import urllib3
http = urllib3.PoolManager()
read = http.request('GET', 'https://www.inferentialthinking.com/data/little_women.txt')
read_type = type(read)
print(read.data)


#print(read_content)
#read_content = read_content.decode('utf-8')
#print(read_content)

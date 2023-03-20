#use variable name myBookURL to store the url
myBookURL <- "http://www.gutenberg.org/files/1342/1342-0.txt"
#use variable name myBook to store the book
myBook <- readLines(myBookURL)
#print the first 10 lines of the book
myBook[1:10]

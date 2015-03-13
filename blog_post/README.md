# Tips for writing a crawler

* optimise for the lowest number of requests to the server
* do the requests in the night when nobody uses the website
* add a sleep between requests or do them from multiple machines
* log every step so you know when you stop
* be prepared for lots of unexpected things
* have patiance because it will take longer than expected
* be prepared to redo at the end because you forgot to scrape for one param

# Libraries I used

* requests - simple API for HTTP calls
* BeautifulSoup - beautiful API for digging into HTML
* arrow - tasteful API for dealing with dates and time

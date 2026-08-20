#code to read online book
#import urllib3
#http = urllib3.PoolManager()
#book = http.request('GET', 'https://www.inferentialthinking.com/data/little_women.txt')
#read_Little_Women_Book = book.data
#print(read_Little_Women_Book)
## below code was generated using copilot to demo how to update legacy code:

"""Download and read Little Women from the course data site."""

from urllib.error import HTTPError, URLError
from urllib.request import urlopen

LITTLE_WOMEN_URL = "https://www.inferentialthinking.com/data/little_women.txt"


def read_url(url: str, *, timeout: float = 30.0) -> str:
    """Return UTF-8 text downloaded from *url*."""
    try:
        with urlopen(url, timeout=timeout) as response:
            return response.read().decode("utf-8")
    except HTTPError as error:
        raise RuntimeError(
            f"Server returned HTTP {error.code} while downloading {url}"
        ) from error
    except URLError as error:
        raise RuntimeError(f"Could not download {url}: {error.reason}") from error


little_women_text = read_url(LITTLE_WOMEN_URL)
little_women_chapters = little_women_text.split("CHAPTER ")[1:]

print(little_women_chapters[0])

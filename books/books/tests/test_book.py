import unittest
from scrapy.http import HtmlResponse, Request
from books.items import BooksItem
from books.spiders.book import BookSpider

class BookSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = BookSpider()
        self.example_html = """
<html>
  <body>
    <article class="product_pod">
      <h3>
        <a href="catalogue/book-one_1/index.html" title="Book One">
          Book One
        </a>
      </h3>
      <p class="price_color">£10.00</p>
    </article>

    <article class="product_pod">
      <h3>
        <a href="catalogue/book-two_2/index.html" title="Book Two">
          Book Two
        </a>
      </h3>
      <p class="price_color">£15.00</p>
    </article>

    <ul class="pager">
      <li class="next">
        <a href="page-2.html">next</a>
      </li>
    </ul>
  </body>
</html>
"""
        self.response = HtmlResponse(
            url="https://books.toscrape.com",
            body = self.example_html,
            encoding="utf-8"
        )

    def test_parse_scrapes_all_items(self):
        """ Test if the spider scapes books and pagination links """
        # Collect the items produced by the generator in a list
        # so that it's possible to iterate over it more htan once.
        results = list(self.spider.parse(self.response))

        # There should be two items and one pagination request
        book_items = [item for item in results if isinstance(item, BooksItem)]
        pagination_requests = [item for item in results if isinstance(item, Request)]

        self.assertEqual(len(book_items), 2)
        self.assertEqual(len(pagination_requests), 1)

    def test_parse_scrapes_correct_book_information(self):
        """ Test if the spider scrapes the correct information for each book. """
        pass

    def test_parse_creates_pagination_requests(self):
        """ Test if the spider creates a pagination request correctly """
        pass

if __name__ == "__main__":
    unittest.main()
from bs4 import BeautifulSoup
import requests



class Scraper:
    """
    A web scraper class for extracting content and links from websites.
    
    This class provides methods to fetch and parse HTML content from web pages,
    extracting both textual content and hyperlinks using BeautifulSoup.
    
    Attributes:
        headers (dict): HTTP headers to use for requests, including a User-Agent
                       to simulate a browser request.
    """
    
    def __init__(self):
        """Initialize the Scraper with standard HTTP headers."""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
    
    def fetch_website_contents(self, url):
        """
        Fetch and extract the textual content from a webpage.
        
        This method retrieves the HTML content from the specified URL, extracts
        the page title and body text while removing script, style, image, and
        input elements. The result is truncated to 2,000 characters.
        
        Args:
            url (str): The URL of the webpage to fetch.
        
        Returns:
            str: The page title followed by the body text, truncated to 2,000
                 characters. Returns "No title found" if the page has no title.
        
        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string if soup.title else "No title found"
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            text = soup.body.get_text(separator="\n", strip=True)
        else:
            text = ""
        return (title + "\n\n" + text)[:2_000]
    
    def fetch_website_links(self, url):
        """
        Fetch and extract all hyperlinks from a webpage.
        
        This method retrieves the HTML content from the specified URL and
        extracts all href attributes from anchor (<a>) tags, filtering out
        any None or empty values.
        
        Args:
            url (str): The URL of the webpage to fetch.
        
        Returns:
            list[str]: A list of all valid hyperlinks found on the page.
        
        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        links = [link.get("href") for link in soup.find_all("a")]
        return [link for link in links if link]

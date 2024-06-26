import scrapy
import re  # Import for regular expressions

class CityParagraphsSpider(scrapy.Spider):
  name = "foreign_city_data_scraper"
  start_urls = ["https://en.wikipedia.org/wiki/Paris","https://en.wikipedia.org/wiki/Madrid","https://en.wikipedia.org/wiki/Ruhr","https://en.wikipedia.org/wiki/Milan","https://en.wikipedia.org/wiki/Barcelona","https://en.wikipedia.org/wiki/Berlin","https://en.wikipedia.org/wiki/Naples","https://en.wikipedia.org/wiki/Athens","https://en.wikipedia.org/wiki/Rome","https://en.wikipedia.org/wiki/Rotterdam","https://en.wikipedia.org/wiki/The_Hague","https://en.wikipedia.org/wiki/Lisbon","https://en.wikipedia.org/wiki/Budapest","https://en.wikipedia.org/wiki/Brussels","https://en.wikipedia.org/wiki/Cologne/Bonn_Region","https://en.wikipedia.org/wiki/Stockholm","https://en.wikipedia.org/wiki/Hamburg","https://en.wikipedia.org/wiki/Munich","https://en.wikipedia.org/wiki/Bucharest","https://en.wikipedia.org/wiki/Frankfurt","https://en.wikipedia.org/wiki/Vienna","https://en.wikipedia.org/wiki/Warsaw","https://en.wikipedia.org/wiki/Katowice_urban_area","https://en.wikipedia.org/wiki/Amsterdam","https://en.wikipedia.org/wiki/Copenhagen","https://en.wikipedia.org/wiki/Valencia","https://en.wikipedia.org/wiki/Turin","https://en.wikipedia.org/wiki/Lyon","https://en.wikipedia.org/wiki/Marseille","https://en.wikipedia.org/wiki/Stuttgart","https://en.wikipedia.org/wiki/Dublin","https://en.wikipedia.org/wiki/Porto","https://en.wikipedia.org/wiki/Lille","https://en.wikipedia.org/wiki/Prague","https://en.wikipedia.org/wiki/Helsinki","https://en.wikipedia.org/wiki/Seville","https://en.wikipedia.org/wiki/Sofia","https://en.wikipedia.org/wiki/Antwerp","https://en.wikipedia.org/wiki/Toulouse","https://en.wikipedia.org/wiki/Utrecht","https://en.wikipedia.org/wiki/Gda%C5%84sk","https://en.wikipedia.org/wiki/Nice","https://en.wikipedia.org/wiki/Thessaloniki","https://en.wikipedia.org/wiki/Bordeaux","https://en.wikipedia.org/wiki/%C5%81%C3%B3d%C5%BA","https://en.wikipedia.org/wiki/Bilbao","https://en.wikipedia.org/wiki/Florence","https://en.wikipedia.org/wiki/Palermo","https://en.wikipedia.org/wiki/Krak%C3%B3w","https://en.wikipedia.org/wiki/Hanover","https://en.wikipedia.org/wiki/Nuremberg","https://en.wikipedia.org/wiki/Zaragoza","https://en.wikipedia.org/wiki/Dresden","https://en.wikipedia.org/wiki/M%C3%A1laga","https://en.wikipedia.org/wiki/Zagreb","https://en.wikipedia.org/wiki/Catania","https://en.wikipedia.org/wiki/Gothenburg","https://en.wikipedia.org/wiki/Pozna%C5%84","https://en.wikipedia.org/wiki/Bergamo","https://en.wikipedia.org/wiki/Mannheim","https://en.wikipedia.org/wiki/Leipzig","https://en.wikipedia.org/wiki/Wroc%C5%82aw","https://en.wikipedia.org/wiki/Las_Palmas","https://en.wikipedia.org/wiki/Riga","https://en.wikipedia.org/wiki/Bremen","https://en.wikipedia.org/wiki/Nantes","https://en.wikipedia.org/wiki/Aachen","https://en.wikipedia.org/wiki/Vilnius","https://en.wikipedia.org/wiki/Genoa","https://en.wikipedia.org/wiki/Palma,_Majorca","https://en.wikipedia.org/wiki/Santa_Cruz_de_Tenerife","https://en.wikipedia.org/wiki/Aarhus","https://en.wikipedia.org/wiki/Oviedo","https://en.wikipedia.org/wiki/Gij%C3%B3n","https://en.wikipedia.org/wiki/Avil%C3%A9s","https://en.wikipedia.org/wiki/Alicante","https://en.wikipedia.org/wiki/Elche","https://en.wikipedia.org/wiki/Elda","https://en.wikipedia.org/wiki/Ostrava","https://en.wikipedia.org/wiki/Bologna","https://en.wikipedia.org/wiki/Malm%C3%B6","https://en.wikipedia.org/wiki/Grenoble","https://en.wikipedia.org/wiki/Douai","https://en.wikipedia.org/wiki/Lens,_Pas-de-Calais","https://en.wikipedia.org/wiki/Toulon","https://en.wikipedia.org/wiki/Charleroi","https://en.wikipedia.org/wiki/Odense","https://en.wikipedia.org/wiki/Granada","https://en.wikipedia.org/wiki/Vigo","https://en.wikipedia.org/wiki/Montpellier","https://en.wikipedia.org/wiki/Eindhoven","https://en.wikipedia.org/wiki/Rennes","https://en.wikipedia.org/wiki/Brno","https://en.wikipedia.org/wiki/Bari","https://en.wikipedia.org/wiki/Heidelberg","https://en.wikipedia.org/wiki/Rouen","https://en.wikipedia.org/wiki/Augsburg","https://en.wikipedia.org/wiki/Bratislava","https://en.wikipedia.org/wiki/Kiel","https://en.wikipedia.org/wiki/Murcia","https://en.wikipedia.org/wiki/Catania","https://en.wikipedia.org/wiki/Tallinn","https://en.wikipedia.org/wiki/Ghent","https://en.wikipedia.org/wiki/Venice","https://en.wikipedia.org/wiki/Groningen","https://en.wikipedia.org/wiki/Plovdiv","https://en.wikipedia.org/wiki/Padua","https://en.wikipedia.org/wiki/M%C3%BCnster","https://en.wikipedia.org/wiki/Erfurt","https://en.wikipedia.org/wiki/Tours","https://en.wikipedia.org/wiki/Verona","https://en.wikipedia.org/wiki/Nancy,_France","https://en.wikipedia.org/wiki/Clermont-Ferrand", "https://en.wikipedia.org/wiki/Monte_Carlo", "https://en.wikipedia.org/wiki/London","https://en.wikipedia.org/wiki/City_of_Westminster","https://en.wikipedia.org/wiki/Birmingham","https://en.wikipedia.org/wiki/City_of_Leeds","https://en.wikipedia.org/wiki/Glasgow","https://en.wikipedia.org/wiki/Manchester","https://en.wikipedia.org/wiki/City_of_Sheffield","https://en.wikipedia.org/wiki/City_of_Bradford","https://en.wikipedia.org/wiki/Edinburgh","https://en.wikipedia.org/wiki/Liverpool","https://en.wikipedia.org/wiki/Bristol","https://en.wikipedia.org/wiki/Cardiff","https://en.wikipedia.org/wiki/Leicester","https://en.wikipedia.org/wiki/City_of_Coventry","https://en.wikipedia.org/wiki/City_of_Wakefield","https://en.wikipedia.org/wiki/Belfast","https://en.wikipedia.org/wiki/Nottingham","https://en.wikipedia.org/wiki/Newcastle_upon_Tyne","https://en.wikipedia.org/wiki/City_of_Doncaster","https://en.wikipedia.org/wiki/City_of_Milton_Keynes","https://en.wikipedia.org/wiki/City_of_Salford","https://en.wikipedia.org/wiki/City_of_Sunderland","https://en.wikipedia.org/wiki/Brighton_and_Hove","https://en.wikipedia.org/wiki/Wolverhampton","https://en.wikipedia.org/wiki/Kingston_upon_Hull","https://en.wikipedia.org/wiki/Plymouth","https://en.wikipedia.org/wiki/Derby","https://en.wikipedia.org/wiki/Stoke-on-Trent","https://en.wikipedia.org/wiki/Southampton","https://en.wikipedia.org/wiki/Swansea","https://en.wikipedia.org/wiki/Aberdeen","https://en.wikipedia.org/wiki/City_of_Peterborough","https://en.wikipedia.org/wiki/Portsmouth","https://en.wikipedia.org/wiki/City_of_York","https://en.wikipedia.org/wiki/City_of_Colchester","https://en.wikipedia.org/wiki/City_of_Chelmsford","https://en.wikipedia.org/wiki/Oxford","https://en.wikipedia.org/wiki/Newport,_Wales","https://en.wikipedia.org/wiki/City_of_Canterbury","https://en.wikipedia.org/wiki/City_of_Preston,_Lancashire","https://en.wikipedia.org/wiki/Dundee","https://en.wikipedia.org/wiki/Cambridge","https://en.wikipedia.org/wiki/St_Albans_City_and_District","https://en.wikipedia.org/wiki/City_of_Lancaster","https://en.wikipedia.org/wiki/Norwich","https://en.wikipedia.org/wiki/Chester","https://en.wikipedia.org/wiki/Exeter","https://en.wikipedia.org/wiki/Wrexham_County_Borough","https://en.wikipedia.org/wiki/Gloucester","https://en.wikipedia.org/wiki/City_of_Winchester","https://en.wikipedia.org/wiki/Durham,_England","https://en.wikipedia.org/wiki/Carlisle","https://en.wikipedia.org/wiki/City_of_Worcester","https://en.wikipedia.org/wiki/Lincoln,_England"]

  # custom_settings = {
  #       'FEED_FORMAT': 'csv',
  #       'FEED_URI': 'city_data.csv'
  #   }

  def clean_paragraph_text(self, text):
    # # Remove HTML tags and replace anchor tags with their text
    # text = re.sub(r'<a[^>]*>(.*?)</a>', r'\1', text)  # Replace <a> with its content
    # text = re.sub(r'<[^>]*>', '', text)  # Remove remaining tags
    
    # text = re.sub(r'<sup.*?>.*?</sup>', '', text)
    # text = re.sub(r'<a[^>]*>\[([^\]]+)\]</a>', r'\1', text)  # Replace anchor tag with content
    # text = re.sub(r'<[^>]*>', '', text)  # Remove all remaining tags

    pattern = r"""
    # Match optional leading slash (/)
    (/)?

    # Match optional pronunciation section (captured group 1)
    (\[(?:\s*|\S| )*\]|\([^)]*\)|<[^>]*>)*?        # Capture anything between brackets, parentheses, or HTML tags (including whitespace and non-breaking space)

    # Match optional comma, whitespace, or specific characters (captured group 2)
    (?:,\s*|\s*(?:Kannada pronunciation:|, IAST: Muṃbaī; formerly known as Bombay\[a\]))?

    # Optional trailing characters with specific class (captured group 3)
    (\s*|\s* *.mw-parser-output\s*.*?)?           # Capture any remaining text with specific class (including whitespace and non-breaking space)
"""

    # Replace matched parts with an empty string
    text = re.sub(pattern, "", text)
    text = re.sub(r'\[([^\]]+)\]', '', text)      
    return text.strip()  # Remove leading/trailing whitespace

  def parse(self, response):
    city_name = response.url.split("/")[-1]  # Extract city name from URL

    paragraphs = []
    for paragraph in response.css("p"):
      # Get text content, preserving whitespace and line breaks
      paragraph_text = paragraph.css("::text").getall()  # Keep whitespace
      # Join paragraph text parts and clean
      paragraph_text = self.clean_paragraph_text("".join(paragraph_text))
      paragraphs.append(paragraph_text)
      # paragraphs.append("".join(paragraph_text))

    # Extract URL of the first image
    image_url = response.css("td.infobox-full-data img:first-child[src^='//upload']::attr(src)").get()

    # Create a dictionary for the city data (if paragraphs and image exist)
    if paragraphs and image_url:
      city_data = {
        "city": city_name,
        "paragraphs": paragraphs,
        "image_url": image_url
      }
      yield city_data
    else:
      if not paragraphs:
        print(f"No paragraphs found for {city_name}!")
      if not image_url:
        print(f"No image found for {city_name}!")

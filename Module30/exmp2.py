from bs4 import BeautifulSoup

html_content = """

    <html>
    <head>
    <title>Example Page</title>
    </head>
    <body>
    <h1>Welcome to the bs4</h1>
    <p class="intro">BeautifulSoup makes web scraping easy</p>
    <div id="content">
        <p>Here are some links:</p>
        <a href="http://example.com/page1">Page 1</a>
        <a href="http://example.com/page2">Page 2</a>
        <a href="http://example.com/page3">Page 3</a>
    </div>
    </body>
    </html>

"""

soup = BeautifulSoup(html_content, 'html.parser')

print("Title of page:", soup.title.text)

intro_text = soup.find('p', class_='intro').text
print("Intro paragraph:", intro_text)

div_content = soup.find('div', id='content')
links = div_content.find_all('a')
for link in links:
    print("Link", link['href'])


first_link = soup.find('a')
print("First link text :", first_link.text)
print("Next sibling of first link :", first_link.find_next_sibling)

paragraphs = soup.select('div#content p')
for paragraph in paragraphs:
    print("Paragraph in content:", paragraph.text)

new_tag = soup.new_tag('b')
new_tag.string = "Important"
soup.h1.append(new_tag)
print("Modified h1 tag:", soup.h1)

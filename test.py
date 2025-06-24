from bs4 import BeautifulSoup

html_doc = """
<div>
  <h1>Hello</h1>
  <p>
    World
  </p>
</div>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# 들여쓰기 없이 출력
pretty_html = soup.prettify(formatter="html")
print(pretty_html)


# 들여쓰기 없이 출력
pretty_html = soup.encode(formatter="html").decode()
print(pretty_html)
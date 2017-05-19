from bs4 import BeautifulSoup

html = [
    '<html><body><heading name="header" style="font-size:20px;"><i>This is the titile <br /><br /></i></heading><b>This is the body</b><p>This is para 1<a href="www.google.com">Google</a></p><p>This is para 2</p></body></html>']

html = ''.join(html)

# print html

soup = BeautifulSoup(html)

# print soup.prettify()

# print soup.html.name

# print soup.heading.name

# print soup.body.text

# print soup.html.contents

# print soup.body.contents

# print soup.body.parent.name

# print soup.heading.nextSibling

# print soup.heading.previousSibling

# print soup.b.previousSibling

# print soup.b.nextSibling

# bold = soup.findAll('b')

# print bold

# print bold[0].text

# paras = ' '.join([p.text for p in soup.findAll('p')])

# print paras

# font20 = ' '.join([p.text for p in soup.findAll(style="font-size:20px")])

# print font20

# print soup.findAll(['b', 'p', 'a'])

# print soup.find('a').text

# linkData = soup.find('a')

# print linkData['href']

# print linkData.text


# print soup.find(text="Google").findNext('p').text
```python
import requests
from bs4 import BeautifulSoup
import re
import sys
if len(sys.argv)>1:
    url=sys.argv[1]
else:
    sys.exit("ERROR: PLZ ENTER URL")
# url='https://www.ted.com/talks/malcolm_gladwell_choice_happiness_and_spaghetti_sauce/'
r=requests.get(url)
print("download starting..................")
soup=BeautifulSoup(r.content,features="lxml")
for val in soup.findAll("script"):
    if (re.search("pageProps",str(val))) is not None:
        result = str(val)
result_mp4 = re.search("(?P<url>https?://[^\s]+.mp4)",result).group("url")
mp4_url=result_mp4.split('"')[0]
print("downloading video.."+mp4_url)
file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]
print("storing video in....." + file_name)
r=requests.get(url)
with open(file_name,'wb') as f:
    f.write(r.content)
print("downlaod finish")


```

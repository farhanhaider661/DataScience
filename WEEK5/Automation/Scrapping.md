```python
import requests # http requests

from bs4 import BeautifulSoup # web scraping
# Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime
now=datetime.datetime.now()
# email content placeholder
content=''
def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text!='More' else '')
        #print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
    return(cnt)
cnt=extract_news('https://news.ycombinator.com/')
content+=cnt
content+=('<br>----<br>')
content+=('<br><br> END OF MESSAGE')
print("composing email...........")
SERVER='smtp.gmail.com'
PORT=587
FROM='fhan15840@gmail.com'
TO='fhan15840@gmail.com'
PASS='umfqrwwnxoyecdmm'
msg=MIMEMultipart()
msg['Subject']='Top News STORIES HN [Automated Email]'+' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From']=FROM
msg['To']=TO
msg.attach(MIMEText(content,'html'))
print('Initializing server')
server=smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())
print('EMAIL SENT.......')
server.quit()

```

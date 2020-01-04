def dlLink(link):
   import os
   import re
   import urllib
   from bs4 import BeautifulSoup
   from urllib.request import urlopen
   soup = BeautifulSoup(urlopen(link), features="html.parser")
   soup2 = soup.title.string
   title1 = soup2.replace(" ", "_")
   title2 = str(title1)
   title3 = re.sub('[!"#$%&()*+,./:;<=>?@[\]^`{|}~]', '', title2)
   title4 = re.sub("'", '', title3)
   print(title4)
   print("wkhtmltopdf " + link + " " + title4 + ".pdf")
   os.system("wkhtmltopdf " + link + " --load-error-handling ignore " + title4 + ".pdf")

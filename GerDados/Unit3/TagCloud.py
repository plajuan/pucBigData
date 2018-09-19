from urllib.request import urlopen
from pyquery import PyQuery as pq
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Read from URL and parse worst passwords
text = pq(urlopen('https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/worst-passwords-2017-top100-slashdata.txt#L28').read())
li = {}
peso = 101
for i in range(1, 101):
    li[text('#LC'+str(i)).text()] = peso - i

#Create word cloud and show it using matplotlib
wordcloud = WordCloud(width=720, height=720, margin=0, background_color='white').generate_from_frequencies(li)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

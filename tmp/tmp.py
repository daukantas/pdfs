import os
from urllib import urlopen


for i in range(1, 52):
    username = urlopen('http://127.0.0.1:8000/events/3/participant/%s/name/' % i).read().strip()
    os.system('wget http://127.0.0.1:8000/events/3/participant/%s/pdf/' % i)
    os.system('mv index.html "%s.pdf"' % username)

url = "https://movie.daum.net/premovie/released"
response = urllib.request.urlopen(url)
soup = BueatifulSoupt(response,'html.parser')
table = soup.select('em. ico_movie ico_allrating a')
for result3 in table:
    mtitle = str(result3.string)
    mcode = str(result3.attrs['href'])
    i=str(re.findall('\d+', mcode)[0]) 
    timecode=tuple([i]) 
    tmtitle = tuple([mtitle]) #made tuple as in executemany에서 튜플을 써서
    tmrvl.append(tmtitle+timeco)

  
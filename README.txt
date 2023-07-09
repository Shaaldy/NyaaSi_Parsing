This program allows you to parse the site Nyaa.si .
I wrote it in order to get content from this site faster, specifically
I wrote it in order to get new One Piece series with subtitles from Erai-Raws faster.
Due to the fact that the name of the subs is written in the same line with the name,
some may not work, since I chose the pars for the case when [Sub]NameAnime - ep [quality][eng][rus][jup]...,
according to this, if in the name for example quality in parentheses, so for example SubsPlease is written in (720p).

It is necessary to run test.py , in order to write data from the Nasa website to an excel spreadsheet.
Before launching, make sure that the site opens in your browser. Otherwise, you will get an error in line 14
parsNyaaSi.py resp = requests.get(url=url, stream=True).
And also change header and way to parsNyaaSi.py (line 8) on your own.
I note that the tar-file does not work unfortunately, but the link in xlsx is working, you can follow it

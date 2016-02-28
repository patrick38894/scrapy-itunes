to use:

1) install scrapy
	pip install scrapy --user

2) cd to scrapy-itunes/musicdb
	cd ~/scrapy-itunes/musicdb

3) run the web crawler and dump to json file
	~/.local/bin/scrapy crawl itunes -o ../data.json
	(after a couple minutes the bot will be banned but it should collect a good amount of data anyway)

4) upload the data to the database
	python database.py

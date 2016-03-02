import psycopg2
import json
import hashlib


def genID(x):
	return str(int(hashlib.md5(x).hexdigest(), 16) % 2147483647)

try:
    conn = psycopg2.connect("dbname='w16adb5' user='w16adb5' host='dbclass.cs.pdx.edu' password='not the real password'")
except:
    print "I am unable to connect to the database"

print "successfully connect to database"


with open('data.json') as data_file:    
    data = json.load(data_file)

cur = conn.cursor()

n = 0
for i in data:
	if (i[j'son_type'] != 'general')
		continue
	album_name = i ["album"]
	song_price = i ["song_price"]
	song_length = i ["song_length"]
	artist_name = i ["artist_name"]
	track_number = i ["track_number"]
	song_name = i ["track_name"]
	genre = i ["genre"]
	
	print song_name
	
	artist_id = genID(artist_name)
	song_id = genID(song_name + artist_name)
	album_id = genID(album_name + artist_name)

	is_top_10 = False
	for (j in data):
		if (j['json_type'] == 'top10' && song_id == genID(j['track_name'] + j['artist']))
			is_top_10 = True

	try:
		query1 = "INSERT INTO music.artist (Artist_ID, Genre, Artist_Name) values "
		query1 += "(" + artist_id + ",\'" + genre + "\',\'" + artist_name + "\');"
		print(query1)
		cur.execute(query1)
	except:
		pass
	try:	
		query2 = "INSERT INTO music.song (Song_ID, Song_Name, Length, Song_Price) values "
		query2 += "(" + song_id + ",\'" + song_name + "\',\'" + song_length + "\',\'" + song_price + "\');"
		print(query2)
		cur.execute(query2)
	except:
		pass
	try:
		query3 = "INSERT INTO music.album (Album_ID, Album_Name) values "
		query3 += "(" +  album_id + ",\'" + album_name + "\');"
		print(query3)
		cur.execute(query3)
	except:
		pass

	try:
		query4 = "INSERT INTO music.plays_on (Artist_ID, Album_ID) values "
		query4 += "(" +  artist_id + "," + album_id + ");"
		print(query4)
		cur.execute(query4)
	except:
		pass
	try:
		query5 = "INSERT INTO music.played_by (Artist_ID, Song_ID) values "
		query5 += "(" +  artist_id + "," + song_id + ");"
		print(query5)
		cur.execute(query5)
	except:
		pass

	try:
		query6 = "INSERT INTO music.appears_on (Album_ID, Song_ID, Track_Number) values "
		query6 += "(" +  album_id + "," + song_id + "," + track_number + ");"
		print(query6)
		cur.execute(query6)
	except:
		pass

	if (is_top_10):
		try
			query6 = "INSERT INTO music.Top_10(Artist_ID, Song_ID) values "
			query6 += "(" + artist_id + "," + song_id + ");"
			print(query6)
			cur.execute(query6)
		except:
			pass

	conn.commit()


conn.commit()
cur.close()
conn.close()

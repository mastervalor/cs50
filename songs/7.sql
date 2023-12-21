select avg(energy) from songs join artists ON songs.artist_id = artists.id where artists.name = 'Drake';

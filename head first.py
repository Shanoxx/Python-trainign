movies=["The Holy Grail", "Thr Life of brian", "The Meaning of Life"]
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(6, 1983)
print(movies)

for game_changer in movies:
    print(game_changer)

count=0
while count <len(movies):
    print(movies[count])
    count=count +1
    print(count)
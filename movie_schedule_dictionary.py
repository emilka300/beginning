current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '1:00pm',
                  'Frosty th Snowman': '3:00pm',
                  'Christmas Vacation': '5:00pm'}

print("We're sowing the following movies:")
for i in current_movies:
    print(i)
movie = input("What movie's showtime would you like check ").title().strip()

showtime = current_movies.get(movie)
if showtime is None:
    print("Requested movie isn't playing")
else:
    print(f"{movie} is playing at {showtime}")

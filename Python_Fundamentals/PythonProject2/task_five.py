movies_number = int(input())
best_movie = ""
best_movie_rating = 0
worst_movie = ""
worst_movie_rating = 11
sum_rating = 0

for i in range(movies_number):
    movie = input()
    movie_rating = float(input())
    if movie_rating > best_movie_rating:
        best_movie = movie
        best_movie_rating = movie_rating
    elif movie_rating < worst_movie_rating:
        worst_movie = movie
        worst_movie_rating = movie_rating

    sum_rating += movie_rating

print(f"{best_movie} is with highest rating: {best_movie_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {worst_movie_rating:.1f}")
print(f"Average rating: {sum_rating / movies_number:.1f}")

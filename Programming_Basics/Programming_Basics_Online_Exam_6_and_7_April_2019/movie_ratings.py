import sys

movies_count = int(input())
best_movie = ""
worst_movie = ""
best_move_rating = 0
worst_movie_rating = sys.maxsize
all_rating = 0
for i in range(1, movies_count + 1):
    movie = input()
    rating = float(input())
    all_rating += rating
    if rating > best_move_rating:
        best_movie = movie
        best_move_rating = rating
    elif rating < worst_movie_rating:
        worst_movie = movie
        worst_movie_rating = rating
average_rating = all_rating / movies_count
print(f"{best_movie} is with highest rating: {best_move_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {worst_movie_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")

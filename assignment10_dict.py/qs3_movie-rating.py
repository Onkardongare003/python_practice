
# ratings={“movie1”:{“ratings”:[4,2,5]},
# “Movie2”:{“ratings”:[1,3,5]},
# “Movie3”:{“ratings”:[9,2,6]}}

# Calculate average rating of each movie
# Add new rating to each movie
# Find the highest rated movie

rating={
    "movie1":[4,2,5],
    "movie2":[1,3,5],
    "movie3":[9,2,6]
}


# Calculate average rating of each movie
for movie in rating:
    avg=sum(rating[movie])/len(rating[movie])
    print(movie,"average = ",avg)

for movie in rating:
        rating[movie].append(4)# Add new rating to each movie
print(rating)

# Find the highest rated movie
higest_movie=""
avg=0
if(higest_movie>rating):
      print(rating)
       






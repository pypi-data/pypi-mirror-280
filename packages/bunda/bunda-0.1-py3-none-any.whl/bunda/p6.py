from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MovieRatingsAnalysis").getOrCreate()

movies_df = spark.read.csv("movies.csv", header=True, inferSchema=True)
ratings_df = spark.read.csv("ratings.csv", header=True, inferSchema=True)

movies_rdd = movies_df.rdd
ratings_rdd = ratings_df.rdd


avg_ratings_rdd = ratings_rdd.map(lambda x: (x['movieId'], (x['rating'], 1))) \
    .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \
    .mapValues(lambda x: x[0] / x[1])

lowest_avg_rating = avg_ratings_rdd.sortBy(lambda x: x[1]).first()
print(f"Movie with the lowest average rating: {lowest_avg_rating}")


from pyspark.sql.functions import from_unixtime, year, month

ratings_df = ratings_df.withColumn("year", year(from_unixtime(ratings_df['timestamp']))) \
                       .withColumn("month", month(from_unixtime(ratings_df['timestamp'])))

ratings_over_time = ratings_df.groupBy("year", "month").count().orderBy("year", "month")

ratings_over_time.show()


movie_ratings_stats = ratings_rdd.map(lambda x: (x['movieId'], (x['rating'], 1))) \
    .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \
    .mapValues(lambda x: (x[0] / x[1], x[1])) 

min_ratings = 100
qualified_movies = movie_ratings_stats.filter(lambda x: x[1][1] >= min_ratings)

highest_rated_movies = qualified_movies.sortBy(lambda x: x[1][0], ascending=False).take(10)
print(f"Highest-rated movies with at least {min_ratings} ratings: {highest_rated_movies}")


user_ratings_count = ratings_rdd.map(lambda x: (x['userId'], 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[1], ascending=False)

top_users = user_ratings_count.take(10)
print(f"Top users by number of ratings: {top_users}")
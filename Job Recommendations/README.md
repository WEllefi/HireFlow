# Introduction
Welcome to the Recommender Engine chapter, where we explore recommendation algorithms for personalized job matching. We’ll discuss principles, implement algorithms, showcase results, and reflect on the lessons learned.

In our recommendation system, we will implement two distinct architectures for each type of recommendation: the TopN architecture and the K-Nearest Neighbors-based rating prediction (KNN). Initially, the TopN architecture will be employed to provide users with a list of top job offers that match their preferences and interests. Subsequently, we will delve deeper into our data and explore the KNN algorithm to predict personalized ratings for job offers that users have not yet encountered. By combining these two approaches, we aim to deliver precise and targeted job recommendations, ultimately enhancing the user experience and facilitating more informed and satisfying job search journeys for our users.

## TopN Architecture
Once we have the recommendation candidates, we proceed to rank them according to their relevance to the user. Alternatively, we can apply a threshold, such as considering only job offers with a rating of 4/5 or higher. After ranking the candidates, we may observe that certain job offers appear multiple times due to their high similarity to the user’s preferences. In such cases, we employ filtering techniques to ensure diverse and relevant job offers are presented to the user, eliminating redundancies and improving the overall recommendation quality. This process ensures that job seekers receive tailored job recommendations that align closely with their preferences.

## K-Nearest Neighbors Architecture
When employing the K-Nearest Neighbors (KNN) algorithm for rating prediction in a recommender system, the process involves taking two essential input parameters: the specific job seeker for whom the recommendation is intended, and a job offer that the job seeker has not encountered previously. The goal is to predict the rating that the job seeker is likely to assign to the unseen job offer. The KNN algorithm operates based on the concept of finding the ”nearest neighbors” of the target job seeker among other users in the system who have similar preferences and historical interactions with job offers.

For each architecture, we used two types of recommendations:

### Content-Based Filtering
Content-based filtering relies on the content of the items being recommended, in our case, the content of the job offer. By analyzing the attributes and characteristics of each job offer, the system can match job seeker preferences with relevant content, providing personalized recommendations based on user interests and preferences.

### Neighborhood-Based Collaborative Filtering
Neighborhood-Based Collaborative Filtering leverages the behavior of others to enhance job offer recommendations. It involves seeking out individuals similar to you, or jobs similar to the ones you prefer. This process, often referred to as finding your ”neighborhood,” allows us to recommend job offers based on the preferences of others like you, guiding you towards opportunities that you haven’t explored yet. Collaborative filtering embodies the idea of collective collaboration, where insights from individuals with similar interests contribute to providing tailored and relevant job recommendations for your unique preferences.

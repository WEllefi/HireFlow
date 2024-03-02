# -*- coding: utf-8 -*-


from OfferLens import OfferLens
from surprise import KNNBasic
import heapq
from collections import defaultdict
from operator import itemgetter
        
testSubject = '85'
k = 10

# Load our data set and compute the user similarity matrix
ml = OfferLens()
data = ml.loadOfferLensLatestSmall()

trainSet = data.build_full_trainset()

sim_options = {'name': 'cosine',
               'user_based': True
               }

model = KNNBasic(sim_options=sim_options)
model.fit(trainSet)
simsMatrix = model.compute_similarities()

# Get top N similar users to our test subject
# (Alternate approach would be to select users up to some similarity threshold - try it!)
testUserInnerID = trainSet.to_inner_uid(testSubject)
similarityRow = simsMatrix[testUserInnerID]

similarUsers = []
for innerID, score in enumerate(similarityRow):
    if (innerID != testUserInnerID):
        similarUsers.append( (innerID, score) )

#the line below select the top 10 similar users and it's replaced by the code(L41=>L44)
#kNeighbors = heapq.nlargest(k, similarUsers, key=lambda t: t[1])

#the code below select only the users that are similar to t with a similarity greater than 0.80
KNeighbors = []
for user in similarUsers:
    if user[1] > (0.80):
        KNeighbors.append(user)

# Get the stuff they rated, and add up ratings for each item, weighted by user similarity
candidates = defaultdict(float)
for similarUser in KNeighbors:
    innerID = similarUser[0]
    userSimilarityScore = similarUser[1]
    theirRatings = trainSet.ur[innerID]
    for rating in theirRatings:
        candidates[rating[0]] += (rating[1] / 5.0) * userSimilarityScore
    
# Build a dictionary of job offers the candidate has already seen
rated = {}
for itemID, rating in trainSet.ur[testUserInnerID]:
    rated[itemID] = 1
    
# Get top-rated items from similar users:
pos = 0
for itemID, ratingSum in sorted(candidates.items(), key=itemgetter(1), reverse=True):
    if not itemID in rated:
        offerID = trainSet.to_raw_iid(itemID)
        print(ml.getOfferName(int(offerID)), ratingSum)
        pos += 1
        if (pos > 10):
            break



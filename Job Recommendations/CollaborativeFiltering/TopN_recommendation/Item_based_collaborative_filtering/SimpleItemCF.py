# -*- coding: utf-8 -*-


from OfferLens import OfferLens
from surprise import KNNBasic
import heapq
from collections import defaultdict
from operator import itemgetter
        
testSubject = '85'
k = 10

ml = OfferLens()
data = ml.loadOfferLensLatestSmall()

trainSet = data.build_full_trainset()

sim_options = {'name': 'cosine',
               'user_based': False
               }

model = KNNBasic(sim_options=sim_options)
model.fit(trainSet)
simsMatrix = model.compute_similarities()


testUserInnerID = trainSet.to_inner_uid(testSubject)

# Get the top K items we rated
testUserRatings = trainSet.ur[testUserInnerID]

#the line below(L33) select the top 10 similar items it's replaced by the code (L36=>L39)
#kNeighbors = heapq.nlargest(k, testUserRatings, key=lambda t: t[1])

#code below select the similar items that are rated more than 4.0 (thresholld)
kNeighbors = []
for rating in testUserRatings:
    if rating[1] > 4.0:
        kNeighbors.append(rating)
    

# Get similar items to stuff we liked (weighted by rating)
candidates = defaultdict(float)
for itemID, rating in kNeighbors:
    similarityRow = simsMatrix[itemID]
    for innerID, score in enumerate(similarityRow):
        candidates[innerID] += score * (rating / 5.0)
    
# Build a dictionary of stuff the user has already seen
rated = {}
for itemID, rating in trainSet.ur[testUserInnerID]:
    rated[itemID] = 1
    
# Get top-rated items from similar users:
pos = 0
for itemID, ratingSum in sorted(candidates.items(), key=itemgetter(1), reverse=True):
    if not itemID in rated:
        OfferID = trainSet.to_raw_iid(itemID)
        print(ml.getOfferName(int(OfferID)), ratingSum)
        pos += 1
        if (pos > 10):
            break
    



# -*- coding: utf-8 -*-


from surprise import AlgoBase
from surprise import PredictionImpossible
from OfferLens import OfferLens
import math
import numpy as np
import heapq

class ContentKNNAlgorithm(AlgoBase):

    def __init__(self, k=40, sim_options={}):
        AlgoBase.__init__(self)
        self.k = k

    def fit(self, trainset):
        AlgoBase.fit(self, trainset)

        # Compute offers similarity matrix based on content attributes

        # Load up description vectors for every job offer
        ml = OfferLens()
        descriptions = ml.getDescription()
        salaries = ml.getSalary()
        
        
        print("Computing content-based similarity matrix...")
            
        # Compute description distance for every job offer a 2x2 matrix
        self.similarities = np.zeros((self.trainset.n_items, self.trainset.n_items))
        
        for thisRating in range(self.trainset.n_items):
            if (thisRating % 100 == 0):
                print(thisRating, " of ", self.trainset.n_items)
            for otherRating in range(thisRating+1, self.trainset.n_items):
                thisOfferID = int(self.trainset.to_raw_iid(thisRating))
                otherOfferID = int(self.trainset.to_raw_iid(otherRating))
                descriptionSimilarity = self.computeDescriptionSimilarity(thisOfferID, otherOfferID, descriptions)
                salarySimilarity = self.computeSalarySimilarity(thisOfferID, otherOfferID, salaries)
                #mesSimilarity = self.computeMiseEnSceneSimilarity(thisOfferID, otherOfferID, mes)
                self.similarities[thisRating, otherRating] = descriptionSimilarity * salarySimilarity
                self.similarities[otherRating, thisRating] = self.similarities[thisRating, otherRating]
                
        print("...done.")
                
        return self
    
    #calculate consine similarity between the offers descrptions
    def computeDescriptionSimilarity(self, offer1, offer2, descriptions):
        descriptions1 = descriptions[offer1]
        descriptions2 = descriptions[offer2]
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(descriptions1)):
            x = descriptions1[i]
            y = descriptions2[i]
            sumxx += x * x
            sumyy += y * y
            sumxy += x * y
        
        return sumxy/math.sqrt(sumxx*sumyy)
    
    def computeSalarySimilarity(self, offer1, offer2, salaries):
        diff = abs(salaries[offer1] - salaries[offer2])
        sim = math.exp(-diff / 10.0)
        return sim
    

    def estimate(self, u, i):

        if not (self.trainset.knows_user(u) and self.trainset.knows_item(i)):
            raise PredictionImpossible('User and/or item is unkown.')
        
        # Build up similarity scores between this item and everything the user rated
        neighbors = []
        for rating in self.trainset.ur[u]:
            descriptionSimilarity = self.similarities[i,rating[0]]
            neighbors.append( (descriptionSimilarity, rating[1]) )
        
        # Extract the top-K most-similar ratings
        k_neighbors = heapq.nlargest(self.k, neighbors, key=lambda t: t[0])
        
        # Compute average sim score of K neighbors weighted by user ratings
        simTotal = weightedSum = 0
        for (simScore, rating) in k_neighbors:
            if (simScore > 0):
                simTotal += simScore
                weightedSum += simScore * rating
            
        if (simTotal == 0):
            raise PredictionImpossible('No neighbors')

        predictedRating = weightedSum / simTotal

        return predictedRating
    
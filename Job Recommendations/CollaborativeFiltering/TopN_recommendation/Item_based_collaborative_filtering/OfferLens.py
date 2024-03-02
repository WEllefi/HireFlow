# -*- coding: utf-8 -*-

import os
import csv
import sys
import re
import pandas as pd

from surprise import Dataset
from surprise import Reader


from collections import defaultdict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from collections import defaultdict
import numpy as np

class OfferLens:

    offerID_to_name = {}
    name_to_offerID = {}
    ratingsPath = 'rating.csv'
    offersPath = 'offers.csv'
    
    
    def loadOfferLensLatestSmall(self):

      

        ratingsDataset = 0
        self.offerID_to_name = {}
        self.name_to_offerID = {}

        reader = Reader(line_format='user item rating', sep=',', skip_lines=1)

        ratingsDataset = Dataset.load_from_file(self.ratingsPath, reader=reader)

        with open(self.offersPath, newline='', encoding='ISO-8859-1') as csvfile:
                offerReader = csv.reader(csvfile)
                next(offerReader)  #Skip header line
                for row in offerReader:
                    offerID = int(row[0])
                    offerName = row[1]
                    self.offerID_to_name[offerID] = offerName
                    self.name_to_offerID[offerName] = offerID
        # returns ratings dataset: user item rating (surpriselib data structure)           
        return ratingsDataset

    def getUserRatings(self, user):
        userRatings = []
        hitUser = False
        with open(self.ratingsPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                if (user == userID):
                    offerID = int(row[1])
                    rating = float(row[2])
                    userRatings.append((offerID, rating))
                    hitUser = True
                if (hitUser and (user != userID)):
                    break

        return userRatings

    def getPopularityRanks(self):
        #initilize two dict objects 'ratings' and 'rankings'
        ratings = defaultdict(int)
        rankings = defaultdict(int)
        with open(self.ratingsPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                offerID = int(row[1])
                ratings[offerID] += 1
        rank = 1
        for offerID, ratingCount in sorted(ratings.items(), key=lambda x: x[1], reverse=True):
            rankings[offerID] = rank
            rank += 1
        
        return rankings
    
    def getDescription(self):
        offersPath = 'offers.csv'
        df = pd.read_csv(offersPath)
        df['Job Description'] = df['Job Description'].astype(str)
        tfidf_vectorizer = TfidfVectorizer()
        job_descriptions = df['Job Description'].tolist()
        tfidf_vectors = tfidf_vectorizer.fit_transform(job_descriptions)

        tfidf_dict = {}
        for i, row in enumerate(df.iterrows()):
          job_id = row[1]['Job_Id']
          tfidf_vector = tfidf_vectors[i].toarray().tolist()[0]
          tfidf_dict[job_id] = tfidf_vector
        return tfidf_dict
    
    def getSalary(self):
        offersPath = 'offers.csv'
        df = pd.read_csv(offersPath)
        salary = defaultdict(int)
       
        #return a dict with the offerID as a KEY AND THE salary as a value
        salary = df[['Job_Id', 'salary']].set_index('Job_Id')['salary'].to_dict()
        return salary
    

    def getOfferName(self, offerID):
        if offerID in self.offerID_to_name:
            return self.offerID_to_name[offerID]
        else:
            return ""
        
    def getOfferID(self, offerName):
        if offerName in self.name_to_offerID:
            return self.name_to_offerID[offerName]
        else:
            return 0
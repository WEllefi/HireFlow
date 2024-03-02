import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math
from Transform import Transform
from Retrieve import Retrieve

class SimilarityComputing:

    transform = Transform()
    tfidf_matrix = transform.tfidfVectorize()

    retrieve = Retrieve()
    applicants = retrieve.loadApplicants()
    offer = retrieve.loadOffer()

    def computeTextSim(self):
       
        # Calculate cosine similarity
        cosine_similarities = cosine_similarity(self.tfidf_matrix[0:1], self.tfidf_matrix[1:]).flatten()

        # Create a new DataFrame with resume ID and similarity percentage
        similarity_df = pd.DataFrame({
            "Text Similarity": cosine_similarities 
        })

        # Add an index column starting from 1
        similarity_df.index = pd.RangeIndex(start=1, stop=len(similarity_df) + 1, step=1)

        # Rename the index column
        similarity_df.index.name = 'Applicant Id'
        return similarity_df

   
    def computeExperienceSimilarity(self):

        similarity_df = pd.DataFrame(columns=['Applicant Id', 'Experience Similarity'])
        
        required_experience = self.offer.at[0, 'Years of Experience']
      
        for index, row in self.applicants.iterrows():
            applicant_experience = row["Years of Experience"]
            applicant_id = row["Applicant Id"]
            diff = abs(applicant_experience - required_experience)
            sim = math.exp(-diff / 2)
            
            # Create a new DataFrame with resume ID and similarity 
            similarity_df.loc[len(similarity_df.index)] = [int(applicant_id), sim] 
        return similarity_df

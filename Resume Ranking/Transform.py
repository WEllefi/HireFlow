from sklearn.feature_extraction.text import TfidfVectorizer 
from Retrieve import Retrieve


class Transform:

    retrieve = Retrieve()
    job_offer = retrieve.getOfferDescription()
    applicants = retrieve.loadApplicants()

    def tfidfVectorize(self):
        
        # Combine job offer and resumes into a list
        documents = [self.job_offer] + self.applicants["Resume"].tolist()

        # Initialize the TF-IDF vectorizer
        vectorizer = TfidfVectorizer()

        # Compute TF-IDF matrix
        tfidf_matrix = vectorizer.fit_transform(documents)

        return tfidf_matrix
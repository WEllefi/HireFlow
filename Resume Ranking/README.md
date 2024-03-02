# Candidate Selection and Ranking System

## Introduction
In this repository, we explore the intricacies and workings of our candidate selection and ranking system. We focus on creating a robust and efficient solution to streamline the recruitment process for job offers.

## How it Works
The candidate selection process of the system commences by taking input, including the applicants and the job offer details. First of all, through a text cleaning pipeline, the job description and candidates’ resumes undergo preprocessing to eliminate irrelevant information and noise. Subsequently, the text data is transformed using the trained word2vec algorithm, yielding vectors that represent each candidate’s resume and the job offer description. These vectors share the same length and encode the semantic meaning of each resume. Using cosine similarity, the system calculates the similarity between each candidate’s resume vector and the job description vector. This similarity score reflects the degree to which a candidate’s resume aligns with the specified job description. Simultaneously, the system computes the similarity between each candidate’s years of experience and the required job experience, producing a similarity value between 0 and 1. The equation to do this task is given by: f(x1, x2) = exp(|x1 − x2| / 3). In this equation, x1 represents the job offer’s required experience, while x2 represents the candidate’s number of years of experience. The function f(x1, x2) gives a measure of compatibility, with higher values indicating a closer match between the job requirements and the candidate’s experience. The system then ranks the candidates based on their combined similarity scores and presents the top N candidates that best match the job offer’s requirements. By leveraging advanced text analysis and semantic understanding, the system efficiently identifies the most suitable candidates, significantly streamlining the candidate selection process for recruiters. The integration of text-based similarity and experience relevance ensures that the selected candidates closely align with the specific job offer, optimizing the likelihood of successful job placements.

## Code Structure
- **CleaningPipeline**: Focuses on text preprocessing, removing stop words, stemming, and tokenization to prepare both job descriptions and candidates’ resumes for analysis.
- **Retrieve**: Loads raw data into a pandas dataframe and applies the text cleaning pipeline.
- **Word2Vec Transformation**: Converts textual data into dense vectors using a trained word embeddings model.
- **SimilarityComputation**: Computes text similarity scores between job descriptions and candidates’ resumes, as well as similarity based on years of experience.
- **GetTopN**: Aggregates text similarity and experience relevance scores to generate a holistic ranking for each candidate.

## Configuration
A YAML configuration file is provided to customize the number of candidates retrieved, denoted as N. This file allows recruiters to adjust the candidate selection process without altering the codebase.


# HireFlow 
This Project aims to improve the recruitment process using a data-driven solution. :briefcase: </br>
## Description of the Project

In the realm of the recruitment industry, the prevailing methodologies exhibit limitations in effectively managing extensive datasets. These approaches necessitate manual intervention for the screening and assessment of resumes, resulting in a protracted and inefficient procedure. As the volume of candidates escalates, the recruitment team grapples with the challenge of retaining comprehensive insights into each individual applicant. Conversely, job seekers invest substantial time in identifying employment opportunities that align with their profiles.

This project illuminates the transformative potential of artificial intelligence in mitigating these challenges. By harnessing the power of AI and Data Analysis, the time investment required for evaluating a candidate’s profile by HR personnel can be significantly curtailed from an average of approximately 7 minutes to a task seamlessly executed by artificial intelligence. This transition not only expedites the evaluation process but also streamlines it into an automated workflow.

Moreover, this research delves into the augmentation of job seekers’ experiences through the implementation of recommendation and matching algorithms. By leveraging these advanced algorithms, the likelihood of identifying fitting job opportunities is substantially enhanced. Consequently, job seekers are empowered to navigate the employment landscape more efficiently and with a heightened probability of securing positions that harmonize with their qualifications and aspirations.

In summation, this project demonstrates the efficacy of integrating artificial intelligence and data analysis into the recruitment domain to revolutionize candidate evaluation, optimize resource utilization, and amplify the efficacy of job matching for enhanced outcomes.

## What Does This Project Provides

This project provides three main services:

1. **AI-Based Candidate Selection:** An AI-based solution that selects the top *n* candidates that match the job requirements. This service helps recruiters streamline the candidate selection process and focus on the most suitable candidates.

2. **Interactive Dashboard:** An interactive dashboard that helps recruiters gain insights and information about the candidates. The dashboard provides visualizations and analytics to aid in decision-making and candidate evaluation.

3. **Robust Recommender System:** A robust recommender system that helps candidates find the most suitable job offers. The system uses machine learning algorithms to recommend job offers based on the candidate's skills, experience, and preferences.

## Installation instructions

**Installation Requirements**

This project is a comprehensive system consisting of several components. To run it, you will need to install the following:

### Python Libraries
- Python 3.x
- SurpriseLib 1.x
- PySpark 2
- Pandas
- NLTK

You can install Python libraries using pip. For example: </br>
pip install surpriselib

### Data Integration and Dashboard Tools
- Talend Open Studio version 8
- MySQL 8
- Power BI (latest version)

## Data Sources

It is important to note that the data utilized in this project is publicly available and obtained
from reliable sources on the Internet. The decision to use public data stems from the need to work with real-world information that
is accessible to the wider research community. By utilizing publicly available data, we ensure
that the findings and insights derived from our analysis can be validated and reproduced by
others in the field.

To gain a deeper understanding of the data, we will conduct an Exploratory Data Analysis
(EDA). Through EDA, we aim to uncover valuable insights, detect outliers, understand the distribution
of variables, and identify any missing or inconsistent values.

The data used in this project can be categorized into two main data sets: job offer data and job
seeker data.

The job offer data provides insights into the various job opportunities available in the market.
It includes details such as the location of the job, job titles, descriptions, salary ranges,
required experience, and other relevant attributes. This data is sourced from reputable job portals,
industry-specific websites such as Glassdoor, LinkedIn, and Indeed.

On the other hand, job seeker data focuses on individuals seeking employment. This data
encompasses information related to job seekers, including their resumes, job titles, fields of
expertise, age, salary expectations, and other pertinent details. The job seeker data is typically
sourced through surveys or online profiles. Analyzing this data provides insights into the characteristics,
preferences, and qualifications of job seekers, allowing us to match their profiles with suitable job opportunities.

By dividing the data into these two major data sets, we can effectively analyze and address
the needs of both job seekers and employers. Understanding the job offer data enables us to
provide personalized job recommendations to job seekers based on their qualifications, preferences,
and the specific requirements of available job opportunities. Simultaneously, the job
seeker data helps us assess the profiles and qualifications of candidates and assists recruiters in
identifying the most suitable candidates for their job openings.

## Code Structure

This project is organized into four major folders or repositories:

1. **Recommender Systems:** This folder contains several recommender systems employed for our needs and their designs. These systems are used to recommend job offers to job seekers based on their qualifications and preferences.

2. **Resume Ranking:** The `resume_ranking` folder contains the project that helps recruiters analyze candidates' resumes and select the most qualified ones. This project likely involves machine learning models to rank resumes based on their relevance to job requirements.

3. **Dashboard:** The `dashboard` folder contains the files related to the interactive dashboard that provides insights and information about the candidates. This dashboard helps recruiters visualize data and make informed decisions.

4. **Word2Vec Preprocessing:** This folder contains an important phase of preprocessing, which is the `word2vec` using `gensim`. In this phase, we create a database of vectors based on data related to jobs that we already have. This database of vectors is used in the recommender systems to match job seekers with suitable job offers.


## Results and Evaluation

Each system in this project is evaluated separately, and the evaluation results are discussed in their respective repositories. Below is a summary of the evaluation process for each component:

1. **Recommender Systems:** The recommender systems are evaluated based on their ability to recommend relevant job offers to job seekers. Metrics such as precision, hit rate, and diversity are used to assess the performance of each recommender system.

2. **Resume Ranking:** The resume ranking system is evaluated on its effectiveness in ranking resumes based on their relevance to job requirements.

3. **Dashboard:** The dashboard is evaluated based on its usability and the insights it provides to recruiters. User feedback and usability tests are conducted to assess the effectiveness of the dashboard in helping recruiters make informed decisions.

4. **Word2Vec Preprocessing:** The word2vec preprocessing phase is evaluated based on the quality of the word embeddings generated. Metrics such as cosine similarity and word analogy tests are used to evaluate the quality of the word embeddings.

By evaluating each component separately, we can gain a comprehensive understanding of the strengths and weaknesses of each system and identify areas for improvement.

# Project Overview

For a comprehensive understanding of this project and the research behind it, please refer to the full report (thesis) named [Wissem_Ellefi_Thesis.pdf](WEllefi/HireFlow/Wissem_Ellefi_Thesis.pdf).

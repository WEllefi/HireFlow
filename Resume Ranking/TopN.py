from SimilarityComputing import SimilarityComputing
import pandas as pd
from Config import cfg
from Retrieve import Retrieve

retrieve = Retrieve()
retrieve.loadApplicants()


sim = SimilarityComputing()

df1 = sim.computeTextSim()

df2 = sim.computeExperienceSimilarity()

# Merge the two data frames on "Applicant Id" using an outer join
merged_df = pd.merge(df1, df2, on="Applicant Id", how="outer")
    
# Multiply the similarity scores and store the result in a new column
merged_df["Similarity"] = merged_df["Experience Similarity"] * merged_df["Text Similarity"]
    
# Fill missing similarity values with 0
merged_df["Similarity"].fillna(0, inplace=True)
    
# Select only the "Applicant Id" and "Similarity" columns
result_df = merged_df[["Applicant Id", "Similarity"]]
result_df['Applicant Name'] = result_df['Applicant Id'].apply(retrieve.getApplicantName)
print(result_df.sort_values("Similarity", ascending=False).head(cfg.topN.N))
from Retrieve import Retrieve
from SimilarityComputing import SimilarityComputing
import pandas as pd


'''retrieve = Retrieve()


applicants = retrieve.loadApplicants()
print(applicants)
offer = retrieve.loadOffer()  
print(offer)'''

sim = SimilarityComputing()


print(sim.computeTextSim())
df1 = sim.computeTextSim()

df2 = sim.computeExperienceSimilarity()

#df2['Applicant Id'] = df2['Applicant Id'].astype(int)

print(df2)




# Merge the two data frames on "Applicant Id" using an outer join
merged_df = pd.merge(df1, df2, on="Applicant Id", how="outer")
    
# Multiply the similarity scores and store the result in a new column
merged_df["Similarity"] = merged_df["Experience Similarity"] * merged_df["Text Similarity"]
    
# Fill missing similarity values with 0
merged_df["Similarity"].fillna(0, inplace=True)
    
# Select only the "Applicant Id" and "Similarity" columns
result_df = merged_df[["Applicant Id", "Similarity"]]

print(result_df.sort_values("Similarity", ascending=False))

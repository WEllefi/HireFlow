import pandas as pd
from Config import cfg
from Clean import Clean

class Retrieve:

    
    clean = Clean()
    applicantID_to_name = {}
    name_to_applicantID = {}

    offerPath = cfg.data.path.offerPath
    applicantsPath = cfg.data.path.applicantsPath

    def loadOffer(self):
        df = pd.read_csv(self.offerPath)
        df["Job Description"] = df["Job Description"].apply(self.clean.cleanTextPipeline)
        #return pd.read_csv(self.offerPath)
        return df
    
    def loadApplicantRaw(self):
        return pd.read_csv(self.applicantsPath)
    
    def loadApplicants(self):
        self.applicantID_to_name = {}
        self.name_to_applicantID = {}
        applicants = pd.read_csv(self.applicantsPath)
        #applicants["Resume"] = applicants["Resume"].apply(self.clean.cleanTextPipeline)

        for index, row in applicants.iterrows():
            # Extract the applicant ID, name, and last name from the row
            applicant_id = row[cfg.data.column_name.applicant_id]
            applicant_name = row[cfg.data.column_name.applicant_first_name]
            applicant_last_name = row[cfg.data.column_name.applicant_last_name]
    
            # Concatenate the name and last name to get the full name
            full_name = f"{applicant_name} {applicant_last_name}"
            
            # Add the entry to the dictionary
            self.applicantID_to_name[applicant_id] = full_name
            self.name_to_applicantID[full_name] = applicant_id

        return applicants
    
    def getApplicantResume(self, applicant_index):
   
        df = pd.read_csv(self.applicantsPath)
        try:
            cell_value = df.loc[applicant_index-1, cfg.data.column_name.resume]
        except IndexError:
            print("Index is out of range! this is the last candidate resume:")
            cell_value = df.loc[ len(df)-1, cfg.data.column_name.resume]
        except Exception as e:
            print("An error occurred! this is the last candidate resume:")
            cell_value = df.loc[len(df)-1, cfg.data.column_name.resume]
        return cell_value

    def getOfferDescription(self):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(self.offerPath)

        # Access the specific cell at row index 0 and column 'Job Description'
        cell_value = df.loc[0, cfg.data.column_name.offer_description]
        return cell_value

    def getApplicantName(self, applicantID):
        self.loadApplicants()
        if applicantID in self.applicantID_to_name:
            return self.applicantID_to_name[applicantID]
        else:
            return r"applicant doesn't exist!"
        
    def getApplicantID(self, applicantName):
        if applicantName in self.name_to_applicantID:
            return self.name_to_applicantID [applicantName]
        else:
            return -1
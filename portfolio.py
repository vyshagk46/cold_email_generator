import pandas as pd

# class Portfolio:
#     def __init__(self, path="portfolio.csv"):
#         self.df = pd.read_csv(path)

#     def retrieve(self, skills):
#         if not skills:
#             return []
#         return self.df[self.df["skills"].str.contains("|".join(skills), case=False, na=False)] \
#                       .to_dict(orient="records")

class Portfolio:
    def __init__(self, path="portfolio.csv"):
        self.df = pd.read_csv(path)

    def retrieve(self, extracted_skills):
        extracted_skills = set(s.lower() for s in extracted_skills)

        results = []
        for _, row in self.df.iterrows():
            project_skills = set(
                s.strip().lower() for s in row["skills"].split(",")
            )

            score = len(extracted_skills & project_skills)
            if score > 0:
                results.append({
                    "project": row["project_name"],
                    "skills": row["skills"],
                    "description": row["description"],
                    "match_score": score
                })

        return sorted(results, key=lambda x: x["match_score"], reverse=True)

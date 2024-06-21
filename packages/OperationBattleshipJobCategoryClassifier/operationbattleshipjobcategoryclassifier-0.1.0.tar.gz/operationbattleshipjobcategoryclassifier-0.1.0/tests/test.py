from JobCategoryClassifierBertInference import JobCategoryClassifierBertInference as JobCategoryClassifierBert
#Example usage:
s3_url = "https://operationbattleship-resumes.nyc3.cdn.digitaloceanspaces.com/BERT/BERT.zip"
classifier = JobCategoryClassifierBert(s3_url)
job_title = "Software Engineer"
predicted_category = classifier.predict(job_title)
print(f"Predicted Job Category: {predicted_category}")
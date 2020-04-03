This is my first project using airflow.

### What it does
* Get a sample of the most recent tweets in English language
* Use Latent Dirichlet Allocation to model topics and extract most significant words / word tokens
* Upload result as json file to an S3 bucket

### Prerequisites
* Twitter dev account
* Existing AWS S3 Bucket

### Configuration
Place an .env file in dags/topics/ containing the following env variables:
* TWITTER\_CONSUMER\_KEY
* TWITTER\_CONSUMER\_SECRET
* TWITTER\_ACCESS\_TOKEN
* TWITTER\_ACCESS\_TOKEN\_SECRET
* TWITTER\_SAMPLE\_SIZE (optional)
* LDA\_NUM\_TOPICS (optional)
* LDA\_NUM\_TOP\_WORDS (optional)
* S3\_ACCESS\_KEY
* S3\_SECRET\_KEY
* S3\_BUCKET
* AIRFLOW\_SCHEDULE (optional)


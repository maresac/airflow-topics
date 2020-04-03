This is my first project using airflow.

### What it does
* Get a sample of the most recent tweets in English language
* Use Latent Dirichlet Allocation to model topics and extract most significant words / word tokens
* Upload result as json file to an S3 bucket

### Prerequisites
* Twitter dev account
* Existing AWS S3 Bucket

### Configuration
Place an `.env` file in `dags/topics/` containing the following env variables:
* `TWITTER_CONSUMER_KEY`
* `TWITTER_CONSUMER_SECRET`
* `TWITTER_ACCESS_TOKEN`
* `TWITTER_ACCESS_TOKEN_SECRET`
* `TWITTER_SAMPLE_SIZE` (optional)
* `LDA_NUM_TOPICS` (optional)
* `LDA_NUM_TOP_WORDS` (optional)
* `S3_ACCESS_KEY`
* `S3_SECRET_KEY`
* `S3_BUCKET`
* `AIRFLOW_SCHEDULE` (optional)

### Usage
* Run `pip install -r requirements.txt` first
* Set `AIRFLOW_HOME` to your project path
* Get airflow up and running:
  * `airflow initdb`
  * `airflow scheduler`
  * `airflow webserver -p 8080`
* Run tasks separately:
  * `airflow test airflow-topics extract_tweets $(date +%F)`
  * `airflow test airflow-topics dump_topics $(date +%F)`
  * `airflow test airflow-topics push_results $(date +%F)`
* Alternatively:
  * `airflow trigger_dag airflow-topics`

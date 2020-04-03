import twitter

from .config import settings


def extract_tweets(**context):
    api = twitter.Api(
        consumer_key=settings.twitter.consumer_key,
        consumer_secret=settings.twitter.consumer_secret,
        access_token_key=settings.twitter.access_token,
        access_token_secret=settings.twitter.access_token_secret,
    )

    sample_size = context["sample_size"]
    samples = []

    for line in api.GetStreamSample(stall_warnings=True):
        if "text" in line and line["lang"] == "en":
            samples.append(line["text"])

        if len(samples) == sample_size:
            break

    return samples

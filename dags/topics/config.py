from dotenv import load_dotenv
import environ


@environ.config(prefix=None)
class Config(object):
    @environ.config
    class Twitter(object):
        consumer_key=environ.var()
        consumer_secret=environ.var()
        access_token=environ.var()
        access_token_secret=environ.var()

    twitter = environ.group(Twitter)

    @environ.config
    class LDA(object):
        num_topics=environ.var(10, converter=int)
        num_top_words=environ.var(20, converter=int)

    lda = environ.group(LDA)

    @environ.config
    class S3(object):
        access_key=environ.var()
        secret_key=environ.var()

    s3 = environ.group(S3)

    sample_size = environ.var(5000, converter=int)

load_dotenv()

settings = environ.to_config(Config)
twitter = settings.twitter
lda = settings.lda
s3 = settings.s3


import json

from nltk import TweetTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

from .config import lda as settings


LANGUAGE = "english"
PUNCTUATION = [".", ",", '"', "'", "?", "!", ":", ";", "(", ")", "[", "]", "{", "}", "’", "”", "...", "-", "/", "$", "&", "*"]

stop_words = set(stopwords.words(LANGUAGE))
stop_words.update(PUNCTUATION)
stop_words.update(["rt"])


def dump_topics(**context):
    file_name = context["filename"]
    tweets = context["task_instance"].xcom_pull(task_ids="extract_tweets")
    topics = _extract_topics(tweets)
    with open(file_name, "w+") as f:
        json.dump(topics, f)
    return file_name


def _extract_topics(tweets):
    tokenizer = TweetTokenizer(
        preserve_case=False,
        reduce_len=True,
        strip_handles=True,
    )

    vectorizer = CountVectorizer(
        tokenizer=tokenizer.tokenize,
        stop_words=stop_words,
        strip_accents="unicode",
    )
    features = vectorizer.fit_transform(tweets)
    words = vectorizer.get_feature_names()

    lda = LatentDirichletAllocation(n_components=settings.num_topics)
    lda.fit(features)

    top_words = [_get_top_words(words, t, settings.num_top_words) for _, t in enumerate(lda.components_)]
    return {i: w for i, w in enumerate(top_words)}


def _get_top_words(words, topic, num_top_words):
    return [words[i] for i in topic.argsort()[:-num_top_words - 1:-1]]

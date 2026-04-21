import json
import nltk
import string

# download nltk data
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))


def preprocess(text):
    """
    Cleans and normalizes a phrase:
    1. lowercase
    2. remove punctuation
    3. tokenize into words
    4. remove stopwords
    5. stem each word
    """
    # make it lowercase
    text = text.lower()

    # remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # tokenize
    tokens = word_tokenize(text)

    # remove stopwords and stem
    tokens = [stemmer.stem(t) for t in tokens if t not in stop_words]

    return " ".join(tokens)


def load_training_data(path="intents.json"):
    """
    Loads intents.json and returns two lists:
    - X: preprocessed example phrases
    - y: corresponding intent tags
    """
    with open(path, "r") as f:
        data = json.load(f)

    X, y = [], []
    for intent in data["intents"]:
        for example in intent["examples"]:
            X.append(preprocess(example))
            y.append(intent["tag"])

    return X, y


# quick test
if __name__ == "__main__":
    print(preprocess("What is your name?"))
    print(preprocess("Tell me a funny joke!"))

    X, y = load_training_data()
    print(f"\nLoaded {len(X)} training examples across {len(set(y))} intents")
    for phrase, label in list(zip(X, y))[:5]:
        print(f"  [{label}] {phrase}")
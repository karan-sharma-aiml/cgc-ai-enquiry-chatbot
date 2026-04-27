import re
# text cleaning and preprocessing for NLP tasks
# Stopwords (common useless words)
stopwords = ["kya", "hai", "ka", "ki", "ke", "the", "is", "are", "a", "an"]

# Step 1: Clean text
def clean_text(text):
    text = text.lower()  # lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # remove symbols
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return text

# Step 2: Remove stopwords
def remove_stopwords(text):
    words = text.split()
    filtered_words = []

    for word in words:
        if word not in stopwords:
            filtered_words.append(word)

    return " ".join(filtered_words)

# Final function (use this in project)
def preprocess(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    return text
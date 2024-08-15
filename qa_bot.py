from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading the scraped data
with open('scraped_data.txt', 'r', encoding='utf-8') as file:
    data = file.read()

sentences = data.split('. ')

# Function to find the best answer based on cosine similarity
def get_answer(question, sentences):
    corpus = [question] + sentences
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    
    similarities = cosine_similarity(X[0:1], X[1:])
    
    best_idx = similarities.argmax()
    
    return sentences[best_idx]

# Example usage
question = "Who are the founders of Mercedes Benz?"
answer = get_answer(question, sentences)
print("Question:", question)
print("Answer:", answer)

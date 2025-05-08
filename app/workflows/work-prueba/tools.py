from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

class DocumentProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
    
    def __call__(self, document):
        # Tokenize the document
        words = word_tokenize(document)
        
        # Remove stopwords
        words = [word for word in words if word not in self.stop_words]
        
        return " ".join(words)

class DocumentSummarizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
    
    def __call__(self, document):
        # Tokenize the document into sentences
        sentences = sent_tokenize(document)
        
        # Vectorize the sentences
        tfidf_matrix = self.vectorizer.fit_transform(sentences)
        
        # Compute the similarity matrix
        sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        # Rank the sentences
        sentence_rank = np.argsort(np.sum(sim_matrix, axis=1))[::-1]
        
        # Get the top 3 sentences
        summary = " ".join([sentences[i] for i in sentence_rank[:3]])
        
        return summary
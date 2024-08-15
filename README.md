# Merc-Project

This is a simple Question-Answering (QA) chatbot application built using Python. The chatbot extracts and scrapes text data from a Wikipedia page, processes the data using TF-IDF vectorization, and answers user queries based on the scraped content. The project uses Flask for the web interface, BeautifulSoup for web scraping and scikit-learn for machine learning.

Web Interface: The chatbot has a simple web interface where users can ask questions and receive answers based on the content from a specified Wikipedia page.
No Pre-Trained LLMs: The chatbot does not rely on pre-trained LLMs or external APIs. It is built from scratch using a dataset scraped from a Wikipedia page.
Custom Dataset: The bot scrapes, cleans and processes text data from a specified Wikipedia page, which is then used to train the model.
Flask API: The application is hosted using Flask, making it easy to deploy the web interface.

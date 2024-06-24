from setuptools import setup, find_packages
setup(
name='semantic_text_search_word_disambiguation',
version='0.1.1',
author='Sastry K V S R',
author_email='sivaram.kavuri@gmail.com',
description='A package to create a semantic search word disambiguation functionality with vector db, NER, POS, Lemmatization support',
packages=(find_packages() +
          find_packages(where="langchain") +
          find_packages(where="langchain-community") +
          find_packages(where="sentence-transformers") +
          find_packages(where="faiss-cpu") +
          find_packages(where="transformers") +
          find_packages(where="nltk")
),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)

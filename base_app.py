"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    -------------------------------------------------https://docs.streamlit.io/en/stable/api.html#magic-commands
    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/



"""
# Streamlit dependencies
from matplotlib import matplotlib_fname
from numpy.lib.function_base import _meshgrid_dispatcher
import streamlit as st
import joblib, os
from PIL import Image
import altair as alt
#import  graphviz as graphviz

import time

import seaborn as sns
# Data dependencies
import pandas as pd
#matplotlib_fname. use("Agg")
import matplotlib.pyplot as plt

# Vectorizer
news_vectorizer = open("resources/SVR_clf.pkl","rb")
news_vectorizer = open("resources/lr_clf.pkl","rb")
tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("resources/train.csv")



# The main function where we will build the actual app
def main():
	# Creates a main title and subheader on your page -
	# these are static across all pages
	st.title("Welcome to our Tweet Classifier Project")
	st.subheader("Climate change tweet classification")
	

	# Creating sidebar with selection box -
	# you can create multiple pages this way",
	options = ["Prediction", "Information", "Introduction", "Data analysis and Data  visualizations", "Model Explanation", "Presentation"]
	selection = st.sidebar.selectbox("Choose Option", options)

#building out the Information page
	if selection == "Introduction":
		st.image("Image.jpeg")
	
	if selection == "Data analysis and Data  visualizations":
		#st.info("Exploratory Data Analysis")
		if st.checkbox('Mentions'):
			#st.image(#"NegetiveTags.png")
			st.image("positivetags.png")
			st.image("TopNeutral.png")
			st.image("TopNews.png")

		if st.checkbox('Tweet length'):
			st.image("Pieplot.png")
			st.image("sentme.png")
			
			
			st.image("Tweets.png")
			st.image("Avaragetext.png")
			st.image("map.png")
		

	# Building out the "Information" page
	if selection == "Information":
		st.info("General Information")
		# You can read a markdown file from supporting resources for feature engineering to be usable. As for the integer variables, little to no 
		
		
	
		
		
		
		
		
		
	
		st.subheader("resources/train.csv")
		if st.checkbox("test_with_no_labels.csv"): # data is hidden if box is unchecked
			st.write(raw[['sentiment', 'message']]) # will write the df to the page

	# Building out the predication page
	#if st.button("Models"):
		

	if selection == "Prediction":
		st.info("Prediction with ML Models")
		# Creating a text box for user input
		tweet_text = st.text_area("welcome","Type Here")

		if st.button("Classify"):
			# Transforming user input with vectorizer
			#st.text_area("Real test ::/n{}". format(text_area))
			#tweet_text= _msg_clean[col].apply(clean_data)
			vect_text = tweet_cv.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
		#if ML_Model	== "SVC":
			predictor = joblib.load(open(os.path.join("resources/SVC_clf.pkl"),"rb")
			prediction = predictor.predict(vect_text)
		#if ML_Model == "LR":
			predictor = joblib.load(open(os.path.join("resources/lr_clf.pkl"),"rb"))
			prediction = predictor.predict(vect_text)




			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
		if prediction == 0:
			results ="neutral"
		if prediction == 1:
		 results = "positive"
		if prediction ==0:
			results='negetive'
			st.success("Text Categorized as: {}".format(prediction))

# Required to let Streamlit instantiate our web app. 
if __name__ == '__main__':
	main()

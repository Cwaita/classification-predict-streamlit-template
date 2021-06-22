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
news_vectorizer = open("resources/tfidfvect.pkl","rb")
tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("resources/train.csv")
#if raw  == pd.DataFrame(np.random(50, 2), columns= ('col %d' % i in range (2))
    #.dataframe (raw)
	#st.table(raw)
	#st.markdown('here we be displaying our distrubution using matplotlib libraries') 
#if raw =np.random.normal(1,1, size=100):
	#ax.hist(raw, bin= 20)
	#st.pyplot(fig)


# The main function where we will build the actual app
def main():
	# Creates a main title and subheader on your page -
	# these are static across all pages
	st.title("Welcome to our Tweet Classifier Project")
	st.subheader("Climate change tweet classification")
	st.image("Image.jpeg")

#def main(train):
	# Creating sidebar with selection box -
	# you can create multiple pages this way",
	options = ["Prediction", "Information", "Introduction", "Data anlysis and Data  visualizations ", "Model Explanation", "Presentation"]
	selection = st.sidebar.selectbox("Choose Option", options)
	if selection == "Data anlysis and Data  visualizations":
		st.info	("Exploratory Data Analysis")
		raw = st.file_uploader("resources/train.csv", type= ["csv"])
		if raw is None:

			train= pd.read_csv(raw)

		st.dataframe(train.head())
		if st.checkbox("Show Shape"):


			st.write(train.shape)


			if st.checkbox("Show Columns"):
				all_columns = train.columns.to_list()
				st.write(all_columns)


			if st.checkbox("Show  Selected Column"):

				selected_columns = st.multselect("Select columns",  all_columns)

				new_df = train[selected_columns]

				st.dataframe(new_df)

	        #if st.checkbox("Summary"):

			    #st.write(train.describe())

		if st.checkbox("Show Value Counts"):
				st.write(train.iloc[:, -1].value_counts())

		if st.checkbox("Correlation Plot(Matplotlib)"):
			plt.matshow(train. corr())
			st.pyplot()

		if st.checkbox("Pie Plot"):
			all_columns = train.columns.to_list()
			column_to_plot = st.selectbox("sentiment",all_columns)
			pie_plot = df[column_to_plot].value_count().plot.pie(autopct = "1.1f%%")
			st.write(pie_plot)
			st.pyplot()

	elif selection == 'Plots':
		st.subheader('Data Visualisation')
		raw = st.file_uploader("resources/train.csv", type= ["csv"])
		if raw is not None:
			pd.read_csv(raw)
			st.dataframe(train.head())

			if st.checkbox("Show Value Counts"):
				st.write(df.iloc[:, -1].value_counts().plot(kind = "bar"))
				st.pyplot()

		#Customize Plot	
		all_columns_names =train.columns.tolist()
		type_of_plot= st.selectbox("Select Type of plot",['area', 'bar', 'line', 'hist', 'box', 'kde'])
		selected_columns_names = st.multiselect ("Select Columns To Plot, all_columns_names ")


		if st.button("Generate Plot"):
			st.success("Generate Customizable Plot of {} for {} ". format(type_of_plot, selected_columns_names))

		#Plot BY Streamlit 	
		if type_of_plot =='area':
			cust_data = train[selected_columns_names]
			st.area_chart(cust_data)


		elif type_of_plot =='line':
			cust_data = train[selected_columns_names].plot(kind= type_of_plot)
			st.line_chart(cust_data)
		elif type_of_plot =="bar":
			cust_data = train[selected_columns_names]
			st.bar_chart(cust_data)
		#Custom Plot
		elif type_of_plot:
			cust_plot =train[selected_columns_names].plot(kind= type_of_plot)
			st.write(cust_plot)
			st.pyplot()	

			
	#st.markdown("In statistics exploratory data analysis is an approach of analyzing data sets to summarize their main characteristics often using statistical graphics and other data visualization methodsIn statistics")



	# Building out the "Information" page
	if selection == "Information":
		st.info("General Information")
		# You can read a markdown file from supporting resources folder
		st.markdown("The train dataset given consists of object and integer variables. The object variable (message column) requires cleaning and/or feature engineering to be usable. As for the integer variables, little to no cleaning needs to be done as there are little to no issues with them in this dataset. In total, there are 3 columns/variables. The first column/variable  will be used as our response variable (sentiment)")

		st.subheader("Raw Twitter data and label")
		if st.checkbox('Show raw data'): # data is hidden if box is unchecked
			st.write(raw[['sentiment', 'message']]) # will write the df to the page

	# Building out the predication page
	if selection == "Prediction":
		st.info("Prediction with ML Models")
		# Creating a text box for user input
		tweet_text = st.text_area("Enter Text","Type Here")

		if st.button("Classify"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))

# Required to let Streamlit instantiate our web app. 
if __name__ == '__main__':
	main()

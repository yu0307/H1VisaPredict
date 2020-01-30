# H1VisaPredict
This is a short python program that uses linear regression to fit the data(H1 Visa processing time) and to predict the amount of time one has to wait to get their visa approved. 

# Data Files: 

1. VISA.xlsx is the original data collected from a website that keeps track of individual application case. It is also the file used by Analyze.py to get a general description of the data. 

2. Analysis.xlsx is the normalized(intermediate) data file that we need to convert into something we can work with.

3. export_dataframe.csv (Label) is the output from the converter file, and is also what we used to train the model.

4. Test.cvs is the testing data set to evaluate the prediction.

5. My_solution.csv is the result (output) from the prediction.

# Program Files:
- Convert.py will take the data file and convert non-numerical data into something we can work with and build a dictionary to store converted data. 
- Analyze.py will take the Original data and generate a descriptive representation. 
- Predict.py will take both trainning data and testing data to train the model as well as produce result base on the testing data. 

# This project was really something I'd do to pass time. I will be glad if it could really help someone :)

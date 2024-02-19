import pandas as pd
data=pd.read_csv("housing_data.csv")
print(data)
#Creating own dataframe
d={'Cars':['Porsche','Ferrari','Thar','Tesla'],'Speed':[100,200,170,180]}
print(type(d))
d=pd.DataFrame(d)
print(d)
print(d.shape)

# Data Anaytics Process
'''
1. Bussiness Problem: Process of Analytics begins with questions or business problems for stakeholders.
2. Data Acquisition: Collect data from various sources for analysis to answer questions raised in step 1.
3. Data Wrangling and Exploration: Data Wrangling includes data cleaning and data manipulation whereas data exploration includes data discovery and data pattern.
   Data Wrangling Challenges:
   -> Unexpected Data Format
   -> Errorneous Data
   -> Volumous Data to be manipulated
   -> Classifying Data into linear or clusters
   
   Data Exploration:Model Selection
   -> Based on overall data analysis process
   -> Should be accurate to avoid iterations
   -> Depends on pattern identification and algorithm
   
5. EDA(Exploratory Data Analysis):
   -> Studies the data to recommend suitable model that best fits the data
   EDA: Quatitative Technique
   Measurement of Central Tendency
   -> Mean: Suitable for symmetric distributions
   -> Median: Suitable for skewed distributions and for catching outliers in the dataset.
   -> Mode: Mode common value in the data
   
   EDA: Graphical technique-> Histograms and Scatter Plotts are most used techniques
   
6. Conclusions and Predictions: Reaching a conclusion and making predictions based on data Analysis.
7. Communications 
    
    
    # Types of Plots
    1. Histograms
    2. Heat Map  - continuous
    3. Line Chart - continuous
    4. Regression Plot
    5. Cluster Map
8.Hypothesis testing -> Training data set
'''
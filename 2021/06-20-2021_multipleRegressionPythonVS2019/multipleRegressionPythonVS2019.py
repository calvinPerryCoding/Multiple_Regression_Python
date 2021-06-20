import pandas as pd
import numpy as np
from sklearn import linear_model

#Right now there is no user input besides the questions
#FUTURE UPDATE: USER INPUT
df = pd.read_csv("sampleProductData.csv")
#FUTURE UPDATE: change fields for your csv file
X = df[["Age", "Gender", "Season", "Parent", "Education", "Salary"]]
#If you get an error message try adding/removing a space before or after
y = df["Buy Product"]
#FUTURE UPDATE: DO NOT CHANGE ANYTHING PAST THIS POINT UNLESS YOU ARE THE DEVELOPER

regr = linear_model.LinearRegression()
regr.fit(X, y)

print("\n\nThis program will predict how likely a customer will buy Halloween candy\n\n")

#while True:
#do stuff here
#if condition 
#break
while True:
    print("Enter Age:")
    field1 = input()
    print("Enter Gender:")

    print("0 = Female")
    print("1 = Male")
    field2 = input()

    print("Enter Season:")
    print("0 = Winter")
    print("1 = Spring")
    print("2 = Summer")
    print("3 = Fall")
    field3 = input()

    print("Is the customer a parent?")
    print("0 = No")
    print("1 = Yes")
    field4 = input()

    print("Enter the customer's education:")
    print("0 = HS Dropout")
    print("1 = HS Diploma/GED")
    print("2 = Certification")
    print("3 = Associate")
    print("4 = Bachelor")
    print("5 = Master")
    print("6 = Doctor")
    field5 = input()

    print("Enter the customer's salary:")
    print("0 = Poor Less Than $30,000")
    print("1 = Average $30,000 To $60,000")
    print("2 = Wealthy More Than $60,000")
    field6 = input()

    predictedValue = regr.predict([[field1, field2, field3, field4, field5, field6]])

    rounded = np.round(predictedValue, 0) 

    if rounded >= 1:
        print("\n\nCustomer WILL Buy Product\n")

    elif rounded <= 0:
        print("\n\nCustomer WILL NOT Buy Product\n")

    answerLoop = input("\nPress y to run again or press any key to exit\n")

    if answerLoop != "y":
        break

# References APA 7th Edition


# W3schools. (n.d.). Python machine learning multiple regression. W3Schools Online Web Tutorials. https://www.w3schools.com/python/python_ml_multiple_regression.asp
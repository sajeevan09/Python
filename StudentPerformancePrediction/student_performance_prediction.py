import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Sample Dataset 
data = {
    'Hours_Studied': [1,2,3,4,5,6,7,8,9,10],
    'Attendance': [60,65,70,75,80,85,90,95,97,100],
    'Test_Score': [50,55,60,65,70,75,80,85,90,95],
    'Passed': [0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# Split data into inputs (X) and output (y)
X = df[['Hours_Studied', 'Attendance', 'Test_Score']]
y = df['Passed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Predict a new student
new_student = pd.DataFrame({'Hours_Studied':[7], 'Attendance':[88], 'Test_Score':[82]})
prediction = model.predict(new_student)
print("\nPredicted Result for new student:", "Pass" if prediction[0]==1 else "Fail")

# Visualize data
plt.scatter(df['Hours_Studied'], df['Test_Score'], c=df['Passed'], cmap='bwr')
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.title("Student Performance (Blue = Fail, Red = Pass)")
plt.show()

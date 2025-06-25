from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load diabetes dataset
X, y = load_diabetes(return_X_y=True)
X_train, X_test , y_train,y_test =train_test_split(X,y, test_size=0.33)

#Train model 
model =LinearRegression()
model.fit(X_train,y_train)

#Save model to file 
joblib.dump(model,"model.pkl")
print("traning complete model saved to model.pkl")
 


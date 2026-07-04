import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler


model = load_model("model/titanic_model.h5")


age = float(input("Enter Age: "))
gender = input("Gender (male/female): ")
fare = float(input("Fare: "))
pclass = int(input("Class (1/2/3): "))


# male=1 female=0
if gender.lower() == "male":
    gender = 1
else:
    gender = 0


data = np.array([[age, gender, fare, pclass]])


# same preprocessing as training
scaler = StandardScaler()

# Titanic approximate training values
train_data = np.array([
    [22,0,7.25,3],
    [38,0,71.28,1],
    [26,1,7.92,3]
])

scaler.fit(train_data)

data = scaler.transform(data)


result = model.predict(data)


print("Probability:", result[0][0])


if result[0][0] > 0.4:
    print("Survived : Yes")
else:
    print("Survived : No")
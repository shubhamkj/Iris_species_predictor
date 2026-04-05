import pickle
import numpy as np

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Sample predictions
samples = [
    [5.1, 3.5, 1.4, 0.2],  # Setosa
    [7.0, 3.2, 4.7, 1.4],  # Versicolor
    [6.3, 3.3, 6.0, 2.5],  # Virginica
]

species = ['Setosa', 'Versicolor', 'Virginica']

for i, sample in enumerate(samples):
    prediction = model.predict([sample])
    print(f"Sample {i+1}: {sample} -> Predicted: {species[prediction[0]]}")
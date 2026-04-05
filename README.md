# Iris Species Predictor

A machine learning web application to predict the species of Iris flowers based on their measurements using a Random Forest classifier.

## 🌸 Features

- Interactive web interface built with Streamlit
- Predict Iris species (Setosa, Versicolor, Virginica) from sepal and petal measurements
- Real-time prediction with sliders for input
- Trained on the classic Iris dataset

## 📋 Requirements

- Python 3.7+
- scikit-learn
- streamlit
- pandas
- numpy

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shubhamkj/Iris_species_predictor.git
   cd Iris_species_predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (optional, model.pkl is already included):
   ```bash
   python train_model.py
   ```

## 🎯 Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501` and use the sliders to input flower measurements, then click "Predict" to see the species.

## 🌐 Live Demo

This app can be accessed directly from GitHub by deploying it to Streamlit Cloud:

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub account
3. Select this repository: `shubhamkj/Iris_species_predictor`
4. Deploy the `app.py` file

Once deployed, you'll get a URL like: `https://your-app-name.streamlit.app`

For now, run it locally as described in Usage.

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier
- **Dataset**: Iris dataset from scikit-learn
- **Features**: Sepal length, Sepal width, Petal length, Petal width
- **Accuracy**: ~97% on test set (see log.txt for exact value)

## 📁 Project Structure

- `app.py`: Main Streamlit application
- `train_model.py`: Script to train and save the model
- `predict.py`: Prediction utilities (if used)
- `model.pkl`: Trained model file
- `requirements.txt`: Python dependencies
- `log.txt`: Training logs

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
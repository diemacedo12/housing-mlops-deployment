import gradio as gr
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load("model.pkl")

# Define prediction function
def predict_price(area, bedrooms, bathrooms):
    # Create input DataFrame
    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms]
    })
    # Make prediction
    prediction = model.predict(input_data)
    return f"Predicted Price: ${prediction[0]:,.2f}"

# Create Gradio interface
interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Area (sq ft)", value=7500),
        gr.Number(label="Bedrooms", value=3, precision=0),
        gr.Number(label="Bathrooms", value=2, precision=0)
    ],
    outputs="text",
    title="Housing Price Prediction",
    description="Enter the area, number of bedrooms, and number of bathrooms to predict the house price."
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()

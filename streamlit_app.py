import streamlit as st
import requests

st.set_page_config(page_title="Iris Classifier", page_icon="🌸", layout="centered")

st.title("🌸 Iris Flower Classifier")
st.markdown("Enter the flower measurements below and click **Predict** to classify the Iris species.")

API_URL = st.sidebar.text_input("API URL", value="http://localhost:8000")

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info("This app calls a FastAPI backend that uses a Random Forest model trained on the Iris dataset.")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1, 0.1)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5, 0.1)

with col2:
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4, 0.1)
    petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2, 0.1)

if st.button("🔍 Predict", use_container_width=True):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    try:
        response = requests.post(f"{API_URL}/predict", json=payload, timeout=5)
        if response.status_code == 200:
            result = response.json()
            st.success(f"**Predicted Species: {result['species'].capitalize()}** (class {result['prediction']})")
            st.markdown("### Prediction Probabilities")
            for species, prob in result["probabilities"].items():
                st.progress(prob, text=f"{species}: {prob:.2%}")
        else:
            st.error(f"API error: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the API. Make sure the FastAPI server is running.")
    except Exception as e:
        st.error(f"Error: {e}")

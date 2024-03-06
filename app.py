import streamlit as st
from fastai.vision.all import *
import plotly.express as px

# title 
st.title("Model for classificate animals")

# upload image
file = st.file_uploader("Download image", type=['png', 'jpg', 'gif', 'svg'])

if file:

    st.image(file)
    # PIL convert 
    img = PILImage.create(file)

    # Model
    model = load_learner('animals_model.pkl')

    # Predict 
    pred, pred_id, probs = model.predict(img)

    st.success(f"Predict: {pred}")
    st.info(f"Probability: {probs[pred_id]*100:.1f}%")

    # Plotting
    fig = px.bar(x=model.dls.vocab,y= probs*100, title="Animal Classification Sort")
    fig.update_layout(
        autosize=False,
        width=600,
        height=450,
        template='plotly_dark',
        title=dict(
            text="Animal Classification Sort",
            font=dict(size=20, color='#FFFFFF'),
            x=0.4,
            y=0.9
        ),
        xaxis_title=dict(text='Classification', font=dict(size=16, color='#FFFFFF')),
        yaxis_title=dict(text='Probability', font=dict(size=16, color='#FFFFFF')),
        plot_bgcolor='rgb(40, 70, 70)',
        xaxis=dict(tickfont=dict(size=14, color='#FFFFFF')),
        yaxis=dict(tickfont=dict(size=14, color='#FFFFFF'))
    )    
    st.plotly_chart(fig)
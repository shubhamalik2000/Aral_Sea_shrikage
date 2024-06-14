import streamlit as st

st.title('Studying the Shrinkage of Aral Sea')
st.write('''
Over the years, the surface area of the Aral Sea has been descreing. So, here is the processed data to showcase, the findings. 
''')

st.image(r"Deployement/original.jpg", caption = 'Data image, with a gap of 23 years')

latex_exp1 = "\[ d(p, q) = \sqrt{\sum_{i=1}^n (p_i - q_i)^2} \]"

import streamlit as st

euclidean_formula = r'd(p, q) = \sqrt{\sum_{i=1}^n (p_i - q_i)^2}'
manhattan_formula = r'd(p, q) = \sum_{i=1}^n |p_i - q_i|'
chebyshev_formula = r'd(p, q) = \max_{i=1}^n |p_i - q_i|'

st.write(f"""
### Distance Metrics

Distance metrics are mathematical measures used to quantify the distance or similarity between data points in a given space. Three commonly used distance metrics are Euclidean, Manhattan, and Chebyshev distances.

#### Euclidean Distance
Euclidean distance is the most commonly used distance metric. It measures the straight-line distance between two points in Euclidean space. The formula for Euclidean distance between two points p = (p1, p2, ..., pn) and q = (q1, q2, ..., qn) is:

 ${euclidean_formula}$ 

#### Manhattan Distance
Manhattan distance, also known as L1 distance or taxicab distance, measures the distance between two points by only moving along the axes at right angles, as if moving along the grid lines of a city. The formula for Manhattan distance between two points p = (p1, p2, ..., pn) and q = (q1, q2, ..., qn) is:

 ${manhattan_formula}$ 

#### Chebyshev Distance
Chebyshev distance, also known as L∞ distance, measures the maximum distance one has to travel along any coordinate dimension. It is used in scenarios where the maximum movement in any dimension is of primary interest. The formula for Chebyshev distance between two points p = (p1, p2, ..., pn) and q = (q1, q2, ..., qn) is:

 ${chebyshev_formula}$ 

""")


st.header('Using Euclidean Distance')
st.image(r"Deployement/euclidean.png")

st.header('Using Manhattan Distance')
st.image(r"Deployement/manhattan.png")

st.header('Using Chebyshev Distance')
st.image(r"Deployement/chebyshev.png")

st.header('Working of various distance metrics')
st.image(r"Deployement/comparison.png")

st.header('Findings')
st.write('Our calculation shows that there has been 89% decrease in the surface area. \n Check the calculation here: https://github.com/shubhamalik2000/Aral_Sea_shrikage')


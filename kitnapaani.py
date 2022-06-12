import streamlit as st
import math

st.write("Enter the Time taken by each pipe in same units")

pipe1 = st.slider("Pipe 1",0,30,0)
pipe2 = st.slider("Pipe 2",0,30,0)
pipe3 = st.slider("Pipe 3",0,30,0)

pipe1_2 = st.slider("Pipe 1 and 2",0,30,0)
pipe2_3 = st.slider("Pipe 2 and 3",0,30,0)
pipe3_1 = st.slider("Pipe 1 and 3",0,30,0)

pipe1_2_3 = st.slider("All 3 pipes",0,30,0)

work = math.lcm(pipe1,pipe2,pipe3,pipe1_2,pipe2_3,pipe3_1)

st.write("capacity of tank is ")

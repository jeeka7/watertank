import streamlit as st
import math
from math import gcd

st.write("Enter the Time taken by each pipe in same units")

pipe1 = st.slider("Pipe 1",0,30,0)
pipe2 = st.slider("Pipe 2",0,30,0)
pipe3 = st.slider("Pipe 3",0,30,0)

pipe1_2 = st.slider("Pipe 1 and 2",0,30,0)
pipe2_3 = st.slider("Pipe 2 and 3",0,30,0)
pipe3_1 = st.slider("Pipe 1 and 3",0,30,0)

pipe1_2_3 = st.slider("All 3 pipes",0,30,0)

#work = math.lcm(pipe1,pipe2,pipe3,pipe1_2,pipe2_3,pipe3_1)

time_taken = [pipe1,pipe2,pipe3,pipe1_2,pipe2_3,pipe3_1,pipe1_2_3]

NonZeroPipes = []

def RemoveZeroes():
  for pipe in time_taken:
    if (pipe == 0):
      pass
    else:
      NonZeroPipes.append(pipe)

RemoveZeroes()

def PrintKnown():
  for pipe in NonZeroPipes:
    st.write(pipe)
PrintKnown()

lcm = NonZeroPipes[0]
for i in NonZeroPipes[1:]:
  lcm = int(lcm*i/gcd(lcm, i))
  
st.write("capacity of tank is ", lcm)
work=lcm

e1=work/pipe1
e2=work/pipe2
e3=work/pipe3


st.write("time taken by pipe 1 to alone fill the tank is ",work/e1)
st.write("time taken by pipe 2 to alone fill the tank is ",work/e2)
st.write("time taken by pipe 3 to alone fill the tank is ",work/e3)

st.write("time taken by pipe 1 and pipe 2 together to fill the tank is ",work/(e1+e2))
st.write("time taken by pipe 2 and pipe 3 together to fill the tank is ",work/(e2+e3))
st.write("time taken by pipe 3 and pipe 1 together to fill the tank is ",work/(e1+e3))

st.write("time taken by all 3 pipe to fill the tank is ",work/(e1+e2+e3)

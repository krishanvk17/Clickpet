import streamlit as st
clicks=0
st.title("Online Clickpet")
st.info("This website will not save progress!")

if st.button("Click!"):
  clicks=clicks+1

  
  st.write("You have clicked",clicks,"times!" )

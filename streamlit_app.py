import streamlit
import pandas
import requests

streamlit.title("My breakfast")
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#creating a pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])
filter_list = my_fruit_list.loc[fruits_selected]

# display only selected items
streamlit.dataframe(filter_list)

fruityvice_response = request.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)


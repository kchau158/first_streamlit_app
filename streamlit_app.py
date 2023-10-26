import streamlit
import pandas
import requests
import snowflake.connector

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

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input("What fruit do you like?",'Kiwi')
streamlit.text("User enters "+fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


#snowflake test
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_csr = my_cnx.cursor()
my_csr.execute("select * from fruit_load_list")
my_data_row = my_csr.fetchall()
streamlit.text("The fruit load list contains..")
streamlit.text(my_data_row)

user_selected_fruit = streamlit.multiselect("What would you like to add",['Apple'])






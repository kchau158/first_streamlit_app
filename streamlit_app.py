import streamlit
import pandas
import requests
import snowflake.connector
import urllib.error as URLError


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
streamlit.dataframe(filter_list)

# display fruit advice section
# first define a function
def get_fruit_advice(input_text):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+input_text)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input("What fruit do you like?")
  if not fruit_choice:
    streamlit.error("Please select a fruit choice to get information")
  else:
    streamlit.dataframe(get_fruit_advice(fruit_choice)

except URLError as e:
  streamlit.error()
  
streamlit.stop()

#snowflake inserting data
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_csr = my_cnx.cursor()
my_csr.execute("select * from fruit_load_list")
my_data_row = my_csr.fetchall()
streamlit.text("The fruit load list contains..")
streamlit.dataframe(my_data_row)

adding_fruit = streamlit.text_input("What would you like to add?",'Apple')
streamlit.text("Thanks for adding "+adding_fruit)

my_csr.execute("insert into fruit_load_list values('from streamlit!')")






import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.cache to only run once.


@st.experimental_singleton
def init_connection():
	return psycopg2.connect(**st.secrets["postgres"])


conn = init_connection()
cur = conn.cursor()
conn.autocommit = True
with conn.cursor()as c:
	def create_ph_user():
		c.execute('Create table pharmacy_users if not exists(username TEXT, password TEXT)')
	def add_ph_user(username,password):
		c.execute('Insert into pharmacy_users(username,password) values(?,?)',(username,password))
	def login_ph_user(username,password):
		c.execute('SELECT * FROM pharmacy_users WHERE username =? AND password = ?',(username,password))
		data = c.fetchall()
		return data


def main():
	"""Simple Login App"""

	st.title("Simple Login App")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		users=['pharmacy','doctor','supplier']
		choice1 = st.sidebar.selectbox("User",users)
		st.subheader("Login Section")
		if choice1=='pharmacy':
			username = st.sidebar.text_input("User Name")
			password = st.sidebar.text_input("Password",type='password')
			if st.sidebar.checkbox("Login"):
			# if password == '12345':
				create_ph_user()
				

				result = login_ph_user(username,password)
				if result: 
					st.success("Logged In as {}".format(username))
				else:
					st.warning("Incorrect Username/Password")
	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_ph_user()
			add_ph_user(new_user,new_password)
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()
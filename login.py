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


def add_ph_user(username,password):
    cur.execute("Insert into pharmacy_users(username,password) values(%s,%s);",(username,password))
def login_ph_user(username,password):
    cur.execute("SELECT * FROM pharmacy_users WHERE username =%s AND password = %s;",(username,password))
    data = cur.fetchall()
    return data
def add_dc_user(username,password):
    cur.execute("Insert into doctor_users(username,password) values(%s,%s);",(username,password))
def login_dc_user(username,password):
    cur.execute("SELECT * FROM doctor_users WHERE username =%s AND password = %s;",(username,password))
    data = cur.fetchall()
    return data
def add_sp_user(username,password):
    cur.execute("Insert into supplier_users(username,password) values(%s,%s);",(username,password))
def login_sp_user(username,password):
    cur.execute("SELECT * FROM supplier_users WHERE username =%s AND password = %s;",(username,password))
    data = cur.fetchall()
    return data


def main():
    """Simple Login App"""

    st.title("Simple Login App")

    menu = ["Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    

    if choice == "Login":
        users=['pharmacy','doctor','supplier']
        choice1 = st.sidebar.selectbox("User",users)
        st.subheader("Login Section")
        if choice1=='pharmacy':
            username = st.sidebar.text_input("User Name")
            password = st.sidebar.text_input("Password",type='password')
            if st.sidebar.button("Login"):
            # if password == '12345':
                #create_ph_user()
                

                result = login_ph_user(username,password)
                if result: 
                    st.success("Logged In as {}".format(username))
                else:
                    st.warning("Incorrect Username/Password")
                app.add_app
        if choice1=='doctor':
            username = st.sidebar.text_input("User Name")
            password = st.sidebar.text_input("Password",type='password')
            if st.sidebar.button("Login"):
            # if password == '12345':
                #create_ph_user()
                

                result = login_dc_user(username,password)
                if result: 
                    st.success("Logged In as {}".format(username))
                else:
                    st.warning("Incorrect Username/Password")
        if choice1=='supplier':
            username = st.sidebar.text_input("User Name")
            password = st.sidebar.text_input("Password",type='password')
            if st.sidebar.button("Login"):
            # if password == '12345':
                #create_ph_user()
                

                result = login_sp_user(username,password)
                if result: 
                    st.success("Logged In as {}".format(username))
                else:
                    st.warning("Incorrect Username/Password")
    elif choice == "SignUp":
        users=['pharmacy','doctor','supplier']
        choice2=st.sidebar.selectbox("Menu",users)
        if choice2=='pharmacy':
            new_user = st.text_input("Username")
            new_password = st.text_input("Password",type='password')

            if st.button("Signup"):
                
                add_ph_user(new_user,new_password)
                st.success("You have successfully created a valid Account")
                st.info("Go to Login Menu to login")
        elif choice2=='doctor':
            new_user = st.text_input("Username")
            new_password = st.text_input("Password",type='password')

            if st.button("Signup"):
                
                add_dc_user(new_user,new_password)
                st.success("You have successfully created a valid Account")
                st.info("Go to Login Menu to login")
        elif choice2=='supplier':
            new_user = st.text_input("Username")
            new_password = st.text_input("Password",type='password')

            if st.button("Signup"):
                
                add_sp_user(new_user,new_password)
                st.success("You have successfully created a valid Account")
                st.info("Go to Login Menu to login")



if __name__ == '__main__':
    main()

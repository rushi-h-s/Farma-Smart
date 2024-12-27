from email.message import EmailMessage
import ssl
import smtplib
from connector.ConnectionProvider import ConnectionProvider


def fetch_appuser_data():
    try:
        connection_provider = ConnectionProvider()
        con = connection_provider.get_con()
        cursor = con.cursor()

        # Query to fetch user data
        cursor.execute(
            "SELECT appuser_pk, userRole, name, doj, mobileNumber, emailid, username, password, salary FROM appuser")  # Adjust your SQL query as needed
        rows = cursor.fetchall()

        # Creating a formatted string for the email body
        user_list = []
        for row in rows:
            appuser_pk, userRole, name, doj, mobileNumber, emailid, username, password, salary = row
            user_list.append(f"User ID: {appuser_pk}, Role: {userRole}, Name: {name}, "
                             f"Date of Joining: {doj}, Mobile: {mobileNumber}, Email: {emailid}, "
                             f"Username: {username}, Salary: {salary}")

        # Join all user details into a single string
        result = "\n".join(user_list)

        con.close()
        return result
    except Exception as e:
        print(f"An error occurred while fetching user data: {str(e)}")
        return ""


# Fetch user data and assign it to the result variable
result = fetch_appuser_data()

try:
    # Email configuration
    sender_email = "divesh.patil@ssvpsengg.ac.in"
    receiver_email = "diveshpatil9104@gmail.com"
    password = "smnp ukhw lmfs anov"  # Make sure this password is kept secure
    subject = "App Users Information"
    body = "APP USERS:\n" + result  # Use the result from the database

    # Create a multipart message
    em = EmailMessage()
    em["From"] = sender_email
    em["To"] = receiver_email
    em["Subject"] = subject

    # Add body to email
    em.set_content(body)

    # Establish a connection to the SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender_email, password)

        # Send the email
        smtp.sendmail(sender_email, receiver_email, em.as_string())

    print("Email sent successfully")
except Exception as e:
    print(f"An error occurred: {str(e)}")

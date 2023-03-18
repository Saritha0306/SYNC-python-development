import random
import smtplib

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email(to_email, subject, body):
    from_email = "sarithaunkverma@gmail.com"
    password = "vqblujafapqqcwwp"
    message = f"Subjesarict: {subject}\n\n{body}"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, message)
    server.quit()

otp = generate_otp()
user_email = input("Enter your email: ")
send_email(user_email, "OTP Verification", f"Your OTP is: {otp}")

user_otp = input("Enter the OTP you received: ")
if user_otp == otp:
    print("User verified successfully!")
else:
    print("Invalid OTP. Please try again.")

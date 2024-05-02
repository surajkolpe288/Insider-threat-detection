import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the data
data = pd.DataFrame({
  'email_text': ["Your account has been compromised. Click here to reset your password.",
                  "Congratulations! You've won a free vacation.",
                  "Meeting reminder: Tomorrow at 10 AM.",
                  "URGENT: Your attention is required.",
                  "Hi, how are you doing?",
                  "Paid holidays, sick leave, and vacation time Find out more about our operations and activities.",
                  '''Attention User, Your files have been encrypted by ransomware. Pay "$1000" in Bitcoin to the following address to decrypt your files''',
                  "if your Want to be involved with a project login to an account with user name 'dinesh_hcl_1248' with password '191123@dnk'. You can download the files."],
  'is_threat': [1, 1, 0, 1, 0,0,1,1]
})

# Vectorize the text data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['email_text'])
y = data['is_threat']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the SVM model
svm_model = SVC()
svm_model.fit(X_train, y_train)

# Function to predict whether an email is a threat or not
def predict_threat(email_text):
  email_vectorized = vectorizer.transform([email_text])
  prediction = svm_model.predict(email_vectorized)
  if prediction[0] == 1:
    return "Threat"
  else:
    return "No Threat"

# Function to handle button click event
def on_click():
  email_text = entry.get()
  result = predict_threat(email_text)
  messagebox.showinfo("Prediction Result", result)

# Create the main window
root = tk.Tk()
root.title("Email Threat Detection")

# Create a label and entry for user input
label = tk.Label(root, text="Enter email text:")
label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Create a button to trigger prediction
button = tk.Button(root, text="Predict", command=on_click)
button.pack()

# Run the application
root.mainloop()
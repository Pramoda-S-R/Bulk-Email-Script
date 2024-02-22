# Bulk Email Script

## Overview
This Python script automates the process of sending personalized emails to a list of recipients. It reads recipient details from an Excel file, fetches an HTML template for the email body, personalizes the email content, and sends the emails securely using SMTP and SSL.

## Features
- Personalizes emails using recipient names extracted from an Excel spreadsheet.
- Utilizes an HTML file as the email body template, allowing for rich text and formatting in the emails sent.
- Securely logs in to the sender's email account using SMTP over SSL.
- Handles exceptions gracefully, providing feedback on the success or failure of each email sent.

## Setup Instructions

### Environment Setup
1. Ensure you have Python installed on your machine.
2. Install required packages:
```pip install pandas bs4```

### Preparing Your Data
1. Update the `docs\\info.xlsx` file with the email addresses and names of your recipients.
2. Customize the `html\\index.html` file to design your email body. Use `[[name]]` as a placeholder where you want the recipient's name to appear.

### Configuring Email Account for Sending Emails
- **For Gmail Users:**
1. Enable 2-Step Verification for your Google Account.
2. Generate an App Password specifically for this script.
  - Go to Google Account Settings > Security > App Passwords > Generate.
  - Choose "Other" and name it (e.g., "Python Email Script").
  - Use this 16-character App Password in the script as your `PASSWORD`.

- **For Yahoo Mail Users:**
1. Enable 2-Step Verification for your Yahoo Account.
2. Create an App Password specifically for this script.
  - Go to Yahoo Account Security Settings > Account Security > Generate app password.
  - Select "Other App" and name it (e.g., "Python Email Script").
  - Use this App Password in the script as your `PASSWORD`.

### Running the Script
Execute the script in your terminal or command prompt:
```python email_sender.py```

## Customization
Feel free to customize the HTML email template and Excel file format to fit your needs. You can also adjust the script to include additional personalization or modify the email sending parameters.

## Screenshots
Here are some examples of the emails sent using this script. (Add your images here)

- **Email Example 1:**
  ![Email Example 1](https://www.dropbox.com/scl/fi/midj016kfj3npl7rf4f9l/example1.png?rlkey=9msl6ngtuzdudem5x6q2xl3ik&dl=0)

- **Email Example 2:**
  ![Email Example 2](https://www.dropbox.com/scl/fi/xaw4yknnjwos6we448195/example2.png?rlkey=eegggtllyp6z175ct0yorny0v&dl=0)

## License
This project is open-sourced under the MIT license. Feel free to use, modify, and distribute it as you see fit.

## Contributions
Contributions are welcome! If you have suggestions for improvements or encounter any issues, please feel free to submit a pull request or open an issue.

---
Happy emailing!

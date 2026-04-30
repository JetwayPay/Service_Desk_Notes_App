# Service Desk Notes App

## Overview

The Service Desk Notes App is a beginner-friendly Python console application created to help CSD / Service Desk agents quickly create structured notes for Dash / ServiceNow tickets.

The app prompts the user for important ticket information, such as the customer’s name, eID, issue, impact, urgency, KB Article Number, troubleshooting steps, result, and next step. After the information is entered, the app generates a clean note that can be copied and pasted into Dash / ServiceNow.

## Purpose

The purpose of this project is to make ticket documentation faster, cleaner, and more consistent for Service Desk work.

This app helps agents document:

- What happened
- Who contacted CSD
- Who was contacted during troubleshooting
- What troubleshooting was completed
- What the result was
- What the next step is
- Which KB Article Number was used

## Features

- Console-based Python application
- Beginner-friendly code structure
- Prompts the user for ticket information
- Requires a KB Article Number before continuing
- Generates a formatted Dash / ServiceNow note
- Uses functions to organize the code
- Uses input validation for required fields
- Easy to run in Visual Studio Code or terminal

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## How the App Works

The app asks the user to enter the following information:

- Incoming phone number
- Customer name
- Customer eID
- Customer email
- Customer phone number
- Device name or IP address
- KB Article Number
- Impact
- Urgency
- Whether others are affected
- Issue
- Who was contacted
- Troubleshooting steps
- Result
- Next step

After collecting the information, the app builds a formatted note that can be copied and pasted into Dash / ServiceNow.

## Example Output

```text
**Incoming Phone Number:
555-555-5555

Issue:
User is unable to log in to their workstation.

Impact:
Single user impacted

Urgency:
Medium

Others Affected?:
No

Device Name/IP Address:
PC12345

Customer's Name:
John Smith

Customer's eID:
e123456

Customer's Email:
john.smith@example.com

Customer's Phone Number:
555-123-4567

KB Article Number:
KB0012345

Who Was Contacted:
Customer and supervisor

Troubleshooting Steps:
Verified username, checked account status, reset password, and tested login.

Result:
User was able to log in successfully.

Next Step:
No further action needed.
How to Run the App
Make sure Python is installed on your computer.
Clone this repository:
git clone https://github.com/JetwayPay/Service_Desk_Notes_App.git
Open the project folder:
cd Service_Desk_Notes_App
Run the Python file:
python csd_dash_notes_console.py

If you are on Mac and python does not work, try:

python3 csd_dash_notes_console.py
Project Structure
Service_Desk_Notes_App/
│
├── csd_dash_notes_console.py
└── README.md
Code Concepts Used

This project demonstrates beginner Python concepts, including:

Variables
Functions
User input
String formatting
While loops
If statements
Return values
Basic input validation
Console output
Required Field Validation

The KB Article Number is required because incident tickets require a KB reference.

The program uses a while loop to make sure the user enters a KB Article Number before continuing.

If the user leaves the KB Article Number blank, the program displays a warning and asks again.

Future Improvements

Possible future improvements include:

Add a graphical user interface
Add multiple note templates
Add a copy-to-clipboard feature
Save notes to a text file
Add dropdown options for impact and urgency
Add date and time automatically
Create an executable version of the app
Add ServiceNow / Dash-specific templates
Author

Created by Larrell Thornton as a Service Desk note-taking tool and beginner software development project.

License

This project is for educational and portfolio purposes.**

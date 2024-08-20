# Spell and Grammar Checker

This repository contains a spell and grammar checker application built with Python. It uses advanced NLP models for text correction and Flask for server management. The user interface is designed to be responsive and customizable, using Bootstrap and SVG.

## 📝 Project Overview

This project is a web-based spell and grammar checker. It allows users to input text or upload files for spell and grammar correction. The application processes the input, identifies mistakes, and provides corrected text along with details about the errors found.

## 🛠️🌐 Technologies Used

- **Python 3.11.9**: Core application logic.
- **Flask**: Lightweight web framework for server-side logic.
- **Bootstrap**: For responsive and user-friendly UI design.
- **NLP Models**: Integrated for advanced text correction using `language_tool_python` and `enchant`.
- **Java 21.34**: Required for specific NLP libraries.
- **HTML/CSS**: UI and page structuring.
- **JavaScript**: For additional client-side functionality.

## ✨🌟 Features

- **Real-time Spell Check**: Detects and corrects spelling mistakes in input text.
- **Grammar Corrections**: Identifies and corrects grammatical errors.
- **File Upload**: Supports text file uploads for batch correction.
- **Customizable Interface**: Provides a responsive and user-friendly experience.
- **Error Reporting**: Displays a list of mistakes and their corrections.

## ⚙️🛠️ Requirements

- **Python 3.11.9**
- **Java 21.34**
- **pip**: For managing Python dependencies.
- **Flask**: To be installed via `requirements.txt`.
- **NLP Libraries**: `language_tool_python`, `enchant`.

## 🚀📥 How to Run

**1.** Install Python 3.11.9  
   Use the installer included in the project to install Python version 3.11.9 on the MS Windows platform.

**2.** Install Java 21.34  
   Install the Java Runtime Environment version 21.34 using the provided installer.

**3.** Locate the Python installation path  
   After installing Python, find the path where it was installed. Example path:  
   `C:\Users\<User_Name>\AppData\Local\Programs\Python\Python311\python.exe`  
   Remember this path as it will be needed later.

**4.** Find the `pip` path  
   Typically, the `pip` package manager is located in the `Scripts` directory, which is a subfolder of the Python installation. Example path:  
   `C:\Users\<User_Name>\AppData\Local\Programs\Python\Python311\Scripts\pip.exe`

**5.** Create a virtual environment  
   Go to the application's root directory where the project file is located. Use the following command to create a virtual environment:  
   `<full_path_to_python.exe> -m venv .`  
   Replace `<full_path_to_python.exe>` with the full path to Python found in step 3.

**6.** Navigate to the `Scripts` directory  
   After creating the virtual environment, navigate to the `Scripts` directory:  
   `cd Scripts`

**7.** Activate the virtual environment  
   Run the script to activate the virtual environment:  
   `activate.bat`  
   Note: On Linux and macOS, the command is `source activate`.

**8.** Navigate back to the root directory of the application  
   Return to the root directory of the application:  
   `cd ..`

**9.** Install dependencies  
   Install all necessary dependencies with the following command:  
   `<full_path_to_pip.exe> install -r requirements.txt`  
   Replace `<full_path_to_pip.exe>` with the full path to `pip` found in step 4.

**10.** Run the application  
    To run the application, use the following command:  
    `<full_path_to_python.exe> app.py`  
    Replace `<full_path_to_python.exe>` with the full path to Python found in step 3.

**11.** Open a web browser  
    Launch your web browser.

**12.** Access the application  
    In the browser, navigate to the following address:  
    **http://127.0.0.1:5000**


## 📸 Screenshots

![](image.png)

## 🚀🔮 Future Features

The App could be developed in ways given below:

- **Multi-language Support** - adding support for spell and grammar checks in multiple languages.
- **Advanced Text Analysis** - implementation of deep syntactical analysis and language style suggestions.
- **Mobile Compatibility** - optimization for mobile users.



# Finance Wizard

## Overview

**Finance Wizard** is a web application built using Streamlit that provides personalized investment suggestions based on user inputs. The suggestions are generated using the `llama3.1` AI model by Meta, accessed via the `ollama` platform. The application processes the financial information provided by the user to recommend suitable investment vehicles such as ETFs, mutual funds, bonds, stocks, and other options that match the user's risk appetite and financial goals.

## Features

- User-friendly interface to input financial details
- Personalized investment suggestions
- Real-time processing and display of results
- Option to reset all inputs
- Responsive and visually appealing layout

## Installation

To run the Finance Wizard application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/adityachavan198/finwiz.git
   cd finwiz
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Open the application:**
   - After running the command `streamlit run app.py`, the application will open in your default web browser.

2. **Enter your financial details:**
   - Input your annual income, age, current savings, marital status, fixed monthly expenses, liabilities, investment goals, and risk appetite using the provided input fields.

3. **Get investment suggestions:**
   - Click the "Get Investment Suggestions" button to receive personalized investment recommendations. The results will be displayed in a text area below the button.

4. **Reset the inputs:**
   - Click the "Reset" button to clear all inputs and start over.

## Code Structure

- **app.py:** The main file that contains the Streamlit interface and functions to handle user inputs and generate investment suggestions.
- **requirements.txt:** Lists all the dependencies required to run the application.

## Dependencies

- `streamlit`: Used for creating the web interface.
- `llama3.1` via `ollama`: Used for generating investment suggestions based on user inputs. Learn more about it [here](https://ollama.com/library/llama3.1).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

Created by Aditya Chavan. For any questions or suggestions, please connect with me: https://www.linkedin.com/in/aditya-ramesh-chavan/


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

---

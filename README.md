# Black-Shoes-Morton-model-

# Black-Scholes Model Option Pricing Calculator

This project is a Streamlit web application for calculating option prices using the Black-Scholes model and a binomial tree approach for American options. It provides an intuitive interface for users to input option parameters and displays both theoretical European and American option prices with detailed results and explanations.

---

## Features

- **European Option Pricing**: Implements the Black-Scholes model to calculate call and put option prices.
- **American Option Pricing**: Uses a binomial tree approach to calculate American option prices for both call and put options.
- **Interactive Input Fields**: Allows users to input key parameters like underlying price, strike price, volatility, risk-free rate, and time to expiration.
- **Detailed Explanation**: Displays the Black-Scholes formula and explains each variable for better understanding.
- **Enhanced UI/UX**: Includes a colorful and animated interface with a rainbow divider and visually appealing elements.

---

## Technologies Used

- **Python**
- **Streamlit**: For creating the interactive web interface.
- **SciPy**: For statistical computations (e.g., normal distribution function).
- **Math**: For mathematical calculations.

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/black-scholes-calculator.git
   cd black-scholes-calculator
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser at `http://localhost:8501`.

---

## How to Use

1. Open the app and enter the required input parameters:
   - **Underlying Price (S)**: Current price of the underlying asset.
   - **Strike Price (K)**: Strike price of the option.
   - **Time to Expiration (T)**: Time remaining for the option to expire (in years).
   - **Risk-Free Rate (r)**: Annual risk-free interest rate (decimal format).
   - **Volatility (\(\sigma\))**: Annualized volatility of the underlying asset (decimal format).
   - **Steps**: Number of steps for the binomial tree (for American options).
   - **Option Type**: Select "European Option" or "American Option".

2. View the results:
   - For European options, the app calculates and displays the call and put option prices based on the Black-Scholes model.
   - For American options, the app calculates the option price using the binomial tree approach.

3. Explore the formulas and explanations displayed on the dashboard for deeper insights.

---

## Screenshots

![image](https://github.com/user-attachments/assets/61fba8a4-6923-49c4-9c03-d99a6784c179)


![image](https://github.com/user-attachments/assets/a3e1ce3c-0a8e-4615-be47-4febaecf41d1)

---

## Future Enhancements

- Add additional option pricing models (e.g., Garman-Kohlhagen for currency options).
- Include visualizations of binomial trees and payoff diagrams.
- Support real-time market data integration for live calculations.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- Streamlit for making web app development intuitive.
- SciPy for robust statistical computations.
- Financial community resources for detailed explanations of the Black-Scholes model.

---



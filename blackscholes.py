import streamlit as st
import math
from scipy.stats import norm

st.markdown("""
    <style>
    .main-title {
    font-size: 36px !important;
    text-align: center !important;
    color: #4CAF50 !important;
    font-weight: bold !important;
    }
    .body {
    background-color: yellow !important;
    }
    
    .rainbow-divider {
        height: 4px;
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius: 50px;
    }
    .button-style {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    </style>

""", unsafe_allow_html=True)


# Define Functions
def black_scholes(S, K, T, r, vol):
    # Calculate d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * vol**2) * T) / (vol * math.sqrt(T))
    d2 = d1 - (vol * math.sqrt(T))

    # Calculate call and put option prices
    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return d1, d2, call_price, put_price


def binomial_tree_american_option(S, K, T, r, vol, steps, option_type):
    dt = T / steps
    u = math.exp(vol * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(r * dt) - d) / (u - d)

    # Initialize asset prices at maturity
    asset_prices = [S * (u**j) * (d**(steps - j)) for j in range(steps + 1)]

    # Initialize option values at maturity
    if option_type == "Call":
        option_values = [max(0, price - K) for price in asset_prices]
    elif option_type == "Put":
        option_values = [max(0, K - price) for price in asset_prices]

    # Step back through the tree
    for i in range(steps - 1, -1, -1):
        option_values = [
            max(
                (p * option_values[j + 1] + (1 - p) * option_values[j]) * math.exp(-r * dt),
                (price - K if option_type == "Call" else K - price)
            )
            for j, price in enumerate([S * (u**j) * (d**(i - j)) for j in range(i + 1)])
        ]

    return option_values[0]

# Streamlit App Interface

st.markdown('<div class="rainbow-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Black-Scholes Model Option Pricing Calculator</div>', unsafe_allow_html=True)
# Add divider

st.markdown("<div style='height: 4px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); margin-top: 10px; margin-bottom: 20px;'></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    S = st.number_input("Underlying Price (S)", value=45.0, step=0.1)
    K = st.number_input("Strike Price (K)", value=40.0, step=0.1)

with col2:
    T = st.number_input("Time to Expiration (T in years)", value=2.0, step=0.1)
    r = st.number_input("Risk-Free Rate (r in decimal)", value=0.1, step=0.01)

# User Inputs
vol = st.number_input("Volatility (σ in decimal)", value=0.1, step=0.01)
steps = st.number_input("Number of Steps (for American Option)", value=100, step=1, min_value=1)
option_type_input = st.selectbox("Option Type (for American Option)", ("Call", "Put"))

# Option Type Selection
option_type = st.radio("Select Option Type:", ("European Option", "American Option"))


if option_type == "European Option":
    # Calculate Black-Scholes Outputs
    d1, d2, call_price, put_price = black_scholes(S, K, T, r, vol)

    # Display Results
    st.subheader("Results (European Option)")
    st.write(f"The value of d1 is: {d1:.4f}")
    st.write(f"The value of d2 is: {d2:.4f}")
    st.write(f"The price of the Call Option is: ${call_price:.2f}")
    st.write(f"The price of the Put Option is: ${put_price:.2f}")

elif option_type == "American Option":
    # Calculate American Option Pricing using Binomial Tree
    american_price = binomial_tree_american_option(S, K, T, r, vol, int(steps), option_type_input)

    # Display Results
    st.subheader("Results (American Option)")
    st.write(f"The price of the {option_type_input} Option is: ${american_price:.2f}")

# Additional Information
st.subheader("Black-Scholes Model Formula")
st.latex(r"""d_1 = \frac{\ln(\frac{S}{K}) + (r + \frac{\sigma^2}{2})T}{\sigma \sqrt{T}}""")
st.latex(r"""d_2 = d_1 - \sigma \sqrt{T}""")
st.latex(r"""Call\ Price = S \Phi(d_1) - K e^{-rT} \Phi(d_2)""")
st.latex(r"""Put\ Price = K e^{-rT} \Phi(-d_2) - S \Phi(-d_1)""")

st.subheader("Explanation of Variables")
st.write("""\
- \(S\): Current price of the underlying asset.  
- \(K\): Strike price of the option.  
- \(T\): Time to expiration (in years).  
- \(r\): Risk-free interest rate (annualized).  
- \(\sigma\): Volatility of the underlying asset (annualized).  
- \(\Phi\): Cumulative distribution function of the standard normal distribution.
""")

st.subheader("Additional Insights")
st.write("The Black-Scholes model assumes the following:")
st.write("1. The returns on the underlying asset are normally distributed.")
st.write("2. Markets are efficient and there are no arbitrage opportunities.")
st.write("3. The risk-free rate and volatility are constant over the option's life.")
st.write("4. There are no transaction costs or taxes.")
st.write("5. The option can be exercised only at expiration (European option).")

st.write("This model is widely used in the financial industry, but its assumptions may not always hold true in real-world scenarios. "
         "Adjustments like the Garman-Kohlhagen model (for foreign exchange options) or incorporating stochastic volatility are used to address some of these limitations.")

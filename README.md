# Predicting Undervalued and Overvalued Options Using Black-Scholes and Binomial Option Pricing Models

## Overview
This project aims to identify mispriced options by comparing market prices with theoretical prices calculated using the Black-Scholes and Binomial Option Pricing models. By determining whether an option is undervalued or overvalued, traders and analysts can make more informed investment decisions.

## Key Concepts
- **Black-Scholes Model**: A model providing a closed-form solution for pricing European options.
- **Binomial Tree Model**: A flexible model that uses a discrete-time framework, suitable for American options and dividend-paying stocks.

## Methodology
1. **Data Collection**: Collected option data through web scraping through the NSE website.
2. **Model Implementation**:
   - **Black-Scholes Model**: Implemented considering constant volatility and a risk-free rate.
   - **Binomial Model**: Constructed using a multi-step binomial tree to account for early exercise and other features.
3. **Comparison**: Compare theoretical prices with market prices to detect mispriced options.
4. **Prediction**: Classify options as undervalued or overvalued based on predefined criteria.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/chetanya-sharma/Option-Pricing-Models-on-Equity-Option-Data.git
    ```
2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Results

- **Analysis**: Finding overvalued and undervalued options based on Black Scholes on Indian equity option data and Binomial Tree model on american equity option data.

## Limitations

- **Assumptions**: Both models assume constant volatility and a known risk-free rate, which may not hold true in real markets.
- **Model Accuracy**: Potential inaccuracies in pricing due to unmodeled market factors.

## Future Work

- **Improvements**: Explore advanced models like Black-Scholes-Merton model which includes dividend factor.

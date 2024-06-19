# Tokencal: Token Price Estimation for LLMs
<p align="center">
  <img src="tokencal.png" height="500" alt="Tokencal" />
</p>

<p align="center">
    <a href="https://pypi.org/project/tokencal/" target="_blank">
        <img alt="Version" src="https://img.shields.io/pypi/v/tokencal?style=for-the-badge&color=3670A0">
    </a>
</p>

## Overview
**Tokencal** is a sophisticated tool designed to estimate token prices for large language models (LLMs). Whether you're a developer, researcher, or business, Tokencal helps you optimize token usage and manage costs effectively. 

## Features
- **Accurate Estimations**: Get precise token price estimates for various LLMs.
- **Efficient Performance**: Fast calculations to save your time.
- **Extensive Compatibility**: Works with multiple LLMs.

## Installation
To install Tokencal, simply run:
```bash
pip install tokencal
```
## Usage
Using Tokencal is straightforward. Here’s a quick example to get you started:
```
from tokencal import TokenEstimator

# Initialize the estimator with your LLM model details
estimator = TokenEstimator(model_name="Your_LLM_Model")

# Estimate token price
price = estimator.estimate_price(text="Sample text to estimate token price.")
print(f"Estimated token price: {price}")
```

## Keywords
Token price estimation, LLM, Large Language Models, cost optimization, token usage
# Simplified Binance Futures Trading Bot (Testnet)

A command-line trading bot that uses the Binance Futures **Testnet** API to place **market**, **limit**, and **stop-limit** orders.  
Built with `python-binance` and structured for clarity, logging, and reusability.

---

## Features

- Place **Market**, **Limit**, and **Stop-Limit** orders
- Supports both **Buy** and **Sell** sides
- Logs API requests, responses, and errors
- Shows available **USDT balance**
- CLI-based input prompts
- Modular code structure with clean logging
- Runs safely on Binance **Test**

## 🛠️ Setup Instructions

### 1. 📦 Install Dependencies
```bash
pip install -r requirements.txt

### 2. Set up your `.env` file  
Create a .env file and add necessary configurations mentioned in Example.env data.
Find your API key and API secret from the  
[Binance Futures Testnet](https://testnet.binancefuture.com)

### 3. Run the bot
```bash
python trading_bot.py

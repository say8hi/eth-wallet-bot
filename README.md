# 🛠This bot is currently in development🛠
# ETH Wallet Telegram Bot
This Telegram bot provides a user-friendly interface for securely storing and transferring Ethereum (ETH) within the Telegram platform. Easily manage your ETH assets with just a few clicks!

## About
### Features

- **Wallet Creation:** Generate a new Ethereum wallet associated with your Telegram account.
  
- **Balance Inquiry:** Check the current balance of your Ethereum wallet.

- **Deposit Functionality:** Obtain a unique deposit address to add ETH to your wallet.

- **Secure Transactions:** Initiate secure transactions to send ETH to other wallets.

- **Transaction History:** View a record of your recent wallet transactions.


### Security

- Your wallet is secured using industry-standard encryption.


### Technologies Used

- **Python:** The bot is developed using the Python programming language.

- **aiogram:** A Python framework for Telegram bot development.

- **web3:** A Python library for interacting with the Ethereum blockchain.

- **PostgreSQL:** The choice of database for storing bot-related information.

- **Redis:** Used as a storage backend for the bot.

- **Celery:** Used for scheduling and performing regular database dumps.

---

## Installation Guide

### Local Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/say8hi/eth-wallet-bot.git
2. Navigate to the project directory:

    ```bash
   cd eth-wallet-bot
   
3. Create a .env file with the following content:
    
   ```env
   # Tg bot
    BOT_TOKEN=your_telegram_bot_token
    ADMINS=your_admin_telegram_user_id

    # Postgres
    POSTGRES_DB=your_database_name
    POSTGRES_USER=your_database_user
    POSTGRES_PASSWORD=your_database_password
    POSTGRES_HOST=your_postgres_host
    
    # Redis
    REDIS_HOST=your_redis_host
    REDIS_PORT=your_redis_port
    REDIS_PASSWORD=your_redis_password
You can get BOT_TOKEN from [@botfather](https://t.me/botfather)
   
4. Install the required dependencies:
    ```bash
   pip install -r requirements.txt
   
5. Set up your PostgreSQL database and configure the connection in the .env file.

6. Configure your Redis server and update the .env file.
7. Run the bot:
    ```bash
   python bot.py
   
### Docker Compose Installation
1. Clone the repository to your server:
    ```bash
   git clone https://github.com/say8hi/eth-wallet-bot.git

2. Navigate to the project directory:
    ```bash
   cd eth-wallet-bot

3. Create a .env file with the same content as above.
4. Create and start the Docker containers:
    ```bash
   docker-compose up -d
5. Access your Telegram bot and start managing your ETH!

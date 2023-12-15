from tgbot.services.db_commands import DatabaseCommands


class Database:

    users = DatabaseCommands("users")
    eth_accounts = DatabaseCommands("eth_accounts")

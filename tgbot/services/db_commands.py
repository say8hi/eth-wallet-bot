
import asyncpg

from asyncpg import Pool


class DatabaseCommands:

    _pool: Pool = None

    def __init__(self, table: str):
        self.table = table

    @classmethod
    async def connect(cls, user, password, database, host):
        cls._pool = await asyncpg.create_pool(user=user, password=password,
                                              database=database, host=host)

    @classmethod
    async def close(cls):
        if cls._pool:
            await cls._pool.close()

    async def execute_query(self, query, *args):
        async with self._pool.acquire() as conn:
            return await conn.execute(query, *args)

    async def fetch_query(self, query, *args):
        async with self._pool.acquire() as conn:
            result = await conn.fetch(query, *args)
            return result[0] if result and len(result) == 1 else result

    async def add(self, **kwargs):
        keys, values = zip(*kwargs.items())
        query = f"INSERT INTO {self.table} ({', '.join(keys)}) VALUES " \
                f"({', '.join(['$'+str(i) for i in range(1, len(values) + 1)])}) RETURNING *"
        return await self.fetch_query(query, *values)

    async def update(self, id_value: int, **kwargs):
        set_values = ', '.join([f"{key} = ${i}" for i, (key, value) in enumerate(kwargs.items(), start=1)])
        query = f"UPDATE {self.table} SET {set_values} WHERE id = $1"
        await self.execute_query(query, id_value)

    async def get(self, id_value: int = None, get_all: bool = False):
        if get_all:
            return await self.fetch_query(f"SELECT * FROM {self.table}")
        else:
            return await self.fetch_query(f"SELECT * FROM {self.table} WHERE id = $1", id_value)

    async def delete(self, id_value: int):
        query = f"DELETE FROM {self.table} WHERE id = $1"
        await self.execute_query(query, id_value)

    @classmethod
    async def create_tables(cls):
        # Список запросов для создания таблиц
        table_creation_queries = (
            """
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY,
                username VARCHAR(255),
                registered TIMESTAMP
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS eth_accounts (
                id INT REFERENCES users(id),
                address VARCHAR(42) NOT NULL,
                mnemonic_phrase VARCHAR(255) NOT NULL,
                private_key VARCHAR(64) NOT NULL
            );
            """
        )

        async with cls._pool.acquire() as conn:
            for query in table_creation_queries:
                await conn.execute(query)

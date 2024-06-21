from pymongo import MongoClient
import os
import pandas as pd


class Analyzer:
    def __init__(self, strategy_name: str):
        self.strategy_name = strategy_name

    def get_trading_history(self):
        client = MongoClient(os.getenv("MONGO_URL"))
        db = client["qupiato"]
        collection = db["trading_history"]

        cursor = collection.find(
            {"strategy_name": self.strategy_name}, {"_id": 0}
        ).sort({"created_at": 1})

        docs = list(cursor)

        positions = []

        if len(docs) > 0:
            positions = docs[-1]["positions"]
            for doc in docs:
                doc.pop("positions")

        trading_df = pd.DataFrame(docs)
        positions_df = pd.DataFrame(positions)

        return trading_df, positions_df

    def analyze(self):
        history = self.get_trading_history()

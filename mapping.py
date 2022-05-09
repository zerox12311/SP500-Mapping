from typing import List
from collections import UserDict
import pandas as pd
import numpy as np

class KeywordMap(UserDict):

    def __init__(self, keyword: str, alias: List[str]) -> None:
        super().__init__()
        self.keyword = keyword
        self.alias = alias
        self.data[keyword] = keyword

        for it in alias:
            self.data[it] = keyword

    def __repr__(self):
        return repr(self.keyword)

    def __str__(self):
        return self.keyword


df = pd.read_excel('keyword.xlsx')

keywords = []

for i, row in df.iterrows():
    keyword = row['keyword']
    alias = row.iloc[1:][~row.iloc[1:].isna()].to_numpy()
    keywords.append(KeywordMap(keyword, alias))

def get_keyword(name: str) -> KeywordMap:
    for keyword in keywords:
        if name in keyword:
            return keyword
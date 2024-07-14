from functools import cache
from typing import Iterable
from dataclasses import dataclass

import requests


@dataclass
class BalanceInfo:
    address: str
    confirmed: int
    received: int
    txs: int
    unconfirmed: int
    utxo: int


def get_balance_info(address: str) -> BalanceInfo:
    url = f"https://api.blockchain.info/haskoin-store/btc/address/{address}/balance"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Accept": "application"
    }
    resp = requests.get(url, headers=headers).json()
    return BalanceInfo(**resp)


def get_tx_ids(address: str) -> set[str]:
    url = "https://api.blockchain.info/haskoin-store/btc/address/%s/transactions?limit=10000&offset=0" % address
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Accept": "application"
    }
    resp = requests.get(url, headers=headers).json()
    tx_ids = set()
    for e in resp:
        tx_ids.add(e["txid"])
    return tx_ids


@cache
def get_tx_info(tx_id: str) -> dict:
    url = "https://api.blockchain.info/haskoin-store/btc/transaction/" + tx_id
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Accept": "application"
    }
    resp = requests.get(url, headers=headers).json()
    return resp


def get_tx_infos(tx_ids: Iterable[str]) -> list[dict]:
    url = "https://api.blockchain.info/haskoin-store/btc/transactions?txids=" + ",".join(tx_ids)
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Accept": "application"
    }
    resp = requests.get(url, headers=headers).json()  # value에는 100을 나눠야 btc 값이 나옴.
    return resp

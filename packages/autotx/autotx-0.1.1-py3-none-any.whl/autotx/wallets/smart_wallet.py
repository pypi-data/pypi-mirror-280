from abc import abstractmethod

from web3 import Web3
from autotx.intents import Intent
from autotx.utils.ethereum.get_erc20_balance import get_erc20_balance
from autotx.eth_address import ETHAddress
from autotx.utils.ethereum.get_native_balance import get_native_balance


class SmartWallet:
    def __init__(self, web3: Web3, address: ETHAddress):
        self.web3 = web3
        self.address = address

    def on_intents_prepared(self, intents: list[Intent]) -> None:
        pass

    @abstractmethod
    def on_intents_ready(self, intents: list[Intent]) -> bool | str: # True if sent, False if declined, str if feedback
        pass

    def balance_of(self, token_address: ETHAddress | None = None) -> float:
        if token_address is None:
            return get_native_balance(self.web3, self.address)
        else:
            return get_erc20_balance(self.web3, token_address, self.address) 
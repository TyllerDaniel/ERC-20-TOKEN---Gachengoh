from brownie import network,config,accounts
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS =["development","ganache-local", "ganache", "mainnet-fork"]


def get_account(index=None,id=None):

    if index:
        return accounts[index]

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print (accounts[0].balance())
        return accounts [0]
        
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])
   
  


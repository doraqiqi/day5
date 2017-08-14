# Author：zhaoyanqi

#print("this is settings")
TRANSACTION_TYPE = {
    'deposit':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.03},
    'transfer_to':{'action':'minus','interest':0.03},
    'transfer_from':{'action':'plus','interest':0},
    'transfer_to_mall':{'action':'minus','interest':0},
}
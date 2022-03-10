from flask import Flask, jsonify, request

app = Flask(__name__)


#Gets all of the user's addresses
@app.route('/address/{userId}', methods=['GET'])
def getAddresses():
    pass

#Adds new bitcoin address to user's addresses
@app.route('/address/{userId}', methods=['POST'])
def addAddress(newAddress):
    pass

#Gets current balance for a specific bitcoin address
@app.route('/balance/{userId}', methods=['GET'])
def getBalance(address):
    pass

#Gets past transactions for a specific bitcoin address
@app.route('/transactions/{userId}', methods=['GET'])
def getTransactions():

    """
    Return Type:
    [list of transactions]

    transaction structure: ('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 5.3)
    """
    pass

#Gets transfers between all of the user's bitcoin addresses
@app.route('/transfers/{userId}', methods=['GET'])
def getAllTransfers():
    transfers = []
    addresses = getAddresses()
    transactions = {}
    #map each address to it's past transactions
    for address in addresses:
        transactions[address] = getTransactions(address)
    
    #get transactions between every address pair and add them to the return list
    for i in range(len(addresses)):
        for j in range(i + 1, len(addresses)):
            internalTransfers = getTransfers(addresses[i], addresses[j])
            for transfer in internalTransfers:
                transfers.append(transfer)
    
    return transfers
            
#Helper method to get transfers between two addresses
def getTransfers(addressA, addressB):
    transactionsA = getTransactions(addressA)
    transactionsB = getTransactions(addressB)
    transfers = []
    for i in range(len(addressA)):
        for j in range(len(addressB)):
            if matchingTransactions(transactionsA[i], transactionsB[j]):
                transfers.append((transactionsA[i][0], transactionsB[j][0]))
                #since each transaction can only be in a transfer once, we set them to None after adding the transfer to the transfer list 
                transactionsA[i] = None
                transactionsB[j]) = None
    return transfers

#Helper method to determine if two transactions are a part of a transfer
#transaction structure: ('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 5.3)
def matchingTransactions(transactionA, transactionB):
    if (transactionA != None and transactionB != None) and transactionA[4] == transactionB[4] and transactionA[2] == transactionB[2] and transactionA[3] != transactionB[3]:
        return True
    return False 



    


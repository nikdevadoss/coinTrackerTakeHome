"""Transfer detector.

Given a list of withdrawals and desposits, detect the likely transfers amongst them.

A few notes:
- The same withdrawal or deposit cannot be used for multiple different transfers. If there's a case where a given withdrawal or deposit can be matched with multiple possible transfers, use the first occurrence in the list.
- A transfer can only be made between different wallets.

For example, given:
[
	('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 5.3),  # 5.3 BTC was withdrawn out of 'wallet_id_1'
	('tx_id_2', 'wallet_id_1', '2020-01-03 12:05:25 UTC', 'out', 3.2),  # 3.2 BTC was withdrawn out of 'wallet_id_1'
	('tx_id_3', 'wallet_id_2', '2020-01-01 15:30:20 UTC', 'in', 5.3),   # 5.3 BTC was deposited into 'wallet_id_2'
	('tx_id_4', 'wallet_id_3', '2020-01-01 15:30:20 UTC', 'in', 5.3),   # 5.3 BTC was deposited into 'wallet_id_3'
]

Expected output:
[
	('tx_id_1', 'tx_id_3'),
]

Add a few tests to verify your implementation works on a variety of input
"""

def detect_transfers(transactions):
    transfers = []
    for i in range(0, len(transactions)):
        for j in range(0, len(transactions)):
            if i != j and matchingTransactions(transactions[i], transactions[j]):
                transfers.append((transactions[i][0], transactions[j][0]))
                transactions[i] = None
                transactions[j] = None
                break
    return transfers


def matchingTransactions(transactionA, transactionB):
    if (transactionA != None and transactionB != None) and transactionA[3] != transactionB[3] and transactionA[1] != transactionB[1] and transactionA[4] == transactionB[4] and transactionA[2] == transactionB[2]:
        return True
    return False 


def main():
    test_1 = [
	    ('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 5.3),  # 5.3 BTC was withdrawn out of 'wallet_id_1'
	    ('tx_id_2', 'wallet_id_1', '2020-01-03 12:05:25 UTC', 'out', 3.2),  # 3.2 BTC was withdrawn out of 'wallet_id_1'
	    ('tx_id_3', 'wallet_id_2', '2020-01-01 15:30:20 UTC', 'in', 5.3),   # 5.3 BTC was deposited into 'wallet_id_2'
	    ('tx_id_4', 'wallet_id_3', '2020-01-01 15:30:20 UTC', 'in', 5.3),   # 5.3 BTC was deposited into 'wallet_id_3'
    ]


    test_2 = [
	    ('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 1),  
	    ('tx_id_2', 'wallet_id_1', '2020-01-01 12:05:25 UTC', 'out', 1),  
        ('tx_id_3', 'wallet_id_1', '2020-01-03 12:05:25 UTC', 'out', 1),
	    ('tx_id_4', 'wallet_id_2', '2020-01-01 15:30:20 UTC', 'in', 1),   
	    ('tx_id_5', 'wallet_id_3', '2020-01-01 12:05:25 UTC', 'in', 1) 
    ]   

    test_3 = [
	    ('tx_id_1', 'wallet_id_1', '2020-01-01 15:30:20 UTC', 'out', 2),  
	    ('tx_id_2', 'wallet_id_1', '2020-01-03 12:05:25 UTC', 'out', 3),  
        ('tx_id_3', 'wallet_id_1', '2020-01-03 12:05:25 UTC', 'out', 4),
	    ('tx_id_4', 'wallet_id_2', '2020-01-01 15:30:20 UTC', 'in', 1),   
	    ('tx_id_5', 'wallet_id_3', '2020-01-01 15:30:20 UTC', 'in', 6) 
    ]     

    print("test1: ", detect_transfers(test_1))
    print("test2: ", detect_transfers(test_2))
    print("test3: ", detect_transfers(test_3))


if __name__ == "__main__":
    main()


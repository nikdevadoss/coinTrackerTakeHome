To run algorithm.py: 

- python3 algorithm.py


The backend strucure with method stubs is in backend.py, and the database structure is in database.js. I chose to use a noSQL database like MongoDB because we are only storing the userId and a list of the user's bitcoin addresses. As far as the backend, I chose flask because we want to use a bitcoin address API like blockchair to make queries, but other than that most of the API endpoints are simple in the sense that we just need to return information that we get from a single external API call. The only exception to that is the getAllTransfers() method, which requires some computing to get all the past transactions for a user's wallet then figure out which transactions are transfers between their wallets. 
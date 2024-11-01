# Stripe Mini App
This is a mini web application that allows users to select a deposit amount and securely process payments using Stripe. 

## Feature
Select Deposit Amount - Users can choose from preset deposit amounts with easy-to-use buttons.

## Prerequisites
1. Stripe Account - Set up in test mode to simulate payments.
2. Node.js - Only required if using an Express backend for Stripe API calls.
3. Local Server - Use Live Server in VS Code or any other local server for testing.

## Deployment and Execution
1. Clone the repository and navigate to the project folder:
      git clone [https://github.com/your-username/your-repository](https://github.com/Kaja6/OnlineGambling)
      cd OnlineGambling
2. Configure Stripe API Key in index.html:
      const stripe = Stripe('pk_test_51QFyQqP5YDh8SlQPrC0Es3zPkUABUkVLCisITVjsOjx5tRYFHYVhzRLjthKkpu1TCQdaHMnKj8pczEg63h1x8TAg00ODZbwhu4'); 
3. Run the Application with a local server (e.g., use Live Server in VS Code) to serve index.html.

## Note
The app is currently in test mode with Stripe. Use Stripe test card numbers to simulate payments.

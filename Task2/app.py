from flask import Flask, render_template, request, jsonify
import stripe

app = Flask(__name__)

stripe.api_key = "sk_test_51QFyQqP5YDh8SlQPLahVUEGpq7pYr139yt2zHAOwxts4NbUKXOYsQdKjWVEvc8eluO3Rx2T3AUWv9Xc5bXwVROFp00lq7gDJk2"  # My Secret Key
publishable_key = "pk_test_51QFyQqP5YDh8SlQPrC0Es3zPkUABUkVLCisITVjsOjx5tRYFHYVhzRLjthKkpu1TCQdaHMnKj8pczEg63h1x8TAg00ODZbwhu4"  # My Publishable Key

@app.route('/')
def index():
    return render_template('index.html', key=publishable_key)

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        amount = request.form['amount']
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount),  # Amount in cents
            currency='eur',  # Use the appropriate currency
        )
        return jsonify({'clientSecret': payment_intent['client_secret']})
    except Exception as e:
        return jsonify(error=str(e)), 403

#@app.route('/charge', methods=['POST'])
#def charge():
#    amount = request.form['amount']  # Get the amount from the form
#    try:
#        # Create a new charge
#        charge = stripe.Charge.create(
#            amount=int(amount) * 100,  # Amount in cents
#            currency='eur',  # currency
#            description='Payment for deposit',
#            source=request.form['stripeToken']  # Source is the token returned from Stripe
#        )
#        return jsonify({"status": "success", "charge": charge})
#    except stripe.error.StripeError as e:
#        return jsonify({"status": "error", "message": str(e)})

# Placeholder route to handle form submission
#@app.route('/create-checkout-session', methods=['POST'])
#def create_checkout_session():
#    amount = request.form.get('amount')  # get the amount from the form
#    # For now, just print the amount (we'll integrate Stripe here later)
#    print(f"Selected amount: {amount}")
#    return f"Amount {int(amount) / 100}€ selected!"

if __name__ == '__main__':
    app.run(debug=True)

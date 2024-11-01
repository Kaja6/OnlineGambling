from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = '7450749637:AAFs-1ssE_TEhQ6wzZUwrVP-bvz5PUowJeQ'

# Initialization of the application
application = ApplicationBuilder().token(TOKEN).build()

# Respond to the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = (
        "🎉 Welcome to **LuckyBetBot**, where every roll is a new chance! 🎲\n\n"
        "Are you ready to take a spin and see where luck leads you? 💰✨\n\n"
        "Here’s how to get started:\n"
        "- 💳 **/balance** - Keep track of your treasure! Check your balance anytime.\n"
        "- 🎯 **/bet** - Got a good feeling? Place your bet and let’s see what happens! 💸\n\n"
        "The night is young, and the games await! If you need guidance, just ask. May luck be on your side! 🍀"
    )
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

# Dictionary to store user balances
user_balances = {}
# Function to initialize a new user's balance if they don't have one
def get_user_balance(user_id):
    if user_id not in user_balances:
        user_balances[user_id] = 1000  # Start each user with $1000 as an example
    return user_balances[user_id]

# Respond to the /balance command
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    balance = get_user_balance(user_id)
    await update.message.reply_text(
        f"👀 Checking the wallet… you’ve got **{balance} EUR**. Not bad! Time to double it, maybe? 🍀",
        parse_mode='Markdown'
    )


# Command to display betting options
async def bet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Bet options as buttons
    keyboard = [
        [InlineKeyboardButton("5 EUR", callback_data='5')],
        [InlineKeyboardButton("10 EUR", callback_data='10')],
        [InlineKeyboardButton("50 EUR", callback_data='50')],
        [InlineKeyboardButton("100 EUR", callback_data='100')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
 # Send the message with inline buttons
    await update.message.reply_text("How lucky do  you feel? Choose your bet amount:", reply_markup=reply_markup)

# Callback function to handle button presses for betting
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    bet_amount = int(query.data)  # Retrieve the bet amount from the callback data

# Check and update balance
    balance = get_user_balance(user_id)
    if balance >= bet_amount:
        user_balances[user_id] -= bet_amount
        await query.answer() 
        await query.edit_message_text(
            text=f"You placed a bet of {bet_amount} EUR! 🎉 Your new balance is {user_balances[user_id]} EUR. Good luck! 🍀"
        )
    else:
        await query.answer() 
        await query.edit_message_text(
            text="🚫 Insufficient balance to place this bet. Please check your balance with /balance."
        )

print("Bot is running...")

# Setting up the bot with the command and callback handlers
def main() -> None:
    #application = Application.builder().token("YOUR_TOKEN_HERE").build()

    # Register the /start, /balance and /bet commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("balance", balance))
    application.add_handler(CommandHandler("bet", bet))

    # Register the callback handler for button presses
    application.add_handler(CallbackQueryHandler(button_callback))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()

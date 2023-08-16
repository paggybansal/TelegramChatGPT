import telegram
from telegram.ext import Updater, MessageHandler, filters
import requests

# Initialize the Telegram Bot API
bot_token = '6415069814:AAHwPW6-mJKXqF308pYIOFcOKEA-BBRP3AA'
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


# Define a function to interact with GPT-3
def generate_gpt_response(prompt):
    api_key = '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'
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'prompt': prompt,
        'max_tokens': 100
    }

    response = requests.post(url, json=data, headers=headers)
    generated_text = response.json()['choices'][0]['text']
    return generated_text


# Define a message handler function
def handle_message(update, context):
    user_input = update.message.text
    gpt_response = generate_gpt_response(user_input)
    update.message.reply_text(gpt_response)


# Register the message handler with the dispatcher
message_handler = MessageHandler(filters.text & ~filters.command, handle_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()

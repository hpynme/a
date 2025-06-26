import os
from telegram.ext import Updater, CommandHandler

# আপনার বট টোকেন এনভায়রনমেন্ট ভেরিয়েবল থেকে লোড হবে
TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text('হ্যালো! আমি আপনার নতুন বট।')

def main():
    if not TOKEN:
        print("ত্রুটি: টেলিগ্রাম টোকেন পাওয়া যায়নি। 'TOKEN' এনভায়রনমেন্ট ভেরিয়েবল সেট করুন।")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    # বট শুরু করুন
    updater.start_polling()
    # বট বন্ধ না হওয়া পর্যন্ত অপেক্ষা করুন
    updater.idle()

if __name__ == '__main__':
    main()

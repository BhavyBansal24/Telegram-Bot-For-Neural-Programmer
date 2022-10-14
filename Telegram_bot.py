import telegram.ext

Token = "Token received from BotFather at telegram"
updater = telegram.ext.updater(Token, use_context=True)
dispatcher = updater.Dispatcher


def start(update, context):
    update.message.reply_text("Hello! Welcome to Neural_Programmer")


def help(update, context):
    update.message.reply_text(
        """
        /start - Welcome to Neural_Programmer

        /help - This Message

        projects
        /project_1 - UltraSound8k
        /project_2 - Tomato-Plant-Disease-detector
        /project_3 - WhatsApp-Chat-Analyzer
        /project_4 - Backend using MERN Development
        /project_5 - NFT-Marketplace
        /project_6 - Telegram-Bot
        /project_7 - Neural_Programmer website

        Social Media Links
        /github - Github
        /kaggle - Kaggle
        /linkedin - Linkedin
        /twitter - Twitter
        /instagram - Instagram
        /youtube - Youtube
        /medium - Medium
        
        About Neural_Programmer
        /website - Neural_Programmer Website
        /creator - Bot Creator
        """
    )


def project_1(update, context):
    update.message.reply_text(
        "UltraSound8k : https://bhavybansal24-urbansound8k-app-0fbs20.streamlitapp.com/")


def project_2(update, context):
    update.message.reply_text(
        "Tomato-Plant-Disease-detector : https://bhavybansal24-tomato-plant-disease-detector-app-jo66w9.streamlitapp.com/")


def project_3(update, context):
    update.message.reply_text(
        "WhatsApp-Chat-Analyzer : https://whatsapp-chat-analyzer-bhavy.herokuapp.com/")


def project_4(update, context):
    update.message.reply_text(
        "Backend using MERN Development : https://github.com/BhavyBansal24/Shoping-MERN-WebApp")


def project_5(update, context):
    update.message.reply_text(
        "NFT-Marketplace : https://github.com/BhavyBansal24/nft-marketplace")


def project_6(update, context):
    update.message.reply_text("You are using it NOW!")


def project_7(update, context):
    update.message.reply_text(
        "Neural_Programmer website : https://bhavybansal24.github.io/Neural-Programmer/")


def github(update, context):
    update.message.reply_text("Github : https://github.com/BhavyBansal24")


def kaggle(update, context):
    update.message.reply_text("Kaggle : https://www.kaggle.com/bhavybansal")


def linkedin(update, context):
    update.message.reply_text(
        "Linkedin : https://www.linkedin.com/in/bhavybansal24/")


def twitter(update, context):
    update.message.reply_text("Twitter : https://twitter.com/BhavyBansal_24")


def instagram(update, context):
    update.message.reply_text(
        "Instagram : https://www.instagram.com/bhavybansal_24/")


def youtube(update, context):
    update.message.reply_text(
        "Youtube : https://www.youtube.com/channel/UCgr34x_pN-FIm952wfBOR5g")


def medium(update, context):
    update.message.reply_text("Medium : https://medium.com/@bansal1232.bhavy")


def website(update, context):
    update.message.reply_text(
        "Neural_Programmer Website : https://bhavybansal24.github.io/Neural-Programmer/")


def creator(update, context):
    update.message.reply_text("Creator : Bhavy Bansal")


dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
dispatcher.add_handler(telegram.ext.CommandHandler("project_1", project_1))
dispatcher.add_handler(telegram.ext.CommandHandler("project_2", project_2))
dispatcher.add_handler(telegram.ext.CommandHandler("project_3", project_3))
dispatcher.add_handler(telegram.ext.CommandHandler("project_4", project_4))
dispatcher.add_handler(telegram.ext.CommandHandler("project_5", project_5))
dispatcher.add_handler(telegram.ext.CommandHandler("project_6", project_6))
dispatcher.add_handler(telegram.ext.CommandHandler("project_7", project_7))
dispatcher.add_handler(telegram.ext.CommandHandler("github", github))
dispatcher.add_handler(telegram.ext.CommandHandler("Kaggle", kaggle))
dispatcher.add_handler(telegram.ext.CommandHandler("linkedin", linkedin))
dispatcher.add_handler(telegram.ext.CommandHandler("twitter", twitter))
dispatcher.add_handler(telegram.ext.CommandHandler("instagram", instagram))
dispatcher.add_handler(telegram.ext.CommandHandler("youtube", youtube))
dispatcher.add_handler(telegram.ext.CommandHandler("medium", medium))
dispatcher.add_handler(telegram.ext.CommandHandler("website", website))
dispatcher.add_handler(telegram.ext.CommandHandler("Creator", creator))

updater.start_polling()
updater.idle()

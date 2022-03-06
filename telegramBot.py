from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = "5206564396:AAEJRIeSuZ_2wBnMGUAEwPGekXw3b1Ps1qo"

def start(update, context):
    update.message.reply_text("""
Bienvenue sur le bot officiel de tcollart.

Les commandes disponibles sont :
- /site pour obtenir l'adresse du site
- /youtube pour obtenir la chaîne YouTube
- /linkedin pour obtenir son profil Linkedin
    """)

def site(update, context):
    update.message.reply_text('https://www.commentcoder.com')


def youtube(update, context):
    update.message.reply_text('https://www.youtube.com/channel/UCEztUC2WwKEDkVl9c6oUoTw')


def linkedin(update, context):
    update.message.reply_text('https://www.linkedin.com/in/thomascollart')


def pas_compris(update, context):
    update.message.reply_text('Je n\'ai pas compris votre message "', update.message.text,)


def main():
    # La classe Updater permet de lire en continu ce qu'il se passe sur le channel
    updater = Updater(TOKEN, use_context=True)

    # Pour avoir accès au dispatcher plus facilement
    dp = updater.dispatcher

    # On ajoute des gestionnaires de commandes
    # On donne a CommandHandler la commande textuelle et une fonction associée
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("youtube", youtube))
    dp.add_handler(CommandHandler("linkedin", linkedin))
    # Pour gérer les autres messages qui ne sont pas des commandes
    dp.add_handler(MessageHandler(Filters.text, pas_compris))

    # Sert à lancer le bot
    updater.start_polling()

    # Pour arrêter le bot proprement avec CTRL+C
    updater.idle()


if __name__ == '__main__':
    main()
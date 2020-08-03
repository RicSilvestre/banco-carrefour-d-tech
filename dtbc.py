import telebot

KEY = ""

bot = telebot.TeleBot(KEY)

@bot.message_handler(commands=["start"])
def funcao_start(session):
    bot.reply_to(session, """Boas vindas à central de soluções do cartão do Banco Carrefour! Aqui você pode:
    1 – Solicitar segunda via de fatura
    2 – Gerenciar seus avisos do Banco Carrefour
    3 – Solucionar outros problemas
    O que você deseja?""")

    @bot.message_handler(commands=["1", "2", "3"])
    def opcoes(session):
        if session.text == "/1":
            bot.reply_to(session, "Olá, tudo bem? Aparentemente você deseja gerar uma segunda via " 
            "de sua fatura, está bem, aqui está o arquivo: link.bancocarrefour.jpg. Volte sempre!")


        elif session.text == "/2":
            bot.reply_to(session, "Olá, tudo bem? Vimos que você gostaria de receber avisos sobre o "
            "vencimento da fatura. As opções diponíveis são: e-mail, mensagem ou telegram. Qual você deseja?")

            @bot.message_handler(commands=["email", "mensagem","telegram"])
            def avisos(session):
                if session.text == "/email":
                    bot.reply_to(session, "Está bem! Iremos enviar um aviso por e-mail. Volte sempre!")


                elif session.text == "/mensagem":
                    bot.reply_to(session, "Está bem! Iremos enviar um aviso por mensagem. Volte sempre!")


                elif session.text == "/telegram":
                    bot.reply_to(session, "Está bem! Iremos enviar um aviso por telegram. Volte sempre!")

                else:
                    bot.reply_to(session, "Isso não é uma opção válida, por favor, tente outra vez.")

                

        elif session.text == "/3":
            bot.reply_to(session, "Vimos que realmente nenhuma das outras opções condiz "
            "com sua necessidade, assim sendo, para que seu problema possa ser resolvido, deseja "
            "que um de nossos funcionários entre em contato com você? Digite sim em caso de afimartiva, "
            "ou não, caso queira encerrar o atendimento")

            @bot.message_handler(commands=["sim", "não"])
            def contato(session):
                if session.text == "/sim":
                    bot.reply_to(session, "Ok! Um de nossos funcionários entrará em contato "
                    "com você pelo Telegram o mais rápido possível, até logo!")

                elif session.text == "/não":
                    bot.reply_to(session, "Está bem, sua escolha será respeitada. "
                    "Caso ainda deseje tentar resolver de outras formas, nosso número de "
                    "atendimento é 0800-718-2222. Esperamos que consiga solucionar "
                    "seu problema. Até logo!")

                else:
                    bot.reply_to(session, "Isso não é uma opção válida, por favor, tente outra vez.")


            

        else:
            bot.reply_to(session, "Isso não é uma opção válida, por favor, tente outra vez.")



bot.polling()


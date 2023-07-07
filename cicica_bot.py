"""
CICICA TelegramBot

Author: Mariana Chung Garita
Project: CICICA TelegramBot
Student ID: B92250
"""
# The libraries required for the development of the bot are imported
import telebot
from telebot import types
import webparser
import requests


def main(token):
    """
    Entry point of the CICICA TelegramBot.

    Args:
        token (str): The token required to connect to the Telegram Bot API.

    Returns:
        None
    """
    # Declaring the variable to identify the telebot.
    cicica_bot = telebot.TeleBot(token)

    # Creating a message handler specifically to start the bot.
    @cicica_bot.message_handler(func = lambda message: message.text in ['Hola', 'hola', 'Start',
                                                                   'iniciar', 'Hi', 'Restart', 'Inicio', 'inicio', 'Atrás', '/start'])
    
    def start(message):
        """
        Handler for the start message.

        Args:
            message (telebot.types.Message): The message object received.

        Returns:
            None
        """
        # Calls the "seleccion_lenguaje" function
        markup = seleccion_lenguaje()

        # Sends the message and adds the markup (buttons)
        cicica_bot.send_message(
            message.chat.id,
            "Select your language / Selecciona tu idioma:",
            reply_markup = markup
        )

    def seleccion_lenguaje():
        """
        Generates and returns the language selection keyboard markup.

        Returns:
            telebot.types.ReplyKeyboardMarkup: The generated keyboard markup.
        """
        # Creating the buttons for the languages
        markup = types.ReplyKeyboardMarkup(row_width=2)
        spanish = types.KeyboardButton('Español')
        english = types.KeyboardButton('English')
        markup.add(spanish, english)
        return markup
    
    # Creating a message handler specifically to slect the language.    
    @cicica_bot.message_handler(func = lambda message: message.text in ['Español', 'English'])
    def menu_setup(message):
        """
        Handle the menu setup based on the selected language.

        Args:
            message (obj): The message object.

        Returns:
            None
        """
        if message.text == 'Español':
            # Creating a menu with several button options
            markup = types.ReplyKeyboardMarkup(row_width = 2)
            location_button = types.KeyboardButton('\U0001F4CD Ubicación')
            hours_button = types.KeyboardButton('\U0001F554 Horario')
            tests_buttons = types.KeyboardButton('\U0001F52C Pruebas')
            directory_button = types.KeyboardButton('\U0001F4DE Contacto')
            other_button = types.KeyboardButton('Otras opciones')
            help_button = types.KeyboardButton('\U0001F198 Ayuda')
            markup.add(location_button, hours_button, tests_buttons, directory_button, other_button, help_button)
            # Sending the welcome message with a photo and show the menu
            photo = 'https://semanariouniversidad.com/wp-content/uploads/2022/05/Fotografia-del-equipo-1024x691.jpg'
            mensaje = ('¡Bienvenid@! \U0001F44B\n Soy el TelegramBot del CICICA \n ¿Como puedo ayudarte?')
            cicica_bot.send_photo(message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)
            
        if message.text == 'English':
            # Creating a menu with several button options
            markup = types.ReplyKeyboardMarkup(row_width = 2)
            location_button = types.KeyboardButton('\U0001F4CD Location')
            hours_button = types.KeyboardButton('\U0001F554 Working_hours')
            tests_buttons = types.KeyboardButton('\U0001F52C Tests')
            directory_button = types.KeyboardButton('\U0001F4DE Contact')
            other_button = types.KeyboardButton('Other options')
            help_button = types.KeyboardButton('\U0001F198 Help')
            markup.add(location_button, hours_button, tests_buttons, directory_button, other_button, help_button)
            # Sending the welcome message with a photo and show the menu
            photo = 'https://semanariouniversidad.com/wp-content/uploads/2022/05/Fotografia-del-equipo-1024x691.jpg'
            mensaje = '¡Welcome! \U0001F44B\n I\'m the CICICA TelegramBot \n ¿How can I help you?'
            cicica_bot.send_photo(message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

    # Creating a message handler specifically to respond a "Thank you".
    @cicica_bot.message_handler(func = lambda message: message.text in ['Gracias', 'gracias'])
    def con_gusto(message):
        """
        Sends a message with a greeting.
        :param message: The incoming message object.
        """
        cicica_bot.send_message(message.chat.id, 'Con mucho gusto \U0001F609')
    
    @cicica_bot.message_handler(func = lambda message: message.text in ['Thanks', 'thanks'])
    def con_gusto_en(message):
        """
        Sends a message with a greeting.
        :param message: The incoming message object.
        """
        cicica_bot.send_message(message.chat.id, 'Your welcome! \U0001F609')
                                
    # Creating a message handler specifically to respond the english menu.
    @cicica_bot.message_handler(func = lambda message: message.text in ['\U0001F4CD Location', '\U0001F554 Working_hours',
                                                                       '\U0001F52C Tests', '\U0001F4DE Contact', 'Other options', '\U0001F198 Help'])
    def menu_handler(message):
        """
        Handle menu options.

        Args:
            message (telebot.types.Message): The message object.

        Returns:
            None
        """
        if message.text == '\U0001F198 Help':
            cicica_bot.send_message(message.chat.id, '*Command Menu* \n\n' 
                                    '*Language* \n'
                                    'Español - Select Spanish language  \n'
                                    'English - Select English language \n\n'
                                    '*Principal Menu* \n'
                                    '\U0001F4CD Location - Location of the CICICA building \n'
                                    '\U0001F554 Working Hours - Building Hours \n'
                                    '\U0001F52C Tests - Available tests and their information \n'
                                    '\U0001F4DE Contact - Building number \n'
                                    'Other options - Entrance of private vehicles, Social Networks and informative videos', parse_mode='Markdown')
            
        if message.text == '\U0001F4CD Location':
            markup = types.InlineKeyboardMarkup()
            waze = types.InlineKeyboardButton(text ='Waze Link', callback_data ='waze_en')
            map = types.InlineKeyboardButton(text ='Google Maps Link', callback_data ='maps_en')
            markup.row(waze)
            markup.row(map)

            direction = (
                ' \U0001F4CD San Jose (CR), Montes de Oca, San Pedro, Universidad de Costa Rica, '
                'Ciudad de la investigacion. Centro de Investigacion en Cirugia y Cancer'
            )
            photo = 'https://cicica.ucr.ac.cr/sites/default/files/styles/large/public/2023-03/301603829_509221341205881_1286055969924390298_n-3.jpg?itok=hx8Ppx6z'
            cicica_bot.send_photo(message.chat.id, photo, caption= direction)
            cicica_bot.send_message(message.chat.id, 'Other options', reply_markup = markup)

        if message.text == '\U0001F554 Working_hours':
            cicica_bot.send_message(message.chat.id, '\U0001F554 Working Hours:\n'
                                        'Monday to Friday 8:00 am - 5:00 pm\n'
                                        'Saturday to Sunday CLOSED\n')

        if message.text == '\U0001F52C Tests':
            cicica_bot.send_message(message.chat.id, 'Gathering information.\n'
                                    'Please wait, this can take around 45 seconds.')
            info_en = webparser.web_parser_en
            info_list_en = info_en()
            markup = types.InlineKeyboardMarkup()
            secuenciacion_btn = types.InlineKeyboardButton(info_list_en[1], callback_data ='psc_en')
            hpv_btn = types.InlineKeyboardButton(info_list_en[4], callback_data ='hpv_gin_en')
            hpv_lab_btn = types.InlineKeyboardButton(info_list_en[7], callback_data ='hpv_lab_en')
            c_sut_btn = types.InlineKeyboardButton(info_list_en[10], callback_data ='c_sut_en')
            c_laparo_btn = types.InlineKeyboardButton(info_list_en[13], callback_data ='c_laparo_en')
            tox_btn = types.InlineKeyboardButton(info_list_en[16], callback_data ='tox_en')
            pcr_btn = types.InlineKeyboardButton(info_list_en[19], callback_data ='pcr_en')
            bio_btn = types.InlineKeyboardButton(info_list_en[22], callback_data ='bio_en')
            markup.row(secuenciacion_btn)
            markup.row(hpv_btn)
            markup.row(hpv_lab_btn)
            markup.row(c_sut_btn)
            markup.row(c_laparo_btn)
            markup.row(tox_btn)
            markup.row(pcr_btn)
            markup.row(bio_btn)

            cicica_bot.reply_to(message, 'These are the tests available:', reply_markup = markup)

        if message.text == '\U0001F4DE Contact':
            cicica_bot.reply_to(message, '\U0001F4DE Contacts:\n'
                                        '2511-3322\n'
                                        'If you wish to make the call, click on the number')
        
        if message.text == 'Other options':
            markup = types.InlineKeyboardMarkup()
            entrance = types.InlineKeyboardButton('Entrance of private vehicles', url ='https://www.google.com/maps/place/Entrada+vehicular+principal:+Ciudad+de+la+Investigacion+(UCR)/@9.9350731,-84.0449827,18z/data=!4m6!3m5!1s0x8fa0e3891c930363:0x95f412891069878a!8m2!3d9.9347717!4d-84.0456184!16s%2Fg%2F11cmds54w9?entry=ttu')
            social = types.InlineKeyboardButton(text ='Social networks', callback_data ='social_en')
            videos = types.InlineKeyboardButton(text ='Informative videos', callback_data ='videos_en')
            markup.row(entrance)
            markup.row(social)
            markup.row(videos)
            cicica_bot.reply_to(message, 'Other options', reply_markup = markup)


        @cicica_bot.callback_query_handler(func = lambda call: True)
        def callback_answers(call):
            """
            Callback function for handling user interactions.
            Args:
                call (telegram.CallbackQuery): The callback query object.
            Returns:
                None
            """

            if call.data == 'psc_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                global nombre_prueba_en
                nombre_prueba_en = 'Capillary Sequencing Test'
                mensaje = ('*Capillary Sequencing Test* \n Price: %s \n  %s' % (info_list_en[2], info_list_en[3]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Buy', url ='https://www-ucrenlinea-com.translate.goog/products/220/prueba-secuenciacion-capilar?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui')
                correo_btn = types.InlineKeyboardButton('Contact by mail', callback_data='correo_en')
                markup.row(link_btn)
                markup.row(correo_btn)
                photo = 'https://media.nidux.net/pull/800/599/10564/220-product-624b6e197e8ae-b8fcf34e-cc01-4c84-92a1-66367a46f85d.jfif'
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'hpv_gin_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                nombre_prueba_en = 'OncoTect HPV test for gynecologists'
                mensaje = ('*OncoTect HPV test for gynecologists* \n Price: %s \n  %s' % (info_list_en[5], info_list_en[6]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Buy', url ='https://www-ucrenlinea-com.translate.goog/products/132/prueba-hpv-oncotect-para-ginecologos?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui')
                correo_btn = types.InlineKeyboardButton('Contact by mail', callback_data='correo_en')
                markup.row(link_btn)
                markup.row(correo_btn)
                photo = 'https://media.nidux.net/pull/800/599/10564/132-product-60ccc69dc1a58-ginecologos.png'
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'hpv_lab_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                nombre_prueba_en = 'OncoTect HPV test for laboratories'
                mensaje = ('*OncoTect HPV test for laboratories* \n Price: %s \n  %s' % (info_list_en[8], info_list_en[9]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Buy', url ='https://www-ucrenlinea-com.translate.goog/products/131/prueba-hpv-oncotect-para-laboratorios?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui')
                correo_btn = types.InlineKeyboardButton('Contact by mail', callback_data='correo_en')
                markup.row(link_btn)
                markup.row(correo_btn)
                photo = 'https://media.nidux.net/pull/800/599/10564/131-product-60ccbf93506db-laboratorios.png'
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'c_sut_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                nombre_prueba_en = 'Surgical Suture Technique Course'
                mensaje = ('*Surgical Suture Technique Course* \n Price: %s \n  %s' % (info_list_en[11], info_list_en[12]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Buy', url ='https://www-ucrenlinea-com.translate.goog/products/293/curso-tecnica-de-suturas-quirurgicas?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui')
                correo_btn = types.InlineKeyboardButton('Contact by mail', callback_data='correo_en')
                markup.row(link_btn)
                markup.row(correo_btn)
                photo = 'https://media.nidux.net/pull/800/599/10564/293-product-63447c45ca7e4-foto-1.jpeg'
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'c_laparo_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                nombre_prueba_en = 'Basic Laparoscopy Course for General Practitioners'
                mensaje = ('*Basic Laparoscopy Course for General Practitioners* \n Price: %s \n  %s' % (info_list_en[14], info_list_en[15]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Buy', url ='https://www-ucrenlinea-com.translate.goog/products/292/curso-basico-de-laparoscopia-para-medicos-generales?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui')
                correo_btn = types.InlineKeyboardButton('Contact by mail', callback_data='correo_en')
                markup.row(link_btn)
                markup.row(correo_btn)
                photo = 'https://media.nidux.net/pull/800/599/10564/292-product-6344785998e3e-dsc-8689.jpg'
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'tox_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                nombre_prueba_en = 'Toxicity in Fluoropyrimidines (5-FU)'
                mensaje = ('*Toxicity in Fluoropyrimidines (5-FU)* \n Price: %s \n  %s' % (info_list_en[17], info_list_en[18]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Buy', url ='https://www-ucrenlinea-com.translate.goog/products/314/toxicidad-en-fluoropirimidinas-5-fu?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui')
                correo_btn = types.InlineKeyboardButton('Contact by mail', callback_data='correo_en')
                markup.row(link_btn)
                markup.row(correo_btn)
                photo = 'https://media.nidux.net/pull/800/599/10564/314-product-63d3ec6aea328-5-fu.png'
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'pcr_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                nombre_prueba_en = 'Real PCR for detection of HPV serotypes'
                mensaje = ('*Real PCR for detection of HPV serotypes* \n Price: %s \n  %s' % (info_list_en[20], info_list_en[21]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Buy', url ='https://www-ucrenlinea-com.translate.goog/products/325/pcr-real-para-deteccion-de-serotipos-de-hpv?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui')
                correo_btn = types.InlineKeyboardButton('Contact by mail', callback_data='correo_en')
                markup.row(link_btn)
                markup.row(correo_btn)
                photo = 'https://media.nidux.net/pull/800/599/10564/325-product-643584b15dd60-dsc-6521.jpg'
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'bio_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                nombre_prueba_en = 'Vacuum biopsy training workshop for early detection of breast cancer'
                mensaje = ('*Vacuum biopsy training workshop for early detection of breast cancer* \n Price: %s \n  %s' % (info_list_en[23], info_list_en[24]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Buy', url ='https://www-ucrenlinea-com.translate.goog/products/339/taller-de-entrenamiento-en-biopsia-al-vacio-para-deteccion-temprana-de-cancer-de-mama?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui')
                correo_btn = types.InlineKeyboardButton('Contact by mail', callback_data='correo_en')
                markup.row(link_btn)
                markup.row(correo_btn)
                photo = 'https://media.nidux.net/pull/800/599/10564/339-product-6470d7c6d55be-imagen-taller-de-biopsia-al-vacio-1.jpg'
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data =='correo_en':
                cicica_bot.send_message(call.message.chat.id, 'Please, send me your name:')
                cicica_bot.register_next_step_handler(message, guardar_nombre_en)
            if call.data =='no_en':
                cicica_bot.send_message(call.message.chat.id, 'Hit the "Contact by mail" button again')
            if call.data == 'si_en':
                correo_destino = 'cicica@ucr.ac.cr'  
                mensaje = f'Hola! \n De parte del CICICA_Bot, el usuario {nombre_en}. Esta interesado en {nombre_prueba_en} \n Informacion: \n Nombre: {nombre_en}\n Cedula: {cedula_en}\n Conctacto:{contacto_en}'
                asunto = 'CICICA_Bot'
                sendgrid_api_key = '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'  
                url = 'https://api.sendgrid.com/v3/mail/send'
                headers = {'Authorization': f'Bearer {sendgrid_api_key}', 'Content-Type': 'application/json'}
                payload = {
                    'personalizations': [{'to': [{'email': correo_destino}]}],
                    'from': {'email': 'cicicatelegrambot@hotmail.com'},  
                    'subject': asunto,
                    'content': [{'type': 'text/plain', 'value': mensaje}]
                }
                response = requests.post(url, headers=headers, json=payload)


                if response.status_code == 202:
                    cicica_bot.send_message(call.message.chat.id, 'I have sent an email to CICICA, to inform them about your interest in the test')
                else:
                    print('Error sending the mail')

            if call.data == 'waze_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                cicica_bot.send_message(call.message.chat.id, ' https://www.waze.com/es/live-map/directions/cr/san-jose/san-jose/centro-de-investigacion-en-cirugia-y-cancer-(cicica-or-ucr)?to=place.ChIJ04Ci2uzjoI8RwLhqJfO_sPY')

            if call.data == 'maps_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                cicica_bot.send_message(call.message.chat.id, 'https://www.google.com/maps/place/Centro+de+Investigaci%C3%B3n+en+Cirug%C3%ADa+y+C%C3%A1ncer+(CICICA+%7C+UCR)/@9.9402232,-84.0444673,15z/data=!4m6!3m5!1s0x8fa0e3ecdaa280d3:0xf6b0bff3256ab8c0!8m2!3d9.9402232!4d-84.0444673!16s%2Fg%2F11h5s46xgk ')

            if call.data == 'social_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                markup = types.InlineKeyboardMarkup()
                insta_btn = types.InlineKeyboardButton('Instagram', url ='https://www.instagram.com/cicica.ucr/')
                face_btn = types.InlineKeyboardButton('Facebook', url ='https://www.facebook.com/CicicaUCR')
                markup.row(insta_btn)
                markup.row(face_btn)
                cicica_bot.send_message(call.message.chat.id, 'Social Networks', reply_markup = markup)

            if call.data == 'videos_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                markup = types.InlineKeyboardMarkup()
                v1_btn = types.InlineKeyboardButton('DCLAB Solution', callback_data='v_1_en')
                v2_btn = types.InlineKeyboardButton('DCLab Transdisciplinary Space', callback_data='v_2_en')
                v3_btn = types.InlineKeyboardButton('DCLab Alianzas', callback_data='v_3_en')
                v4_btn = types.InlineKeyboardButton('Javier Mora', callback_data='v_4_en')
                v5_btn = types.InlineKeyboardButton('Denis Chaves', callback_data='v_5_en')
                v6_btn = types.InlineKeyboardButton('Ricardo Chinchilla', callback_data='v_6_en')
                v7_btn = types.InlineKeyboardButton('Marco Zúñiga', callback_data='v_7_en')
                v8_btn = types.InlineKeyboardButton('Rodrigo Mora', callback_data='v_8_en')
                v9_btn = types.InlineKeyboardButton('Yamileth Angulo', callback_data='v_9_en')
                v10_btn = types.InlineKeyboardButton('Vivian Vilchez', callback_data='v_10_en')
                v11_btn = types.InlineKeyboardButton('Francisco Siles', callback_data='v_11_en')
                v12_btn = types.InlineKeyboardButton('Cristian Marín', callback_data='v_12_en')
                v13_btn = types.InlineKeyboardButton('Community Action: Surgery and Cancer Teaching Laboratory (VAS-UCR, 2021)',callback_data='v_13_en')
                markup.row(v1_btn)
                markup.row(v2_btn)
                markup.row(v3_btn)
                markup.row(v4_btn)
                markup.row(v5_btn)
                markup.row(v6_btn)
                markup.row(v7_btn)
                markup.row(v8_btn)
                markup.row(v9_btn)
                markup.row(v10_btn)
                markup.row(v11_btn)
                markup.row(v12_btn)
                markup.row(v13_btn)
                cicica_bot.send_message(message.chat.id, '\U0001F3A5 Videos:', reply_markup = markup)

            if call.data == 'v_1_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_1 = 'C:/Users/Melissa/Desktop/CICICA Bot/cicica/DCLab Solución.mp4'
                video = open(video_1, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='DCLAB Solution')
            if call.data == 'v_2_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_2 = 'cicica/DCLab Espacio Transdisciplinar.mp4'
                video = open(video_2, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption= 'DCLab Transdisciplinary Space')
            if call.data == 'v_3_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_3 = 'cicica/DCLab Alianzas.mp4'
                video = open(video_3, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='DCLab Alliances')
            if call.data == 'v_4_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_4 = 'cicica/Javier Mora.mp4'
                video = open(video_4, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Javier Mora')
            if call.data == 'v_5_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_5 = 'cicica/Denis Chaves.mp4'
                video = open(video_5, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Denis Chaves')
            if call.data == 'v_6_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_6 = 'cicica/Ricardo Chinchilla.mp4'
                video = open(video_6, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Ricardo Chinchilla')
            if call.data == 'v_7_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_7 = 'cicica/Marco Zúñiga.mp4'
                video = open(video_7, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Marco Zúñiga')
            if call.data == 'v_8_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_8 = 'cicica/Rodrigo Mora.mp4'
                video = open(video_8, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Rodrigo Mora')
            if call.data == 'v_9_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_9 = 'cicica/Yamileth Angulo.mp4'
                video = open(video_9, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Yamileth Angulo')
            if call.data == 'v_10_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_10 = 'cicica/Vivian Vilchez.mp4'
                video = open(video_10, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Vivian Vilchez')
            if call.data == 'v_11_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_11 = 'cicica/Francisco Siles.mp4'
                video = open(video_11, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Francisco Siles')
            if call.data == 'v_12_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_12 = 'cicica/Cristian Marín.mp4'
                video = open(video_12, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Cristian Marín')
            if call.data == 'v_13_en':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_13 = 'cicica/Acción en Comunidad_ Laboratorio de Docencia en Cirugía y Cáncer (VAS-UCR, 2021).mp4'
                video = open(video_13, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Community Action: Surgery and Cancer Teaching Laboratory (VAS-UCR, 2021)')
            

    @cicica_bot.message_handler(func=lambda message: message.text in ['\U0001F4CD Ubicación', '\U0001F554 Horario',
                                                                       '\U0001F52C Pruebas', '\U0001F4DE Contacto', 'Otras opciones', '\U0001F198 Ayuda']) 
    def menu_handler(message):
        """
        Handle the menu messages.

        Args:
            message: The message object received from the user.

        Returns:
            None
        """
        if message.text == '\U0001F198 Ayuda' :
            cicica_bot.send_message(message.chat.id, '*Menu de comandos*\n\n' 
                                    '*Idioma* \n'
                                    'Español - Selecciona idioma Español \n'
                                    'English - Selecciona idioma Ingles \n\n'
                                    '*Menu principal* \n'
                                    '\U0001F4CD Ubicación - Ubicacion del edificio CICICA \n'
                                    '\U0001F554 Horario - Horario del edificio \n'
                                    '\U0001F52C Pruebas - Pruebas disponibles y su informacion \n'
                                    '\U0001F4DE Contacto - Numero del edificio \n'
                                    'Otras opciones - Entrada de vehiculos particulares, redes sociales y videos informativos \n\n', parse_mode='Markdown')
            
        if message.text == '\U0001F4CD Ubicación':
            markup = types.InlineKeyboardMarkup()
            waze = types.InlineKeyboardButton(text='Waze Link', callback_data='waze')
            map = types.InlineKeyboardButton(text='Google Maps link', callback_data='maps')
            markup.row(waze)
            markup.row(map)

            # Sending de location
            direccion = (
                ' \U0001F4CD San Jose (CR), Montes de Oca, San Pedro, Universidad de Costa Rica, '
                'Ciudad de la investigacion. Centro de Investigacion en Cirugia y Cancer'
            )
            photo = 'https://cicica.ucr.ac.cr/sites/default/files/styles/large/public/2023-03/301603829_509221341205881_1286055969924390298_n-3.jpg?itok=hx8Ppx6z'
            cicica_bot.send_photo(message.chat.id, photo, caption= direccion)
            # Sending the map URL
            cicica_bot.send_message(message.chat.id, 'Otras opciones', reply_markup=markup)

        # Working Hours button manager
        if message.text == '\U0001F554 Horario':
            cicica_bot.send_message(
                message.chat.id, '\U0001F554 Horario:\nLunes a Viernes 8:00 am - 5:00 pm\nSabados y Domingos CERRADO\n'
            )

        # Tests button manager
        if message.text == '\U0001F52C Pruebas':
            cicica_bot.send_message(message.chat.id, 'Recopilando información. \n Espera un momento')
            info = webparser.web_parser_es
            global info_list_es
            info_list_es = info()
            # Creating a menu with the available tests options
            markup = types.InlineKeyboardMarkup()
            secuenciacion_btn = types.InlineKeyboardButton(info_list_es[1], callback_data='psc')
            hpv_btn = types.InlineKeyboardButton(info_list_es[4], callback_data='hpv_gin')
            hpv_lab_btn = types.InlineKeyboardButton(info_list_es[7], callback_data='hpv_lab')
            c_sut_btn = types.InlineKeyboardButton(info_list_es[10], callback_data='c_sut')
            c_laparo_btn = types.InlineKeyboardButton(info_list_es[13], callback_data='c_laparo')
            tox_btn = types.InlineKeyboardButton(info_list_es[16], callback_data='tox')
            pcr_btn = types.InlineKeyboardButton(info_list_es[19], callback_data='pcr')
            bio_btn = types.InlineKeyboardButton(info_list_es[22], callback_data ='bio')
            markup.row(secuenciacion_btn)
            markup.row(hpv_btn)
            markup.row(hpv_lab_btn)
            markup.row(c_sut_btn)
            markup.row(c_laparo_btn)
            markup.row(tox_btn)
            markup.row(pcr_btn)
            markup.row(bio_btn)

            # Sending a message with the tests availables and calling the menu
            cicica_bot.reply_to(message, 'Pruebas disponibles:', reply_markup=markup)

        # Contacts button manager    
        if message.text == '\U0001F4DE Contacto':
            # chat_id = message.chat.id
            # last_int[chat_id] = datetime.now()
            cicica_bot.send_message(message.chat.id, '\U0001F4DE Contactos:\n'
                                                '2511-3322\n'
                                                'Si desea llamar, haga click sobre el numero')
            
        if message.text == 'Otras opciones':
            markup = types.InlineKeyboardMarkup()
            entrance = types.InlineKeyboardButton('Entrada de vehiculos particulares', url ='https://www.google.com/maps/place/Entrada+vehicular+principal:+Ciudad+de+la+Investigacion+(UCR)/@9.9350731,-84.0449827,18z/data=!4m6!3m5!1s0x8fa0e3891c930363:0x95f412891069878a!8m2!3d9.9347717!4d-84.0456184!16s%2Fg%2F11cmds54w9?entry=ttu')
            social = types.InlineKeyboardButton(text ='Redes sociales', callback_data ='social')
            videos = types.InlineKeyboardButton(text ='Videos informativos', callback_data ='videos_esp')
            markup.row(entrance)
            markup.row(social)
            markup.row(videos)
            cicica_bot.send_message(message.chat.id, 'Otras opciones', reply_markup = markup)

        @cicica_bot.callback_query_handler(func = lambda call_es: True)
        def callback_answers(call):
            """
            Callback function for handling user interactions.

            Args:
                call (telegram.CallbackQuery): The callback query object.

            Returns:
                None

            Raises:
                None
            """
            

            if call.data == 'psc':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                photo = 'https://media.nidux.net/pull/800/599/10564/220-product-624b6e197e8ae-b8fcf34e-cc01-4c84-92a1-66367a46f85d.jfif'
                global nombre_prueba
                nombre_prueba = 'Prueba Secuenciación Capilar'
                mensaje = ('*Prueba Secuenciación Capilar* \n Precio: %s \n  %s' % (info_list_es[2], info_list_es[3]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Comprar', url ='https://www.ucrenlinea.com/products/220/prueba-secuenciacion-capilar')
                correo_btn = types.InlineKeyboardButton('Correo para contactar', callback_data='correo_es')
                markup.row(link_btn)
                markup.row(correo_btn)
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'hpv_gin':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                photo = 'https://media.nidux.net/pull/800/599/10564/132-product-60ccc69dc1a58-ginecologos.png'
                nombre_prueba = 'Prueba HPV OncoTect para ginecólogos'
                mensaje = ('*Prueba HPV OncoTect para ginecólogos* \n Precio: %s \n  %s' % (info_list_es[5], info_list_es[6]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Comprar', url ='https://www.ucrenlinea.com/products/132/prueba-hpv-oncotect-para-ginecologos')
                correo_btn = types.InlineKeyboardButton('Correo para contactar', callback_data='correo_es')
                markup.row(link_btn)
                markup.row(correo_btn)
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)


            if call.data == 'hpv_lab':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                photo = 'https://media.nidux.net/pull/800/599/10564/131-product-60ccbf93506db-laboratorios.png'
                nombre_prueba = 'Prueba HPV OncoTect para laboratorios'
                mensaje = ('*Prueba HPV OncoTect para laboratorios* \n Precio: %s \n  %s' % (info_list_es[8], info_list_es[9]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Comprar', url ='https://www.ucrenlinea.com/products/131/prueba-hpv-oncotect-para-laboratorios')
                correo_btn = types.InlineKeyboardButton('Correo para contactar', callback_data='correo_es')
                markup.row(link_btn)
                markup.row(correo_btn)
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)
                
            if call.data == 'c_sut':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                photo = 'https://media.nidux.net/pull/800/599/10564/293-product-63447c45ca7e4-foto-1.jpeg'
                nombre_prueba = 'Curso Técnica de Suturas Quirúrgicas'
                mensaje = ('*Curso Técnica de Suturas Quirúrgicas* \n Precio: %s \n  %s' % (info_list_es[11], info_list_es[12]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Comprar', url ='https://www.ucrenlinea.com/products/293/curso-tecnica-de-suturas-quirurgicas')
                correo_btn = types.InlineKeyboardButton('Correo para contactar', callback_data='correo_es')
                markup.row(link_btn)
                markup.row(correo_btn)
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)
                
            if call.data == 'c_laparo':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                photo = 'https://media.nidux.net/pull/800/599/10564/292-product-6344785998e3e-dsc-8689.jpg'
                nombre_prueba = 'Curso Básico de Laparoscopía para Médicos Generales'
                mensaje = ('*Curso Básico de Laparoscopía para Médicos Generales* \n Precio: %s \n  %s' % (info_list_es[14], info_list_es[15]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Comprar', url ='https://www.ucrenlinea.com/products/292/curso-basico-de-laparoscopia-para-medicos-generales')
                correo_btn = types.InlineKeyboardButton('Correo para contactar', callback_data='correo_es')
                markup.row(link_btn)
                markup.row(correo_btn)
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'tox':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                photo = 'https://media.nidux.net/pull/800/599/10564/314-product-63d3ec6aea328-5-fu.png'
                nombre_prueba = 'Toxicidad en Fluoropirimidinas (5-FU)'
                mensaje = ('*Toxicidad en Fluoropirimidinas (5-FU)* \n Precio: %s \n  %s' % (info_list_es[17], info_list_es[18]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Comprar', url ='https://www.ucrenlinea.com/products/314/toxicidad-en-fluoropirimidinas-5-fu')
                correo_btn = types.InlineKeyboardButton('Correo para contactar', callback_data='correo_es')
                markup.row(link_btn)
                markup.row(correo_btn)
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'pcr':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                photo = 'https://media.nidux.net/pull/800/599/10564/325-product-643584b15dd60-dsc-6521.jpg'
                nombre_prueba = 'PCR Real para Detección de serotipos de HPV'
                mensaje = ('*PCR Real para Detección de serotipos de HPV* \n Precio: %s \n  %s' % (info_list_es[20], info_list_es[21]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Comprar', url ='https://www.ucrenlinea.com/products/325/pcr-real-para-deteccion-de-serotipos-de-hpv')
                correo_btn = types.InlineKeyboardButton('Correo para contactar', callback_data='correo_es')
                markup.row(link_btn)
                markup.row(correo_btn)
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)

            if call.data == 'bio':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                photo = 'https://media.nidux.net/pull/800/599/10564/339-product-6470d7c6d55be-imagen-taller-de-biopsia-al-vacio-1.jpg'
                nombre_prueba = 'Taller de Entrenamiento en biopsia al vacío para detección temprana de cáncer de mama'
                mensaje = ('*Taller de Entrenamiento en biopsia al vacío para detección temprana de cáncer de mama* \n Precio: %s \n  %s' % (info_list_es[23], info_list_es[24]))
                markup = types.InlineKeyboardMarkup()
                link_btn = types.InlineKeyboardButton('Comprar', url ='https://www.ucrenlinea.com/products/339/taller-de-entrenamiento-en-biopsia-al-vacio-para-deteccion-temprana-de-cancer-de-mama')
                correo_btn = types.InlineKeyboardButton('Correo para contactar', callback_data='correo_es')
                markup.row(link_btn)
                markup.row(correo_btn)
                cicica_bot.send_photo(call.message.chat.id, photo, caption= mensaje, parse_mode='Markdown', reply_markup = markup)
            if call.data =='correo_es':

                cicica_bot.send_message(call.message.chat.id, '¿Cómo te llamas?')
                cicica_bot.register_next_step_handler(message, guardar_nombre)
                
            if call.data == 'no':
                    cicica_bot.send_message(call.message.chat.id, 'Vuelve a estripar el botón de "Contactar por correo"')
            if call.data == 'si':
                cicica_bot.send_message(call.message.chat.id, 'Perfecto, muchas gracias \U0000263A')
                correo_destino = 'cicica@ucr.ac.cr'  
                mensaje = (f'Saludos,\nDe parte del CICICA_Bot, el usuario {nombre} está interesado en {nombre_prueba}\nInformación: \nNombre: {nombre}\nCédula: {cedula}\nContacto:{contacto}\n\nUn gusto servirles, CICICA_Bot')
                asunto = 'CICICA_Bot'
                sendgrid_api_key = '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'  
                url = 'https://api.sendgrid.com/v3/mail/send'
                headers = {'Authorization': f'Bearer {sendgrid_api_key}', 'Content-Type': 'application/json'}
                payload = {
                    'personalizations': [{'to': [{'email': correo_destino}]}],
                    'from': {'email': 'cicicatelegrambot@hotmail.com'},  
                    'subject': asunto,
                    'content': [{'type': 'text/plain', 'value': mensaje}]
                }
                response = requests.post(url, headers=headers, json=payload)

                if response.status_code == 202:
                    cicica_bot.send_message(call.message.chat.id, 'He enviado un correo al CICICA, sobre tu interes en la compra de ')
                else:
                    cicica_bot.send_message(call.message.chat.id, 'Error al enviar correo')    

            if call.data == 'waze':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                cicica_bot.send_message(call.message.chat.id, ' https://www.waze.com/es/live-map/directions/cr/san-jose/san-jose/centro-de-investigacion-en-cirugia-y-cancer-(cicica-or-ucr)?to=place.ChIJ04Ci2uzjoI8RwLhqJfO_sPY')

            if call.data == 'maps':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                cicica_bot.send_message(call.message.chat.id, 'https://www.google.com/maps/place/Centro+de+Investigaci%C3%B3n+en+Cirug%C3%ADa+y+C%C3%A1ncer+(CICICA+%7C+UCR)/@9.9402232,-84.0444673,15z/data=!4m6!3m5!1s0x8fa0e3ecdaa280d3:0xf6b0bff3256ab8c0!8m2!3d9.9402232!4d-84.0444673!16s%2Fg%2F11h5s46xgk ')

            if call.data == 'social':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                markup = types.InlineKeyboardMarkup()
                insta_btn = types.InlineKeyboardButton('Instagram', url ='https://www.instagram.com/cicica.ucr/')
                face_btn = types.InlineKeyboardButton('Facebook', url ='https://www.facebook.com/CicicaUCR')
                markup.row(insta_btn)
                markup.row(face_btn)
                cicica_bot.send_message(call.message.chat.id, 'Redes Sociales', reply_markup = markup)

            if call.data == 'videos_esp':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                markup = types.InlineKeyboardMarkup()
                v1_btn = types.InlineKeyboardButton('DCLAB Solucion', callback_data='v_1')
                v2_btn = types.InlineKeyboardButton('DCLab Espacio Transdisciplinar', callback_data='v_2')
                v3_btn = types.InlineKeyboardButton('DCLab Alianzas', callback_data='v_3')
                v4_btn = types.InlineKeyboardButton('Javier Mora', callback_data='v_4')
                v5_btn = types.InlineKeyboardButton('Denis Chaves', callback_data='v_5')
                v6_btn = types.InlineKeyboardButton('Ricardo Chinchilla', callback_data='v_6')
                v7_btn = types.InlineKeyboardButton('Marco Zúñiga', callback_data='v_7')
                v8_btn = types.InlineKeyboardButton('Rodrigo Mora', callback_data='v_8')
                v9_btn = types.InlineKeyboardButton('Yamileth Angulo', callback_data='v_9')
                v10_btn = types.InlineKeyboardButton('Vivian Vilchez', callback_data='v_10')
                v11_btn = types.InlineKeyboardButton('Francisco Siles', callback_data='v_11')
                v12_btn = types.InlineKeyboardButton('Cristian Marín', callback_data='v_12')
                v13_btn = types.InlineKeyboardButton('Acción en Comunidad: Laboratorio de Docencia en Cirugía y Cáncer (VAS-UCR, 2021)',callback_data='v_13')
                markup.row(v1_btn)
                markup.row(v2_btn)
                markup.row(v3_btn)
                markup.row(v4_btn)
                markup.row(v5_btn)
                markup.row(v6_btn)
                markup.row(v7_btn)
                markup.row(v8_btn)
                markup.row(v9_btn)
                markup.row(v10_btn)
                markup.row(v11_btn)
                markup.row(v12_btn)
                markup.row(v13_btn)
                cicica_bot.send_message(message.chat.id, '\U0001F3A5 Videos:', reply_markup = markup)

            if call.data == 'v_1':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_1 = 'C:/Users/Melissa/Desktop/CICICA Bot/cicica/DCLab Solución.mp4'
                video = open(video_1, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='DCLAB Solucion')
            if call.data == 'v_2':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_2 = 'cicica/DCLab Espacio Transdisciplinar.mp4'
                video = open(video_2, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption= 'DCLab Espacio Transdisciplinar')
            if call.data == 'v_3':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_3 = 'cicica/DCLab Alianzas.mp4'
                video = open(video_3, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='DCLab Alianzas')
            if call.data == 'v_4':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_4 = 'cicica/Javier Mora.mp4'
                video = open(video_4, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Javier Mora')
            if call.data == 'v_5':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_5 = 'cicica/Denis Chaves.mp4'
                video = open(video_5, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Denis Chaves')
            if call.data == 'v_6':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_6 = 'cicica/Ricardo Chinchilla.mp4'
                video = open(video_6, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Ricardo Chinchilla')
            if call.data == 'v_7':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_7 = 'cicica/Marco Zúñiga.mp4'
                video = open(video_7, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Marco Zúñiga')
            if call.data == 'v_8':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_8 = 'cicica/Rodrigo Mora.mp4'
                video = open(video_8, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Rodrigo Mora')
            if call.data == 'v_9':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_9 = 'cicica/Yamileth Angulo.mp4'
                video = open(video_9, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Yamileth Angulo')
            if call.data == 'v_10':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_10 = 'cicica/Vivian Vilchez.mp4'
                video = open(video_10, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Vivian Vilchez')
            if call.data == 'v_11':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_11 = 'cicica/Francisco Siles.mp4'
                video = open(video_11, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Francisco Siles')
            if call.data == 'v_12':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_12 = 'cicica/Cristian Marín.mp4'
                video = open(video_12, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Cristian Marín')
            if call.data == 'v_13':
                cicica_bot.answer_callback_query(callback_query_id = call.id)
                video_13 = 'cicica/Acción en Comunidad_ Laboratorio de Docencia en Cirugía y Cáncer (VAS-UCR, 2021).mp4'
                video = open(video_13, 'rb')
                cicica_bot.send_video(message.chat.id, video, caption='Acción en Comunidad: Laboratorio de Docencia en Cirugía y Cáncer (VAS-UCR, 2021)')


    def guardar_nombre(message):
        global nombre
        nombre = message.text
        cicica_bot.send_message(message.chat.id, f'¡Hola {nombre}!\n¿Cuál es tu número de cédula?')
        cicica_bot.register_next_step_handler(message, guardar_contacto, nombre)
            
    def guardar_contacto(message, nombre):
        global cedula
        cedula = message.text
        cicica_bot.send_message(message.chat.id, f'Por último, envíame tu número de contacto')
        cicica_bot.register_next_step_handler(message, guardar_cedula, nombre, cedula)

    def guardar_cedula(message, nombre, cedula):
        global contacto
        contacto = message.text
        cicica_bot.send_message(message.chat.id, f'Gracias, {nombre}\nLa información proporcionada es:\nNombre: {nombre}\nCédula: {cedula}\nContacto: {contacto}')
        markup = types.InlineKeyboardMarkup()
        Si = types.InlineKeyboardButton('Si', callback_data ='si')
        No = types.InlineKeyboardButton('No', callback_data ='no')
        markup.row(Si)
        markup.row(No)
        cicica_bot.send_message(message.chat.id, '¿Es correcta?', reply_markup = markup)
    
    def guardar_nombre_en(message):
        global nombre_en
        nombre_en = message.text
        cicica_bot.send_message(message.chat.id, f'¡Hi {nombre_en}! Now, please, send me your ID:')
        cicica_bot.register_next_step_handler(message, guardar_contacto_en, nombre_en)
            
    def guardar_contacto_en(message, nombre_en):
        global cedula_en
        cedula_en = message.text
        cicica_bot.send_message(message.chat.id, f'Thank you, {nombre_en}! At last, please provide a contact number')
        cicica_bot.register_next_step_handler(message, guardar_cedula_en, nombre_en, cedula_en)

    def guardar_cedula_en(message, nombre_en, cedula_en):
        global contacto_en
        contacto_en = message.text
        cicica_bot.send_message(message.chat.id, f'Thank you, {nombre_en}!\nYour information is: {nombre_en}\nID: {cedula_en}\nContact number: {contacto_en}')
        markup = types.InlineKeyboardMarkup()
        Yes = types.InlineKeyboardButton('Yes', callback_data ='si_en')
        No_en = types.InlineKeyboardButton('No', callback_data ='no_en')
        markup.row(Yes)
        markup.row(No_en)
        cicica_bot.send_message(message.chat.id, '¿Is it correct?', reply_markup = markup)

    
    cicica_bot.polling()

if __name__ == "__main__":
    token = '6031380198:AAES5vF4MMLoSyVNz8Nzi1Y13uRBYBkOSLM'
    main(token)

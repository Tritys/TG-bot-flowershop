from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Профиль')],
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Адрес магазина'), KeyboardButton(text='Заказать букте')],
    [KeyboardButton(text='Акции'), KeyboardButton(text='Сайт'), KeyboardButton(text='YouTube')],
    [KeyboardButton(text='Часто заказываемый букеты')],
],
                            resize_keyboard= True, 
                            input_field_placeholder='Выбирете пункт меню.')



profile = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Заказать букет'), KeyboardButton(text='Корзина')],
    [KeyboardButton(text='назад')],
],
                            resize_keyboard= True, 
                            input_field_placeholder='Выбирете пункт меню.')



shop_address = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Заказть букет')],
    [KeyboardButton(text='меню'), KeyboardButton(text='назад')],
],
                            resize_keyboard= True, 
                            input_field_placeholder='Выбирете пункт меню.')


basket = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Доставка'),  KeyboardButton(text='Заберу')],
    [KeyboardButton(text='назад'), KeyboardButton(text='меню')],
],
                            resize_keyboard= True, 
                            input_field_placeholder='Выбирете пункт меню.')


webYouTube = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com')]
   ])

website = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт', url='https://www.youtube.com')]
   ])




get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', request_contact=True)]],
                                 resize_keyboard= True)
  
#catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Футболки', callback_data='t-shirt')]])


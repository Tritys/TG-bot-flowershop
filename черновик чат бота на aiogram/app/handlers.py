from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types

import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Приветствуем тебя в нашем боте!\nЯ готов помочь тебе с выбором товаров и ответить на все твои вопросы\nПогнали делать покупки! Прежде чем начнём давай зарегистрируемся для этого введите команду /register', reply_markup=kb.main)


@router.message(F.text == 'Профиль')
async def how_are_you(message: Message):
    await message.answer('Ваш ID: {message.from_user.id} \nИмя: \nНомер телефона: {message.from_user.phone}', reply_markup=kb.profile)



@router.message(F.text == 'Адрес магазина')
async def how_are_you(message: Message):
    await message.answer('Наш магазин находится по адрессу ...\nРаботает каждый день с 9:00 до 18:00 \nНомер телефона для связи с администратором цветочного магазина 87369874326', reply_markup=kb.shop_address)

@router.message(F.text == 'Корзина')
async def how_are_you(message: Message):
    await message.answer('Ваши букеты:\n \nЦена без доставки: ', reply_markup=kb.basket)



@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.number)
    await message.answer('Введите номер телефона', reply_markup=kb.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершина.\nВаше имя: {data["name"]} \nВаш номер телефона: {data["number"]}')
    await state.clear()    


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда help')  
  
@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='', caption='')      
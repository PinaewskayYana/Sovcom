from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_autor = [
            [ types.KeyboardButton(text="Войти")],
            [ types.KeyboardButton(text="Зарегистрироваться")]
          ]

builder = ReplyKeyboardBuilder()
builder.row(
        types.KeyboardButton(text="Создать новую заявку"),
        types.KeyboardButton(text="Личный кабинет")
    )
builder.row(
        types.KeyboardButton(text="Мои заявки"),
        types.KeyboardButton(text="Тех.поддержка")
    )
phone = [
            [ types.KeyboardButton(text="Android")],
            [ types.KeyboardButton(text="iPhone")]
          ]

menu_admin = ReplyKeyboardBuilder()
menu_admin.row(
        types.KeyboardButton(text="Начать проверку заявок"),
        types.KeyboardButton(text="Заявки")
    )
'''
menu_admin.row(
        types.KeyboardButton(text="Заявки"),
        types.KeyboardButton(text="New admin")
        )
'''
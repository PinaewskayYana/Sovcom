from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_autor = [
            [ types.KeyboardButton(text="Войти")],
            [ types.KeyboardButton(text="Зарегистрироваться")]
          ]

kb_cat = [
            [ types.KeyboardButton(text="Транспортное средство")],
            [ types.KeyboardButton(text="Загородный дом")]
          ]

builder = ReplyKeyboardBuilder()
builder.row(
        types.KeyboardButton(text="Создать новую заявку"),
        types.KeyboardButton(text="Посмотреть текущие заявки")
    )
builder.row(
        types.KeyboardButton(text="История заявок"),
        types.KeyboardButton(text="Тех.поддержка")
    )
phone = [
            [ types.KeyboardButton(text="Android")],
            [ types.KeyboardButton(text="iPhone")]
          ]

menu_admin = ReplyKeyboardBuilder()
menu_admin.row(
        types.KeyboardButton(text="Заявки, ожидающие рассмотрения"),
        types.KeyboardButton(text="Заявки на корректировке"),
    )

kb_apl = [
            [ types.KeyboardButton(text="Информация о клиенте")],
            [ types.KeyboardButton(text="Просмотр заявки")]
            ]
'''
menu_admin.row(
        types.KeyboardButton(text="Заявки"),
        types.KeyboardButton(text="New admin")
        )
'''
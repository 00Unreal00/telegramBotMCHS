from aiogram.types import (InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

standard_answer_list = ['Вернутся в главное меню', "Назад"]


async def standard_answer():
    keyword = InlineKeyboardBuilder()
    for information in standard_answer_list:
        keyword.add(InlineKeyboardButton(text=information, callback_data=information))
    return keyword.adjust(2).as_markup()


async def main_page():
    start_list = ['Экстренные службы', 'Помощь на месте', 'Обучение', 'О нас']
    keyword = InlineKeyboardBuilder()
    for information in start_list:
        keyword.add(InlineKeyboardButton(text=information, callback_data=information))
    return keyword.adjust(2).as_markup()


# Экстренные службы
async def emergency():
    # emergency_list = ["Телефоны экстренных служб", "Психологическая помощь",
    #                   "Универсальный алгоритм действий"] + standard_answer_list
    emergency_list = ["Телефоны экстренных служб", "Психологическая помощь",
                      "Универсальный алгоритм действий"] + standard_answer_list
    keyword = InlineKeyboardBuilder()
    for information in emergency_list:
        keyword.add(InlineKeyboardButton(text=information, callback_data=information))
    return keyword.adjust(2).as_markup()


#Помощь на месте
async def help_on_place():
    help_on_place_list = ['Перелом', 'Отравление',
                          'Повреждение на коже', 'Потеря сознания',
                          'Обморок', 'Удушье', 'Эпилепсия', 'Инсульт',
                          'Универсальный алгоритм действий'] + standard_answer_list
    keyword = InlineKeyboardBuilder()
    for information in help_on_place_list:
        keyword.add(InlineKeyboardButton(text=information, callback_data=information))
    return keyword.adjust(3).as_markup()


#Обучение
async def studying():
    studying_list = ['Презентации', 'Видеоматериалы', 'Тесты', 'Дополнительная литература'] + standard_answer_list
    keyword = InlineKeyboardBuilder()
    for information in studying_list:
        keyword.add(InlineKeyboardButton(text=information, callback_data=information))
    return keyword.adjust(3).as_markup()


##
async def present():
    presentations_list = ['Организация первой помощи в России', "Психологическая поддержка",
                          "Наружные кровотечения и травмы",
                          "Алгоритм оказания первой помощи",
                          "Методический материал"]
    keyword = InlineKeyboardBuilder()
    for information in presentations_list:
        keyword.add(InlineKeyboardButton(text=information, callback_data=information))
    return keyword.adjust(1).as_markup()


#О нас
async def contact():
    contact_details = ['О проекте', 'обратная связь'] + standard_answer_list
    keyword = InlineKeyboardBuilder()
    for information in contact_details:
        keyword.add(InlineKeyboardButton(text=information, callback_data=information))
    return keyword.adjust(2).as_markup()

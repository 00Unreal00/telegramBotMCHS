import time

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
import app.k2 as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from asyncio import sleep

route = Router()


class Status(StatesGroup):
    main = State()
    esha0 = State()
    e1e3 = State()
    h1h8 = State()
    s1s4 = State()
    s11_s15 = State()


# старт
@route.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Status.main)
    await message.answer("Выберите интересующий вас раздел:", reply_markup=await kb.main_page())


@route.callback_query(F.data == 'Вернутся в главное меню')
async def main_menu(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.main)
    await callback.answer('')
    await callback.message.edit_text("Выберите интересующий вас раздел:", reply_markup=await kb.main_page())


#Назад
@route.callback_query(F.data == 'Назад')
async def go_back(callback: CallbackQuery, state: FSMContext):
    n_state = await state.get_state()
    print(n_state)
    match n_state:
        case Status.main.state:
            pass
        case Status.esha0.state:
            await main_menu(callback, state)
        case Status.e1e3.state:
            await emergency_0(callback, state)
        case Status.h1h8.state:
            await help_on_place_0(callback, state)
        case Status.s1s4.state:
            await study_0(callback, state)
        case Status.s11_s15.state:
            await study_1(callback, state)


# Экстренные службы
@route.callback_query(F.data == 'Экстренные службы')
async def emergency_0(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.esha0)
    await callback.answer('')
    await callback.message.edit_text("📞 112 – Единый номер службы спасения\n"
                                     "📞 101 – Телефон пожарной службы\n"
                                     " 📞 102 – Телефон полицейской службы\n"
                                     "📞 103 – Телефон скорой помощи\n"
                                     "📞 104 – Газовая служба\n"
                                     "📞 +7-495-224-22-22 или 8-800-224-22-22  ФСБ\n"
                                     "📞8-800-2000-122 Единый телефон доверия", reply_markup=await kb.emergency())


# @route.callback_query(F.data == 'Телефоны экстренных служб')
# async def emergency_1(callback: CallbackQuery, state: FSMContext):
#     await state.set_state(Status.e1e3)
#     await callback.answer('')
#     await callback.message.edit_text("112 – Единый номер службы спасения\n"
#                                      "101 – Телефон пожарной службы\n"
#                                      "102 – Телефон полицейской службы\n"
#                                      "103 – Телефон скорой помощи\n"
#                                      "104 – Газовая служба\n"
#                                      "ФСБ +7-495-224-22-22 или 8-800-224-22-22 "
#                                      "Единый телефон доверия 8-800-2000-122", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Психологическая помощь')
async def emergency_2(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.e1e3)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Универсальный алгоритм действий')
async def emergency_3(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.e1e3)
    await callback.answer('')
    photo = FSInputFile('photos/photo_2024-11-25_17.05.57.jpeg')
    await callback.message.answer_photo(photo=photo, caption="Универсальный алгоритм")
    await callback.message.delete()
    await callback.message.answer("Меню", reply_markup=await kb.standard_answer())


# помощь на месте
@route.callback_query(F.data == 'Помощь на месте')
async def help_on_place_0(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.esha0)
    await callback.answer('')
    await callback.message.edit_text("Визуально осмотрите человека и выберите соответствующую кнопку",
                                     reply_markup=await kb.help_on_place())


@route.callback_query(F.data == 'Перелом')
async def help_on_place_1(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.h1h8)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Отравление')
async def help_on_place_2(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.h1h8)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Повреждение на коже')
async def help_on_place_3(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.h1h8)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Потеря сознания')
async def help_on_place_4(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.h1h8)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Обморок')
async def help_on_place_5(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.h1h8)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Удушье')
async def help_on_place_6(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.h1h8)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Эпилепсия')
async def help_on_place_7(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.h1h8)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Инсульт')
async def help_on_place_8(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.h1h8)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


# Обучение
@route.callback_query(F.data == 'Обучение')
async def study_0(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.esha0)
    await callback.answer('')
    await callback.message.edit_text("Для ознакомления с методами оказания первой помощи для Вас собраны различные "
                                     "актуальные материалы и тесты для самопроверки", reply_markup=await kb.studying())


@route.callback_query(F.data == 'Презентации')
async def study_1(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s1s4)
    await callback.answer('')
    await callback.message.edit_text("Выберите нужную презентацию", reply_markup=await kb.present())


@route.callback_query(F.data == 'Организация первой помощи в России')
async def study_1_1(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s11_s15)
    await callback.answer('')
    file = FSInputFile('presentations/Prezentatsia1.pptx')
    await callback.message.answer_document(document=file, caption="Презентация")
    await callback.message.delete()
    await callback.message.answer("Меню", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Психологическая поддержка')
async def study_1_2(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s11_s15)
    await callback.answer('')
    file = FSInputFile('presentations/psikh_podderzhka-1.pptx')
    await callback.message.answer_document(document=file, caption="Презентация")
    await callback.message.delete()
    await callback.message.answer("Меню", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Наружные кровотечения и травмы')
async def study_1_3(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s11_s15)
    await callback.answer('')
    file = FSInputFile('presentations/krovotecheniakh_i_travmakh.pptx')
    await callback.message.answer_document(document=file, caption="Презентация")
    await callback.message.delete()
    await callback.message.answer("Меню", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Алгоритм оказания первой помощи')
async def study_1_4(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s11_s15)
    await callback.answer('')
    file = FSInputFile('presentations/Pervaya_pomosch.pptx')
    await callback.message.answer_document(document=file, caption="Презентация")
    await callback.message.delete()
    await callback.message.answer("Меню", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Методический материал')
async def study_1_5(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s11_s15)
    await callback.answer('')
    file = FSInputFile('presentations/Pervaya_pomosch.pptx')
    await callback.message.answer_document(document=file, caption="Презентация")
    await callback.message.delete()
    await callback.message.answer("Меню", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Видеоматериалы')
async def study_2(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s1s4)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Тесты')
async def study_3(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s1s4)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Дополнительная литература')
async def study_4(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s1s4)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())


# О нас
@route.callback_query(F.data == 'О нас')
async def about(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.esha0)
    await callback.answer('')
    await callback.message.edit_text("Что Вас интересует?", reply_markup=await kb.contact())

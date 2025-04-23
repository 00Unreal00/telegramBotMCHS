from aiogram import F, Router
from aiogram.types import CallbackQuery
import app.keyboards as kb
from aiogram.fsm.context import FSMContext
from app.states import Status


route = Router()


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
from aiogram import F, Router
from aiogram.types import CallbackQuery
import app.keyboards as kb
from aiogram.fsm.context import FSMContext
from app.states import Status


route = Router()


@route.callback_query(F.data == 'О нас')
async def about_0(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.esha0)
    await callback.answer('')
    await callback.message.edit_text("Что Вас интересует?", reply_markup=await kb.contact())


@route.callback_query(F.data == 'О проекте')
async def about_1(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.a1_a2)
    await callback.answer('')
    await callback.message.edit_text("""
О Нас
Руководитель проекта: Малышев Александр
оператор и видео-монтажёр: Криволапова Любовь
Сценарист и статист: Рогов Тимофей
Техническое обеспечение: Никита Ермаков
Теоретическая поддержка: Лашкина Полина
Теоретическая поддержка психологического корпуса: Якимчук Александра
Практические задания: Гостев Константин


    """, reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'обратная связь')
async def about_2(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.a1_a2)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())
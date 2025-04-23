from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
from aiogram.fsm.context import FSMContext

from app.states import Status





route = Router()


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




from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from app.state_router import state_handlers

route = Router()


@route.callback_query(F.data == 'Назад')
async def go_back(callback: CallbackQuery, state: FSMContext):
    n_state = await state.get_state()
    handler = state_handlers.get(n_state)
    if handler:
        await handler(callback, state)
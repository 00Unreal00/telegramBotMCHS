from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
import app.keyboards as kb
from aiogram.fsm.context import FSMContext
from app.states import Status

route = Router()


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


@route.callback_query(F.data == 'Психологическая помощь')
async def emergency_2(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.e1e3)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.psychology())


@route.callback_query(
    F.data.in_(['Агрессия', 'Истерика', 'Психомоторное возбуждение', 'Ступор', 'Паническая атака', 'Апатия', 'Страх',
                'Нервная дрожь', 'Плач']))
async def emergency_2_1(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.e11_e19)
    name = callback.data.lower()
    photos = [InputMediaPhoto(media=FSInputFile(f"photos/{name}_1.jpg"), caption=name),
              InputMediaPhoto(media=FSInputFile(f"photos/{name}_2.jpg"))]
    await callback.message.answer_media_group(photos)
    await callback.message.delete()
    await callback.message.answer(callback.data, reply_markup=await kb.standard_answer())


@route.callback_query(F.data == 'Универсальный алгоритм действий')
async def emergency_3(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.e1e3)
    await callback.answer('')
    photo = FSInputFile('photos/photo_2024-11-25_17.05.57.jpeg')
    await callback.message.answer_photo(photo=photo, caption="Универсальный алгоритм")
    await callback.message.delete()
    await callback.message.answer("Меню", reply_markup=await kb.standard_answer())

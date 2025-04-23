
from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile
import app.keyboards as kb
from aiogram.fsm.context import FSMContext
from app.states import Status

route = Router()


@route.callback_query(F.data.in_(['Обучение', "НазадИЗтеста"]))
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


@route.callback_query(F.data == 'Дополнительная литература')
async def study_4(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Status.s1s4)
    await callback.answer('')
    await callback.message.edit_text("Раздел в разработке", reply_markup=await kb.standard_answer())
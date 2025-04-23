import json
import time
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from asyncio import sleep
from app.states import Quiz

route2 = Router()


with open("questions/questions.json", "r", encoding="utf-8") as f:
    all_questions = json.load(f)
    states = list(Quiz.__states__)

@route2.callback_query(F.data == 'Тест')
async def study_3(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Quiz.Q1)
    await state.update_data(score=0)
    question = all_questions[states.index(await state.get_state())]
    await callback.message.edit_text(
        question["question"],
        reply_markup=await kb.send_question(question))


@route2.callback_query(F.data.in_(["а", "б", "в", "г", "д", "е", "ж"]))
async def study_3_1(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    index = states.index(await state.get_state())
    answer = callback.data
    question = all_questions[index]
    ee = " ".join(question["correct"])
    await callback.answer(f"Ответ на вопрос {ee}")
    await callback.message.edit_text(question["question"],
                                     reply_markup=await kb.send_question_true_answer(
                                         answer, question))
    if answer in question["correct"]:
        await state.update_data(score=user_data["score"] + 1)
    await sleep(8)
    if index + 1 < len(all_questions):
        await state.set_state(states[index + 1])
        question = all_questions[index + 1]
        await callback.message.edit_text(question["question"],
                                         reply_markup=await kb.send_question(
                                             question))
    else:
        user_data = await state.get_data()
        if len(all_questions)*0.7 <= user_data['score'] <= len(all_questions):
            await callback.message.edit_text(f"{user_data['score']} из {len(all_questions)} решено верно. Отлично!!",
                                             reply_markup=await kb.to_hand())
        elif len(all_questions)*0.4 <= user_data['score'] <= len(all_questions)*0.7:
            await callback.message.edit_text(f"{user_data['score']} из {len(all_questions)} решено верно.Хорошо, но "
                                             f"нужно повторить материал!", reply_markup=await kb.to_hand())
        else:
            await callback.message.edit_text(f"{user_data['score']} из {len(all_questions)} решено верно. Плохо, "
                                             f"нужно срочно учить материал!!", reply_markup=await kb.to_hand())

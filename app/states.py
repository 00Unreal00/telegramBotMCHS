from aiogram.fsm.state import StatesGroup, State


class Quiz(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
    Q8 = State()
    Q9 = State()
    Q10 = State()


class Status(StatesGroup):
    main = State()
    esha0 = State()
    e1e3 = State()
    h1h8 = State()
    s1s4 = State()
    s11_s15 = State()
    a1_a2 = State()
    e11_e19 = State()



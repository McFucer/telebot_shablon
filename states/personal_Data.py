from aiogram.dispatcher.filters.state import StatesGroup, State

class Personal(StatesGroup):
    first_name = State()
    phone_n = State()

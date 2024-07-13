from aiogram import Router
from src.filters.chat import UserFilter
from src.handlers.private.user import start, user_test
from src.middlewares import UserMiddleware, ThrottlingMiddleware

router = Router()
router.message.middleware(ThrottlingMiddleware())
router.message.filter(UserFilter())
router.include_router(start.router)
router.include_router(user_test.router)

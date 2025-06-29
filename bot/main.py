import sys
import asyncio
import logging
from .loader import bot, dp
from . import handlers, keyboards


async def main() -> None:
    
    # the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
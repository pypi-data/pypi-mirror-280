import aiohttp

from src.open_irceline.api import IrcelineRioClient
from src.open_irceline.belaqi import belaqi_index_actual


async def test_run():
    return
    async with aiohttp.ClientSession() as session:
        api = IrcelineRioClient(session)
        pos = (50.4657, 4.8647)
        r = await belaqi_index_actual(api, pos)
        print(r)

        # api = IrcelineForecastClient(session)
        # r = await belaqi_index_forecast(api, pos)
        # for k, v in r.items():
        #     print(k, v)

import logging
from unittest import TestCase
from duwi_smarthome_sdk_dev.api.ws import DeviceSynchronizationWS
import asyncio

_LOGGER = logging.getLogger(__name__)


class TestDeviceSynchronizationWS(TestCase):
    def test_device_synchronization(self):
        async def run_test():
            # async def on_callback(x: str):
            #     print(f"on_callback: {x}")
            # # 测试房屋
            # ws = DeviceSynchronizationWS(
            #     on_callback=on_callback,
            #     app_key="2e479831-1fb7-751e-7017-7534f7f99fc1",
            #     app_secret="26af4883a943083a4c34083897fcea10",
            #     access_token="715d1c63-85c0-4d74-9a89-5a0aa4806f74",
            #     refresh_token="c539ec1b-99d9-44f2-8bb0-b942545c0aca",
            #     house_no="cd56eba8-d63c-4676-b09e-9bffae64076e",
            #     app_version="0.0.1",
            #     client_version="0.0.1",
            #     client_model="homeassistant",
            # )
            # print('connect ws server...')
            # _LOGGER.warning('connect ws server...')
            # await ws.reconnect()
            # await ws.listen()
            # await ws.keep_alive()
            # print('end')


        asyncio.run(run_test())

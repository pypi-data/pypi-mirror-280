import aiohttp
import uuid
import asyncio
import nest_asyncio
from IPython.display import display, Markdown

nest_asyncio.apply()


class Neuron:
    API_URL = 'https://chat.neuron.expert/api/v1/secured/getChatCompletion'

    def __init__(self, chat_id: int, api_key: str):
        self.chat_id = chat_id
        self.chat_uuid = str(uuid.uuid4())
        self.headers = {
            "X-api-key": api_key
        }

    async def _get_answer(self, message: str) -> str:
        params = {
            'personalChatId': self.chat_id,
            'clientSessionId': self.chat_uuid,
            'message': message
        }
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.API_URL, params=params, headers=self.headers) as response:
                    response.raise_for_status()
                    data = await response.json()
                    answer = data[0]['message']
                    return answer
            except aiohttp.ClientResponseError as e:
                print(f"HTTP error occurred: {e.status} - {e.message}")
            except aiohttp.ClientConnectionError as e:
                print(f"Connection error occurred: {e}")
            except aiohttp.ClientError as e:
                print(f"Client error occurred: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    async def ask_async(self, message: str) -> str:
        return await self._get_answer(message)

    def ask(self, message: str):
        loop = asyncio.get_event_loop()
        answer = loop.run_until_complete(self.ask_async(message))

        display(Markdown(answer))


if __name__ == "__main__":
    client = Neuron(chat_id=12345, api_key='your-api-key')
    answer = client.ask("Напиши базовую модель линейной регрессии")

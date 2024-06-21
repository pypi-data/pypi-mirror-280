from aiohttp import ClientSession

from .types import SpeechToTextResult
from .exceptions import ApiException

from json import dumps

import requests


class SpeechToText:
    @staticmethod
    def speechtotext(file_path: str, language: str = "en") -> "SpeechToTextResult":
        """Speech to text using google cloud.

        Args:
            file_path (str): The path to the audio file to be translated into text. This should be a valid path to an audio file 
            language (str, optional): he language code for the speech in the audio file. Defaults to "en".
        """
        files = {
        'file': open(file_path, 'rb'),
        }
        data = {
        'language': language,
        }
        response = requests.post(
            f"https://api.devrio.org/api/v1/SpeechToText/",
            files=files,
            data=data
        )
        try:
            result = response.json()
        except Exception as e:
            raise BaseException(str(e))

        if result["ok"] is False:
            raise ApiException(dumps(result["erorr"], indent=2, ensure_ascii=False))

        return SpeechToTextResult.parse(result, file_path)


class AsyncSpeechToText:
    @staticmethod
    async def speechtotext(file_path: str, language: str = "en") -> "SpeechToTextResult":
        """Speech to text using google cloud.

        Args:
            file_path (str): The path to the audio file to be translated into text. This should be a valid path to an audio file 
            language (str, optional): he language code for the speech in the audio file. Defaults to "en".
        """
        async with ClientSession() as session:
            files = {
            'file': open(file_path, 'rb'),
            }
            data = {
            'language': language,
            }
            async with session.get(
                f"https://api.devrio.org/api/v1/SpeechToText/",
                files=files,
                data=data
            ) as response:
                try:
                    result = await response.json()
                except Exception as e:
                    raise BaseException(str(e))

                if result["ok"] is False:
                    raise ApiException(
                        dumps(result["erorr"], indent=2, ensure_ascii=False)
                    )

                return SpeechToTextResult.parse(result, file_path)

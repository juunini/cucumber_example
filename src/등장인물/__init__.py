from .등장인물 import 등장인물
from .심영 import 심영
from .상하이_조 import 상하이_조


def new_등장인물(이름: str) -> 등장인물:
    if 이름 == '심영':
        return 심영(이름)

    if 이름 == '상하이 조':
        return 상하이_조(이름)

    return 등장인물(이름)

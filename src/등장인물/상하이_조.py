from .등장인물 import 등장인물
from .심영 import 심영


class 상하이_조(등장인물):
    def 들리다(self, 사람: 등장인물, 내용: str) -> None:
        if 사람.이름 == '심영' and self.위치.이름 == '중앙극장':
            self.안되겠소_쏩시다(사람)

    def 안되겠소_쏩시다(self, 대상: 심영) -> None:
        대상.성기능 = False

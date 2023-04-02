from src.장소 import 장소


class 등장인물:
    이름: str
    성기능: bool = True
    위치: 장소 | None = None

    def __init__(self, 이름: str | None) -> None:
        if 이름:
            self.이름 = 이름

    def 말하다(self, 내용: str, 사람들) -> None:
        for 사람 in 사람들:
            사람.들리다(self, 내용)

    def 들리다(self, 사람, 내용: str) -> None:
        pass

    def 들어가다(self, 위치) -> None:
        self.위치 = 위치

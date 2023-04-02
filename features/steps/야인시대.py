from functools import reduce
from behave import given, when, then, runner

from src.등장인물 import new_등장인물
from src.장소 import 장소


@given('장소: "{이름}"')
def 장소_추가(context: runner.Context, 이름: str) -> None:
    context.장소 = 장소(이름)


@given('등장인물: "{등장인물_이름}"')
def 등장인물_추가(context: runner.Context, 등장인물_이름: str) -> None:
    try:
        context.등장인물들
    except:
        context.등장인물들 = {}

    if ',' not in 등장인물_이름:
        context.등장인물들[등장인물_이름] = new_등장인물(등장인물_이름)
        context.등장인물들[등장인물_이름].들어가다(context.장소)
        return

    context.등장인물들.update(
        reduce(
            lambda 등장인물들, 이름: 등장인물들.update({이름: new_등장인물(이름)}) or 등장인물들,
            [이름.strip() for 이름 in 등장인물_이름.split(',')],
            {},
        )
    )
    for 등장인물 in context.등장인물들.values():
        등장인물.들어가다(context.장소)


@when('"심영"이 "연설"을 하면')
def 심영이_연설을_하면(context: runner.Context) -> None:
    context.등장인물들['심영'].님을_확실하게_만나고_확인하시게_될_것입니다_여러분(context.등장인물들.values())


@then('심영은 고자가 된다')
def 심영은_고자가_된다(context: runner.Context) -> None:
    assert context.등장인물들['심영'].성기능 is False


@then('심영은 고자가 되지 않는다')
def 심영은_고자가_되지_않는다(context: runner.Context) -> None:
    assert context.등장인물들['심영'].성기능 is True

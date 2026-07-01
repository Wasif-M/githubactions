from src.maths_operations import addition,subtraction

def test_addition():
    assert addition(4,7)==11
    assert addition(0,0)==0
    assert addition(-1,8)==7

def test_subtraction():
    assert subtraction(10,5)==5
    assert subtraction(0,0)==0
    assert subtraction(-1,8)==-9
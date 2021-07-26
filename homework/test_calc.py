
import pytest
import yaml
import Calculator

class TestCal:

    def setup(self):
        print("开始计算")
        self.calc = Calculator.Calculator()

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("yaml/calc_add.yaml"))["add_num"],
                             ids=yaml.safe_load(open("yaml/calc_add.yaml"))["ids"])
    def test_add(self, a, b, expect):
        assert expect == round(self.calc.add(a, b),1)

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("yaml/calc_div.yaml"))["div_num"],
                             ids=yaml.safe_load(open("yaml/calc_div.yaml"))["ids"])
    def test_div(self, a, b, expect):
        if b == 0:
            print("被除数不能为零")
        else:
            assert expect == round(self.calc.div(a, b),2)
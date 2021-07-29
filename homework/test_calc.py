import pytest


class TestCal:

    @pytest.mark.run(order=1)
    def test_add(self, initcalc_class, get_datas_calc_add):
        assert get_datas_calc_add[2] == round(initcalc_class.add(get_datas_calc_add[0], get_datas_calc_add[1]),1)

    @pytest.mark.run(order=0)
    def test_div(self, initcalc_class, get_datas_calc_div):
        if get_datas_calc_div[1] == 0:
            print("被除数不能为零")
        else:
            assert get_datas_calc_div[2] == round(initcalc_class.div(get_datas_calc_div[0], get_datas_calc_div[1]),2)
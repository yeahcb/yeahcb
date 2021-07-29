from Calculator import *
import pytest
import yaml


@pytest.fixture()
def initcalc_class():

    print("setup")
    calc = Calculator()

    yield calc

    print("teardown")


@pytest.fixture(params=yaml.safe_load(open("datas/calc_add.yaml"))["add_num"],
                ids=yaml.safe_load(open("datas/calc_add.yaml"))["ids"])
def get_datas_calc_add(request):
  return request.param


@pytest.fixture(params=yaml.safe_load(open("datas/calc_div.yaml"))["div_num"],
                ids=yaml.safe_load(open("datas/calc_div.yaml"))["ids"])
def get_datas_calc_div(request):
  return request.param


def pytest_collection_modifyitems(session, config, items):
  for item in items:
    item.name = item.name.encode('utf-8').decode('unicode-escape')
    item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
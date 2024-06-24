import json
import os
from jysnowball import cons
from jysnowball import api_ref
from jysnowball import utls


def report(symbol):
    url = api_ref.report_latest_url+symbol
    return utls.fetch(url)


def earningforecast(symbol):
    url = api_ref.report_earningforecast_url+symbol
    return utls.fetch(url)

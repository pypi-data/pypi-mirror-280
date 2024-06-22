"""
基于Python的开源财经数据接口库，实现对股票的量价数据、基本面数据和宏观数据下载的工具，满足金融数据使用者、
量化投资使用者在数据获取方面的需求。
"""

"""
版本信息
"""

__version__ = "0.1.4"
__author__ = "xiaok"

import sys
import warnings

import pandas as pd

pd_main_version = int(pd.__version__.split('.')[0])

if pd_main_version < 2:
    warnings.warn(
        "为了支持更多特性，请将 Pandas 升级到 2.2.0 及以上版本！"
    )

if sys.version_info < (3, 9):
    warnings.warn(
        "为了支持更多特性，请将 Python 升级到 3.9.0 及以上版本！"
    )

del sys




"""
股票行情
"""
from klinecenter.k_api import get_stock_kline

"""
股票指数行情
"""
from klinecenter.k_api import get_index_kline

"""
股票指数成份股
"""
from klinecenter.k_api import get_index_contains

"""
所有指数的代码与名称
"""
from klinecenter.k_api import get_all_index_name

"""
股票财务数据与财务指标
"""
from klinecenter.k_api import get_stock_finance

"""
行业指数行情
"""
from klinecenter.k_api import get_industry_kline

"""
行业成份股
"""
from klinecenter.k_api import get_industry_contains

"""
所有行业的代码与名称
"""
from klinecenter.k_api import get_all_industry_name

"""
宏观指标数据
"""
from klinecenter.k_api import get_macro_indicator

"""
常用宏观指标代码与名称
"""
from klinecenter.k_api import get_all_common_macro





"""
xiaok-api 设置
"""
# from  import set_token, get_token



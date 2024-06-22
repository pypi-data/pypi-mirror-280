'''
Author: Devin
Date: 2024-06-18 21:30:32
LastEditors: Devin
LastEditTime: 2024-06-22 12:30:48
Description: 

Copyright (c) 2024 by Devin, All Rights Reserved. 
'''
# from .date_helper import *
# from .earth_helper import *
# from .file_helper import *
# from .log_helper import *
# from .interpolation_helper import *
# from .map_helper import *
# from .netcdf_helper import *
# from .panelayout_helper import *
# from .projection_helper import *
# from .scatter_plot_helper import *
# from  .sqlite_helper import *

# import importlib
# # 通过在需要使用某个模块时再进行导入，可以显著减少初始加载时间。可以使用importlib模块来实现延迟加载。
# class LazyModule:
#     def __init__(self, module_name):
#         self.module_name = module_name
#         self._module = None

#     def __getattr__(self, item):
#         if self._module is None:
#             self._module = importlib.import_module(self.module_name)
#         return getattr(self._module, item)

# date_helper = LazyModule('.date_helper')
# earth_helper = LazyModule('.earth_helper')
# file_helper = LazyModule('.file_helper')
# log_helper = LazyModule('.log_helper')
# interpolation_helper = LazyModule('.interpolation_helper')
# map_helper = LazyModule('.map_helper')
# netcdf_helper = LazyModule('.netcdf_helper')
# panelayout_helper = LazyModule('.panelayout_helper')
# projection_helper = LazyModule('.projection_helper')
# scatter_plot_helper = LazyModule('.scatter_plot_helper')
# sqlite_helper = LazyModule('.sqlite_helper')
# # 在__init__.py文件中使用__all__来明确表示哪些模块是公共接口，这样可以更好地控制包的导出内容。
# __all__ = [
#     'date_helper',
#     'earth_helper',
#     'file_helper',
#     'log_helper',
#     'interpolation_helper',
#     'map_helper',
#     'netcdf_helper',
#     'panelayout_helper',
#     'projection_helper',
#     'scatter_plot_helper',
#     'sqlite_helper'
# ]

import importlib

def lazy_import(module_name):
    module = None
    def _import():
        nonlocal module
        if module is None:
            module = importlib.import_module(f'esil.{module_name}')
        return module
    return _import

date_helper = lazy_import('date_helper')
earth_helper = lazy_import('earth_helper')
file_helper = lazy_import('file_helper')
log_helper = lazy_import('log_helper')
interpolation_helper = lazy_import('interpolation_helper')
map_helper = lazy_import('map_helper')
netcdf_helper = lazy_import('netcdf_helper')
panelayout_helper = lazy_import('panelayout_helper')
projection_helper = lazy_import('projection_helper')
scatter_plot_helper = lazy_import('scatter_plot_helper')
sqlite_helper = lazy_import('sqlite_helper')
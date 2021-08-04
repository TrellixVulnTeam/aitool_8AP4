# -*- coding: UTF-8 -*-
# Copyright©2020 xiangyuejia@qq.com All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""

"""
from typing import Dict, Union, List, Any, NoReturn


def split_dict(data: Dict, keys: List['str']) -> (Dict, Dict):
    selected_dict = {}
    abandon_dict = {}
    for k, v in data.items():
        if k in keys:
            selected_dict[k] = v
        else:
            abandon_dict[k] = v
    return selected_dict, abandon_dict


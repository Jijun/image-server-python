#!/usr/bin/env python# -*- coding: utf-8 -*-__author__ = 'doog'import re# 英文字母re_alpha = r"^[a-zA-Z]+$"# 英文和数字re_alphanumeric = r"^[a-zA-Z0-9]+$"#re_numeric = r"^[-+]?[0-9]+$"# 整数re_int = r"^(?:[-+]?(?:0|[1-9][0-9]*))$"# 浮点数re_float = r"^(?:[-+]?(?:[0-9]+))?(?:\.[0-9]*)?(?:[eE][\+\-]?(?:[0-9]+))?$"def is_ip(str, version):#     isIP = function (str, version) {#         version = validator.toString(version);#     if (!version) {#     return validator.isIP(str, 4) || validator.isIP(str, 6);#     } else if (version === '4') {#     if (!ipv4Maybe.test(str)) {#     return false;#     }#     var parts = str.split('.').sort(function (a, b) {#     return a - b;#     });#     return parts[3] <= 255;# }# return version === '6' && ipv6.test(str);# };    passdef equals(str, comparison):    return str == comparisondef is_alpha(str):    return bool(re.match(re_alpha, str))def is_alphanumeric(str):    return bool(re.match(re_alphanumeric, str))def is_numeric(str):    return bool(re.match(re_numeric, str))def is_int(str):    return bool(re.match(re_int, str))def is_float(str):    return bool(re.match(re_float, str))
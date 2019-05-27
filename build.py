#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add({"os_build": "Windows", "arch_build": "x86_64"}, {}, {}, {})
    builder.add({"os_build": "Windows", "arch_build": "x86"}, {}, {}, {})
    builder.run()

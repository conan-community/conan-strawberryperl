from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add({"os": "Windows", "arch":"x86_64"}, {}, {}, {})
    builder.add({"os": "Windows", "arch":"x86"}, {}, {}, {})
    builder.run()

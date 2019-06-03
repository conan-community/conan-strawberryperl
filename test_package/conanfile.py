from conans.model.conan_file import ConanFile
from conans import CMake
import os

class DefaultNameConan(ConanFile):
    settings = "os", "arch"

    def test(self):
        self.run("perl --version", run_environment=True)
        self.run("perl {}".format(os.path.join(self.source_folder, "listdir.pl")), run_environment=True)

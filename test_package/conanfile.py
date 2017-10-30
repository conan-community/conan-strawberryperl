from conans.model.conan_file import ConanFile
from conans import CMake
import os

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "arch"
        
    def test(self):
        self.run("perl --version")
        assert os.path.exists(os.path.join(self.deps_cpp_info["strawberryperl"].rootpath, "License.rtf"))

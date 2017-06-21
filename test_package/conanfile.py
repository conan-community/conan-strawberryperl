from conans.model.conan_file import ConanFile
from conans import CMake
import os

############### CONFIGURE THESE VALUES ##################
default_user = "lasote"
default_channel = "testing"
#########################################################

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "arch"
    requires = "strawberryperl/5.26.0@%s/%s" % (username, channel)
        
    def test(self):
        self.run("perl --version")
        assert os.path.exists(os.path.join(self.deps_cpp_info["strawberryperl"].rootpath, "License.rtf"))

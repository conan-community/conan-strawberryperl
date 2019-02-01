from conans import ConanFile, tools
from conans import __version__ as conan_version
from conans.model.version import Version
import os


class StrawberryperlConan(ConanFile):
    name = "strawberryperl"
    version = "5.28.1.1"
    description = "Strawbery Perl for Windows. Useful as build_require"
    license = "GNU Public License or the Artistic License"
    homepage = "http://strawberryperl.com"
    url = "https://github.com/conan-community/conan-strawberryperl"
    if conan_version < Version("0.99"):
        settings = "os", "arch"
    else:
        settings = "os_build", "arch_build"
    short_paths = True

    @property
    def arch(self):
        return self.settings.get_safe("arch_build") or self.settings.get_safe("arch")

    @property
    def os(self):
        return self.settings.get_safe("os_build") or self.settings.get_safe("os")

    def configure(self):
        if self.os != "Windows":
            raise Exception("Only windows supported for strawberry perl")

    def build(self):
        installer = {"x86": "strawberry-perl-5.28.1.1-32bit-portable.zip",
                     "x86_64": "strawberry-perl-5.28.1.1-64bit-portable.zip"}[str(self.arch)]
        url = ("%s/download/5.28.1.1/%s" % (self.homepage, installer))
        tools.download(url, filename="perl.zip")
        tools.unzip("perl.zip")
        os.unlink("perl.zip")

    def package(self):
        self.copy("*", keep_path=True)
        self.copy("licenses/License.rtf*", dst=".", keep_path=False, ignore_case=True)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "perl", "bin"))
        self.env_info.PATH.append(os.path.join(self.package_folder, "c", "bin"))

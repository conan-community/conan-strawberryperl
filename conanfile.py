# -*- coding: utf-8 -*-
import os
from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class StrawberryperlConan(ConanFile):
    name = "strawberryperl"
    version = "5.30.0.1"
    description = "Strawbery Perl for Windows. Useful as build_require"
    license = "GNU Public License or the Artistic License"
    homepage = "http://strawberryperl.com"
    url = "https://github.com/conan-community/conan-strawberryperl"
    author = "Conan Community"
    topics = ("conan", "installer", "perl", "windows")
    settings = "os_build", "arch_build"
    short_paths = True

    def configure(self):
        if self.settings.os_build != "Windows":
            raise ConanInvalidConfiguration("Only windows supported for Strawberry Perl.")

    def build(self):
        arch_build = str(self.settings.arch_build)
        sha256 = {"x86": "a1d77821c77b7a3298cf3fe381e57cba43f89b9859204398f36d85f33b287837",
                  "x86_64": "9367a64ac1451b21804a224bb6235fe6848dd42f5fa1871583821ac3dfabf013"}
        installers = {"x86": "strawberry-perl-%s-32bit-portable.zip" % self.version,
                     "x86_64": "strawberry-perl-%s-64bit-portable.zip" % self.version}
        installer = installers[arch_build]
        url = ("%s/download/%s/%s" % (self.homepage, self.version, installer))
        tools.get(url, sha256=sha256[arch_build])

    def package(self):
        self.copy(pattern="*", keep_path=True)
        self.copy(pattern="License.rtf*", dst="licenses", src="licenses")
        tools.rmdir(os.path.join("c", "lib", "pkgconfig"))

    def package_info(self):
        perl_bin = os.path.join(self.package_folder, "perl", "bin")
        self.output.info('Appending PATH environment variable: %s' % perl_bin)
        self.env_info.PATH.append(perl_bin)
        c_bin = os.path.join(self.package_folder, "c", "bin")
        self.output.info('Appending PATH environment variable: %s' % c_bin)
        self.env_info.PATH.append(c_bin)

**OBSOLETE** The recipe is now in https://github.com/conan-io/conan-center-index

[![Download](https://api.bintray.com/packages/conan-community/conan/strawberryperl%3Aconan/images/download.svg) ](https://bintray.com/conan-community/conan/strawberryperl%3Aconan/_latestVersion)
[![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/github/conan-community/conan-strawberryperl?svg=true)](https://ci.appveyor.com/project/ConanCIintegration/conan-strawberryperl)

## Conan package recipe for [*strawberryperl*](http://strawberryperl.com)

Strawbery Perl for Windows. Useful as build_require

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/conan-community/conan/strawberryperl%3Aconan).


## Issues

If you wish to report an issue or make a request for a package, please do so here:

[Issues Tracker](https://github.com/conan-community/community/issues)


## For Users

### Basic setup

    $ conan install strawberryperl/5.28.1.1@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    strawberryperl/5.28.1.1@conan/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . conan/stable




## Add Remote

Conan Community has its own Bintray repository, however, we are working to distribute all package in the Conan Center:

    $ conan remote add conan-center "https://conan.bintray.com"


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package strawberryperl.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)

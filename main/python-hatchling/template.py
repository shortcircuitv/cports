pkgname = "python-hatchling"
pkgver = "1.27.0"
pkgrel = 0
build_style = "python_pep517"
_deps = [
    "python-editables",
    "python-packaging",
    "python-pathspec",
    "python-pluggy",
    "python-trove-classifiers",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    *_deps,
]
depends = [*_deps]
checkdepends = ["python-pytest", *_deps]
pkgdesc = "Python build backend used by Hatch"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://hatch.pypa.io/latest"
source = f"$(PYPI_SITE)/h/hatchling/hatchling-{pkgver}.tar.gz"
sha256 = "971c296d9819abb3811112fc52c7a9751c8d381898f36533bb16f9791e941fd6"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")

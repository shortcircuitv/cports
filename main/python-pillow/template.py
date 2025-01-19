pkgname = "python-pillow"
pkgver = "11.1.0"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "Tests"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "freetype-devel",
    "lcms2-devel",
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openjpeg-devel",
    "python-devel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python Imaging Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT-CMU"
url = "https://python-pillow.org"
source = f"$(PYPI_SITE)/p/pillow/pillow-{pkgver}.tar.gz"
sha256 = "368da70808b36d73b4b390a8ffac11069f8a5c85f29eff1f1b01bcf3ef5b2a20"


def post_install(self):
    self.install_license("LICENSE")

pkgname = "gnome-initial-setup"
pkgver = "47.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dparental_controls=disabled",
    "-Dsystemd=false",
]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gettext", "dconf"]
makedepends = [
    "accountsservice-devel",
    "fontconfig-devel",
    "gdm-devel",
    "geoclue-devel",
    "geocode-glib-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "heimdal-devel",
    "ibus-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgweather-devel",
    "libnma-devel",
    "libpwquality-devel",
    "libsecret-devel",
    "networkmanager-devel",
    "pango-devel",
    "polkit-devel",
    "webkitgtk4-devel",
]
depends = ["dconf"]
pkgdesc = "GNOME initial setup"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Design/OS/InitialSetup"
source = f"$(GNOME_SITE)/gnome-initial-setup/{pkgver[:-2]}/gnome-initial-setup-{pkgver}.tar.xz"
sha256 = "4f4d18eb56275cc56a1993a5a1f4d13d5a6426869de67096b92f2b29caf2223c"

EAPI=8

DESCRIPTION="Ebuild with unordered, conditional metadata variables"
HOMEPAGE="https://pkgcraft.pkgcraft"
LICENSE="MIT"
SLOT="0"

if [[ ${PV} == 9999 ]]; then
	PROPERTIES="live"
else
	KEYWORDS="amd64"
fi

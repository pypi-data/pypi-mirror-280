EAPI=8

DESCRIPTION="Ebuild with multiple dependencies missing a revision"
HOMEPAGE="https://pkgcraft.pkgcraft"
LICENSE="MIT"
SLOT="0"
KEYWORDS="~amd64"
IUSE="u1 u2"
DEPEND="
	u1? ( =stub/revisioned-1 )
	u2? ( =stub/revisioned-1 )
"
RDEPEND="=stub/revisioned-1"

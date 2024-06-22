EAPI=8
DESCRIPTION="ebuild with multi-line dependencies"
SLOT=0
IUSE="u"
BDEPEND="
	a/pkg
	u? (
		b/pkg
	)
"
DEPEND="
	a/pkg
	u? (
		b/pkg
	)
"
IDEPEND="
	a/pkg
	u? (
		b/pkg
	)
"
PDEPEND="
	a/pkg
	u? (
		b/pkg
	)
"
RDEPEND="
	a/pkg
	u? (
		b/pkg
	)
"

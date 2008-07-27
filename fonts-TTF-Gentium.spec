Summary:	Gentium (a typeface for the nations) - TrueType Fonts
Summary(pl.UTF-8):	Gentium (krój pisma dla wielu narodów) - fonty TrueType
Name:		fonts-TTF-Gentium
Version:	1.0.2
Release:	2
License:	SIL Open Font License
Group:		Fonts
Vendor:		SIL International
Source0:	fonts-ttf-gentium-%{version}.tar.bz2
# Source0-md5:	3782787e9ff010551066266d9defd0f2
URL:		http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=Gentium
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Gentium ("belonging to the nations" in Latin) is a Unicode typeface
family designed to enable the many diverse ethnic groups around the
world who use the Latin script to produce readable, high-quality
publications. It supports a wide range of Latin-based alphabets and
includes glyphs that correspond to all the Latin ranges of Unicode.

The design is intended to be highly readable, reasonably compact, and
visually attractive. The additional 'extended' Latin letters are
designed to naturally harmonize with the traditional 26 ones.
Diacritics are treated with careful thought and attention to their
use. Gentium also supports both ancient and modern Greek, including a
number of alternate forms.

GentiumAlt is an alternate font with flatter diacritics, specifically
designed for languages using multiple accents. A Cyrillic version is
under development and will be added in the near future. Preliminary
work has also begun on additional weights and manual hinting, and a
complementary sans-serif face is in embryonic form.

The Gentium font family has received various awards from the
publishing and typography community.

For more details visit the SIL Computing and Writing Systems website:
<http://scripts.sil.org/>.

%description -l pl.UTF-8
Gentium (po łacinie "należący do narodów") to rodzina unikodowych
krojów pisma zaprojektowana aby umożliwić tworzenie czytelnych,
wysokiej jakości publikacji wielu odmiennym grupom etnicznym z całego
świata, używającym pisma łacińskiego. Wspiera szeroki zakres alfabetów
opartych na łacińskim i zawiera glify odpowiadające wszystkim
łacińskim częściom Unikodu.

Fonty były projektowane z myślą o tym, by były dobrze czytelne, w
miarę zwarte i atrakcyjne wizualnie. Dodatkowe "rozszerzone" litery
łacińskie są zaprojektowane tak, by naturalnie harmonizowały się z
tradycyjnymi 26. Diakrytyki są traktowane z ostrożnością i uwagą na
ich użycie. Gentium wspiera także zarówno starożytną jak i współczesną
grekę, włącznie z wieloma alternatywnymi formami.

GentiumAlt to alternatywny font z bardziej płaskimi diakrytykami,
zaprojektowany szczególnie dla języków używających wielu akcentów.
Wersja w cyrylicy jest w trakcie tworzenia i zostanie dodana w
niedalekiej przyszłości. Zaczęły się początkowe prace nad dodatkowymi
grubościami i ręcznym hintingiem, a uzupełniający krój sans-serif
znajduje się w postaci embrionalnej.

Rodzona fontów Gentium otrzymała różne nagrody od społeczności
wydawców i typografów.

Więcej szczegółów można znaleźć na stronie SIL Computing and Writing
Systems: <http://scripts.sil.org/>.

%prep
%setup -q -n fonts-ttf-gentium-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc README OFL *FAQ QUOTES FONTLOG Gentium*.pdf
%{ttffontsdir}/*.ttf

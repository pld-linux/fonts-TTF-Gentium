Summary:	Gentium (a typeface for the nations) - TrueType Fonts
Summary(pl):	Gentium (krój pisma dla wielu narodów) - fonty TrueType
Name:		fonts-TTF-Gentium
Version:	1.0.2
Release:	1
License:	SIL Open Font License
Group:		Fonts
Vendor:		SIL International
Source0:	fonts-ttf-gentium-%{version}.tar.bz2
# Source0-md5:	3782787e9ff010551066266d9defd0f2
URL:		http://scripts.sil.org/gentium/
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

%description -l pl
Gentium (po ³acinie "nale¿±cy do narodów") to rodzina unikodowych
krojów pisma zaprojektowana aby umo¿liwiæ tworzenie czytelnych,
wysokiej jako¶ci publikacji wielu odmiennym grupom etnicznym z ca³ego
¶wiata, u¿ywaj±cym pisma ³aciñskiego. Wspiera szeroki zakres alfabetów
opartych na ³aciñskim i zawiera glify odpowiadaj±ce wszystkim
³aciñskim czê¶ciom Unikodu.

Fonty by³y projektowane z my¶l± o tym, by by³y dobrze czytelne, w
miarê zwarte i atrakcyjne wizualnie. Dodatkowe "rozszerzone" litery
³aciñskie s± zaprojektowane tak, by naturalnie harmonizowa³y siê z
tradycyjnymi 26. Diakrytyki s± traktowane z ostro¿no¶ci± i uwag± na
ich u¿ycie. Gentium wspiera tak¿e zarówno staro¿ytn± jak i wspó³czesn±
grekê, w³±cznie z wieloma alternatywnymi formami.

GentiumAlt to alternatywny font z bardziej p³askimi diakrytykami,
zaprojektowany szczególnie dla jêzyków u¿ywaj±cych wielu akcentów.
Wersja w cyrylicy jest w trakcie tworzenia i zostanie dodana w
niedalekiej przysz³o¶ci. Zaczê³y siê pocz±tkowe prace nad dodatkowymi
grubo¶ciami i rêcznym hintingiem, a uzupe³niaj±cy krój sans-serif
znajduje siê w postaci embrionalnej.

Rodzona fontów Gentium otrzyma³a ró¿ne nagrody od spo³eczno¶ci
wydawców i typografów.

Wiêcej szczegó³ów mo¿na znale¼æ na stronie SIL Computing and Writing
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

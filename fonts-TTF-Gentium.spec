Summary:	Gentium (a typeface for the nations) - TrueType Fonts
Name:		fonts-TTF-Gentium
Version:	1.0.1
Release:	0.9
License:	Freeware - non-commercial, see COPYING
Group:		Fonts
Vendor:		SIL International
Source0:	fonts-ttf-gentium-%{version}.tar.bz2
# Source0-md5:	eacf8964738c130fdb8874ba419a6b58
URL:		http://scripts.sil.org/
Requires:	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Gentium ("belonging to the nations" in Latin) is a Unicode typeface family
designed to enable the many diverse ethnic groups around the world who use
the Latin script to produce readable, high-quality publications. It supports
a wide range of Latin-based alphabets and includes glyphs that correspond to
all the Latin ranges of Unicode.

The design is intended to be highly readable, reasonably compact, and
visually attractive. The additional 'extended' Latin letters are designed to
naturally harmonize with the traditional 26 ones. Diacritics are treated
with careful thought and attention to their use. Gentium also supports both
ancient and modern Greek, including a number of alternate forms.

GentiumAlt is an alternate font with flatter diacritics, specifically
designed for languages using multiple accents. A Cyrillic version is
under development and will be added in the near future. Preliminary work has
also begun on additional weights and manual hinting, and a complementary
sans-serif face is in embryonic form.

The Gentium font family has received various awards from the publishing and
typography community.

For more details visit the SIL Computing and Writing Systems website:
http://scripts.sil.org/


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
%doc README COPYING INSTALL FAQ QUOTES THANKS HISTORY CHANGELOG Gentium*.pdf
%{ttffontsdir}/*.ttf

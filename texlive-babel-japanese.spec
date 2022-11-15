Name:		texlive-babel-japanese
Version:	57733
Release:	1
Summary:	Babel support for Japanese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-japanese
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-japanese.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-japanese.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-japanese.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a japanese option for the babel package.
It defines all the language definition macros in Japanese.
Currently this package works with pLaTeX, upLaTeX, XeLaTeX and
LuaLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/babel-japanese
%{_texmfdistdir}/tex/generic/babel-japanese
%doc %{_texmfdistdir}/doc/generic/babel-japanese

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

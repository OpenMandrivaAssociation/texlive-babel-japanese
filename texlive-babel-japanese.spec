%global tl_name babel-japanese
%global tl_revision 57733

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Babel support for Japanese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/japanese
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-japanese.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-japanese.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-japanese.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a japanese option for the babel package. It
defines all the language definition macros in Japanese. Currently this
package works with pLaTeX, upLaTeX, XeLaTeX and LuaLaTeX.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-japanese
%dir %{_datadir}/texmf-dist/source/generic/babel-japanese
%dir %{_datadir}/texmf-dist/tex/generic/babel-japanese
%doc %{_datadir}/texmf-dist/doc/generic/babel-japanese/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-japanese/babel-japanese-sample.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-japanese/babel-japanese-sample.tex
%doc %{_datadir}/texmf-dist/doc/generic/babel-japanese/babel-japanese.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-japanese/japanese.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-japanese/japanese.tex
%doc %{_datadir}/texmf-dist/source/generic/babel-japanese/Makefile
%doc %{_datadir}/texmf-dist/source/generic/babel-japanese/babel-japanese.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-japanese/babel-japanese.ins
%{_datadir}/texmf-dist/tex/generic/babel-japanese/japanese.ldf

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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a japanese option for the babel package. It
defines all the language definition macros in Japanese. Currently this
package works with pLaTeX, upLaTeX, XeLaTeX and LuaLaTeX.


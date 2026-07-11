%global tl_name impatient-cn
%global tl_revision 54080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2020
Release:	%{tl_revision}.1
Summary:	Free edition of the book TeX for the Impatient
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/impatient
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient-cn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient-cn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
"TeX for the Impatient" is a book (of around 350 pages) on TeX, Plain
TeX and Eplain. The book is also available in French and Chinese
translations.


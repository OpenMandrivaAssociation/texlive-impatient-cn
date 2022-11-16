Name:		texlive-impatient-cn
Version:	54080
Release:	1
Summary:	Free edition of the book "TeX for the Impatient"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/impatient-cn
License:	fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient-cn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient-cn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
"TeX for the Impatient" is a book (of around 350 pages) on TeX,
Plain TeX and Eplain. The book is also available in French and
Chinese translations.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/plain/impatient-cn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

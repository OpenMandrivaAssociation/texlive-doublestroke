Name:		texlive-doublestroke
Version:	15878
Release:	1
Summary:	Typeset mathematical double stroke symbols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/doublestroke
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doublestroke.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doublestroke.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A font based on Computer Modern Roman useful for typesetting
the mathematical symbols for the natural numbers (N), whole
numbers (Z), rational numbers (Q), real numbers (R) and complex
numbers (C); coverage includes all Roman capital letters, '1',
'h' and 'k'. The font is available both as MetaFont source and
in Adobe Type 1 format, and LaTeX macros for its use are
provided. The fonts appear in the blackboard bold sampler.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/doublestroke/dstroke.map
%{_texmfdistdir}/fonts/source/public/doublestroke/dsrom.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsrom10.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsrom12.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsrom8.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsromo.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsromu.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsss10.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsss12.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsss8.mf
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsrom10.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsrom12.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsrom8.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsss10.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsss12.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsss8.tfm
%{_texmfdistdir}/fonts/type1/public/doublestroke/dsrom10.pfb
%{_texmfdistdir}/fonts/type1/public/doublestroke/dsrom12.pfb
%{_texmfdistdir}/fonts/type1/public/doublestroke/dsrom8.pfb
%{_texmfdistdir}/fonts/type1/public/doublestroke/dsss10.pfb
%{_texmfdistdir}/fonts/type1/public/doublestroke/dsss12.pfb
%{_texmfdistdir}/fonts/type1/public/doublestroke/dsss8.pfb
%{_texmfdistdir}/tex/latex/doublestroke/Udsrom.fd
%{_texmfdistdir}/tex/latex/doublestroke/Udsss.fd
%{_texmfdistdir}/tex/latex/doublestroke/dsfont.sty
%doc %{_texmfdistdir}/doc/fonts/doublestroke/README
%doc %{_texmfdistdir}/doc/fonts/doublestroke/dsdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/doublestroke/dsdoc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

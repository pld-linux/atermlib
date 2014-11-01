Summary:	The ATerm Library
Name:		atermlib
Version:	2.5
Release:	1
License:	LGPL
Group:		Development
Source0:	http://ftp.strategoxt.org/pub/stratego/StrategoXT/strategoxt-0.17/aterm-%{version}.tar.gz
# Source0-md5:	60218283e58c56365c9117690f36c25d
Patch0:		https://svn.nixos.org/repos/nix/nixpkgs/trunk/pkgs/development/libraries/aterm/max-long.patch
# Patch0-md5:	0c7e50b3686a079959e7c978af9444db
Patch1:		strdup.patch
URL:		http://www.cwi.nl/htbin/sen1/twiki/bin/view/SEN1/ATermLibrary
# x86_64 build segfaults
ExcludeArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ATerm (short for Annotated Term) is an abstract data type designed for
the exchange of tree-like data structures between distributed
applications.

The ATerm library forms a comprehensive procedural interface which
enables creation and manipulation of ATerms in C and Java. The ATerm
implementation is based on maximal subterm sharing and automatic
garbage collection.

A binary exchange format for the concise representation of ATerms
(sharing preserved) allows the fast exchange of ATerms between
applications. In a typical application---parse trees which contain
considerable redundant information---less than 2 bytes are needed to
represent a node in memory, and less than 2 bits are needed to
represent it in binary format. The implementation of ATerms scales up
to the manipulation of ATerms in the giga-byte range.

Programming

The ATerm library provides a comprehensive interface in C and Java to
handle the annotated term data-type in an efficient manner. If the
terms you handle are limited to a specific signature, you can use
ApiGen to generate typed interfaces to the same ATerms.

%prep
%setup -q -n aterm-%{version}
%patch0 -p1
%patch1 -p1

%build
CFLAGS="%{rpmcflags} -D__NO_CTYPE"
%configure \
	--disable-static
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libATerm.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atdiff
%attr(755,root,root) %{_bindir}/atreverse
%attr(755,root,root) %{_bindir}/atrmannos
%attr(755,root,root) %{_bindir}/atsum
%attr(755,root,root) %{_bindir}/baf2taf
%attr(755,root,root) %{_bindir}/baf2trm
%attr(755,root,root) %{_bindir}/baffle
%attr(755,root,root) %{_bindir}/dicttoc
%attr(755,root,root) %{_bindir}/taf2baf
%attr(755,root,root) %{_bindir}/taf2trm
%attr(755,root,root) %{_bindir}/termsize
%attr(755,root,root) %{_bindir}/trm2baf
%attr(755,root,root) %{_bindir}/trm2taf
%attr(755,root,root) %{_bindir}/trmcat
%{_includedir}/abool.h
%{_includedir}/afun.h
%{_includedir}/aterm1.h
%{_includedir}/aterm2.h
%{_includedir}/atypes.h
%{_includedir}/deprecated.h
%{_includedir}/encoding.h
%attr(755,root,root) %{_libdir}/libATerm.so
%{_pkgconfigdir}/aterm.pc

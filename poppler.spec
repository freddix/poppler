%define		data_ver	0.4.5

Summary:	PDF rendering library
Name:		poppler
Version:	0.20.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
# Source0-md5:	28c40266f374e1960a7bcead17d39f96
Source1:	http://poppler.freedesktop.org/%{name}-data-%{data_ver}.tar.gz
# Source1-md5:	448dd7c5077570e340340706cef931aa
URL:		http://poppler.freedesktop.org/
BuildRequires:	QtGui-devel
BuildRequires:	QtTest-devel
BuildRequires:	QtXml-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	qt-build
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A common PDF rendering library for integrating PDF viewing into
desktop applications (based on the xpdf-3.0 code base).

%package devel
Summary:	Poppler header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the Poppler library.

%package apidocs
Summary:	Poppler API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Poppler API documentation.

%package gir
Summary:	GObject introspection data
Group:		Libraries
Requires:	gobject-introspection-data

%description gir
GObject introspection data for %{name}.

%package cpp
Summary:	Cpp wrapper for poppler
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cpp
Cpp wrapper for poppler.

%package cpp-devel
Summary:	Header files for cpp wrapper for poppler
Group:		Development/Libraries
Requires:	%{name}-cpp = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description cpp-devel
Header files for cpp wrapper for poppler.

%package glib
Summary:	GLib wrapper for poppler
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description glib
GLib wrapper for poppler.

%package glib-devel
Summary:	Header files for GLib wrapper for poppler
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}

%description glib-devel
Header files for GLib wrapper for poppler.

%package qt4
Summary:	Qt4 wrapper for poppler
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description qt4
Qt4 wrapper for poppler.

%package qt4-devel
Summary:	Header files for Qt4 wrapper for poppler
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt4 = %{version}-%{release}

%description qt4-devel
Header files for Qt4 wrapper for poppler.

%package progs
Summary:	Set of tools for viewing information and converting PDF files
Group:		Applications/Publishing
Provides:	pdftops
Obsoletes:	pdftohtml
Obsoletes:	pdftohtml-pdftops
Obsoletes:	xpdf-tools
Obsoletes:	poppler-utils

%description progs
Package contains utilites for PDF files. These utilities allow to
- extract information about PDF files
- extract images from PDF files
- convert PDF files to HTML, plain text and PS formats

%prep
%setup -q -a1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-xpdf-headers	\
	--enable-zlib		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C %{name}-data-%{data_ver} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdatadir=%{_datadir}/poppler

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%post	qt4 -p /sbin/ldconfig
%postun	qt4 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%attr(755,root,root) %ghost %{_libdir}/libpoppler.so.??
%attr(755,root,root) %{_libdir}/libpoppler.so.*.*.*
%{_datadir}/poppler

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler.so
%{_includedir}/poppler
%exclude %{_includedir}/poppler/glib
%exclude %{_includedir}/poppler/qt4
%{_pkgconfigdir}/poppler-cairo.pc
%{_pkgconfigdir}/poppler.pc
%{_pkgconfigdir}/poppler-splash.pc
%{_datadir}/gir-1.0/Poppler-0.*.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/poppler

%files cpp
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpoppler-cpp.so.?
%attr(755,root,root) %{_libdir}/libpoppler-cpp.so.*.*.*

%files cpp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-cpp.so
%{_includedir}/poppler/cpp
%{_pkgconfigdir}/poppler-cpp.pc

%files glib
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpoppler-glib.so.?
%attr(755,root,root) %{_libdir}/libpoppler-glib.so.*.*.*

%files glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-glib.so
%{_includedir}/poppler/glib
%{_pkgconfigdir}/poppler-glib.pc

%files qt4
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpoppler-qt4.so.?
%attr(755,root,root) %{_libdir}/libpoppler-qt4.so.*.*.*

%files qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoppler-qt4.so
%{_includedir}/poppler/qt4
%{_pkgconfigdir}/poppler-qt4.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdf*
%{_mandir}/man1/pdf*

%files gir
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib


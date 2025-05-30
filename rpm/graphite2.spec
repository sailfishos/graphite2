Name:       graphite2
Summary:    A smart font system for complex lesser-known languages of the world
Version:    1.3.14
Release:    1
License:    (LGPLv2+ or GPLv2+ or MPLv1.1) and (Netscape or GPLv2+ or LGPLv2+)
URL:        http://graphite.sil.org
Source0:    %{name}-%{version}.tar.bz2
# From https://github.com/silnrsi/graphite/pull/92
Patch1:     0001-CMake-Raised-required-version-to-3.5.patch
BuildRequires: pkgconfig(freetype2)
BuildRequires: cmake
BuildRequires: python3-base

%description
Graphite is a system that can be used to create “smart fonts” capable of
displaying writing systems with various complex behaviors. A smart font contains
not only letter shapes but also additional instructions indicating how to combine
and position the letters in complex ways.

%package devel
Summary:  Development headers for %{name}
Requires: %{name} = %{version}

%description devel
Headers and auxiliary files for developing applications with %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%cmake
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE COPYING
%{_bindir}/gr2fonttest
%{_libdir}/libgraphite2.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}

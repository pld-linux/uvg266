Summary:	Open-source VVC encoder
Summary(pl.UTF-8):	Koder VVC o otwartych źródłach
Name:		uvg266
Version:	0.8.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/ultravideo/uvg266/releases
Source0:	https://github.com/ultravideo/uvg266/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c38e50eb8fd4a91f0e53114c8da4cec1
Patch0:		%{name}-pc.patch
URL:		https://ultravideo.fi/uvg266.html
BuildRequires:	cmake >= 3.12
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uvg266 is an open-source VVC encoder, initially based on Kvazaar.

%description -l pl.UTF-8
uvg266 to mający otwarte źródła koder VVC, wywodzący się z projektu
Kvazaar.

%package devel
Summary:	Header files for UVG266 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki UVG266
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for UVG266 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki UVG266.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS LICENSE README.md
%attr(755,root,root) %{_bindir}/uvg266
%attr(755,root,root) %{_libdir}/libuvg266.so
%{_mandir}/man1/uvg266.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/uvg266.h
%{_pkgconfigdir}/uvg266.pc

%define		_beta		beta2

Summary:	Image viewer for The X Window System
Summary(pl):	Przegl�darka do plik�w graficznych
Name:		qtvu
Version:	0.3.21
%define	rel	0.1
Release:	0.%{_beta}.%{rel}
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://download.sourceforge.net/qtvu/%{name}-%{version}%{_beta}.tar.gz
Patch0:		%{name}-qt3.patch
URL:		http://qtvu.sourceforge.net/
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
QtVu, pronounced CuteView, is an image viewer for The X Window System.
QtVu is heavily inspired by ACD Systems' excellent ACDSee.

%description -l pl
QtVu jest przegl�dark� plik�w graficznych pracuj�c� w �rodowisku X
Window. Program ten wzorowany jest na ACDSee firmy ACD Systems.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%patch0 -p1

%build
#(autoheader/autoconf/automake)
#CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
#./configure \
#	--prefix=/usr
cd src
%{__make} \
	INCPATH="-I%{_includedir}/qt" \
	QTDIR="%{_prefix}" \
	CFLAGS="-Wall %{rpmcflags}" \
	CXXFLAGS="-Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog

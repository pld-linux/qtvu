Summary:	Image viewer for The X Window System
Summary(pl):	Przegl±darka do plików graficznych
Name:		qtvu
Version:	0.3.18
Release:	1d
Group:		X11/Applications/Graphics	
Group(pl):	X11/Aplikacje/Grafika
Copyright:	GPL
Source:      	ftp://ftp.troll.no/contrib/%{name}-%{version}.tar.gz
URL:		http://www.softarc.com/~msharkey/QtVu/
Requires:	qt
Requires:	XFree86-libs
BuildRoot:	/tmp/%{name}-%{version}-root

%description
QtVu, pronounced CuteView, is an image viewer for The X Window System.
QtVu is heavily inspired by ACD Systems' excellent ACDSee.

%description -l pl
QtVu jest przegl±dark± plików graficznych pracuj±c± w ¶rodowisku X Window.
Program ten wzorowany jest na ACDSee firmy ACD Systems.

%prep
%setup  -q

%build
#(autoheader/autoconf/automake)
#CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
#./configure \
#	--prefix=/usr
make \
	INCPATH="-I/usr/X11R6/include/X11/qt" \
	QTDIR="/usr/X11R6" \
	CFLAGS="-Wall $RPM_OPT_FLAGS" \
	CXXFLAGS="-Wall $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info*
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*
gzip -9nf README ChangeLog 

%pre

%preun

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

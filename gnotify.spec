Summary:	GNotify - a notification-service for Desktop-Environments
Summary(pl.UTF-8):	GNotify - usługa powiadamiania dla środowisk graficznych
Name:		gnotify
Version:	1.2
Release:	4
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/gnotify/%{name}-%{version}.tar.gz
# Source0-md5:	6e7a031a5b1e9b12ac04992ccbf71627
Source1:	%{name}.xml
Patch0:		%{name}-clean.patch
Patch1:		%{name}-optflags.patch
Patch2:		%{name}-format.patch
URL:		https://gnotify.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNotify is a little daemon written in C using GTK. It provides (like
the KDE KNotify-system) a notification-service for
GNOME/Xfce/FVWM/Fluxbox/Enlightenment and other
Desktop-Environments/WindowManagers.

%description -l pl.UTF-8
GNotify to mały demon napisany w C z użyciem GTK. Dostarcza (podobnie
jak system KDE KNotify) usługę powiadamiania dla środowisk
GNOME/Xfce/FVWM/Fluxbox/Enlightenment i innych środowisk graficznych
oraz zarządców okien.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# symlinks, to replace by automake
%{__rm} COPYING INSTALL install-sh missing mkinstalldirs

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# gnotify.h is missing externs, some of them never defined in .c - use -fcommon for now
CFLAGS="%{rpmcflags} -fcommon"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# missing from make install
gzip -dc gnotify.1.gz > $RPM_BUILD_ROOT%{_mandir}/man1/gnotify.1

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

# no API, useless
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/GNotify
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gnotify

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS PROTOCOL README TODO
%attr(755,root,root) %{_bindir}/gnotify
%{_mandir}/man1/gnotify.1*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gnotify.xml

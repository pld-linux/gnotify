Summary:	GNotify - a notification-service for Desktop-Environments
Summary(pl):	GNotify - us³uga powiadamiania dla ¶rodowisk graficznych
Name:		gnotify
Version:	1.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnotify/%{name}-%{version}.tar.gz
# Source0-md5:	8c0248e1c53a2c595821acd8590ce858
Source1:	%{name}.xml
Patch0:		%{name}-clean.patch
Patch1:		%{name}-optflags.patch
URL:		http://gnotify.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNotify is a little daemon written in C using GTK. It provides (like
the KDE KNotify-system) a notification-service for
GNOME/XFce/FVWM/Fluxbox/Enlightenment and other
Desktop-Environments/WindowManagers.

%description -l pl
GNotify to ma³y demon napisany w C z u¿yciem GTK. Dostarcza (podobnie
jak system KDE KNotify) us³ugê powiadamiania dla ¶rodowisk
GNOME/XFce/FVWM/Fluxbox/Enlightenment i innych ¶rodowisk graficznych
oraz zarz±dców okien.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
rm -f {COPYING,INSTALL,mkinstalldirs}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_sysconfdir}}

gzip -dc gnotify.1.gz > $RPM_BUILD_ROOT%{_mandir}/man1/gnotify.1
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS PROTOCOL README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gnotify.xml

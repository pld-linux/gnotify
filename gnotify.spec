Summary:	GNotify provides a notification-service for Desktop-Environments.
Name:		gnotify
Version:	1.0
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnotify/%{name}-%{version}.tar.gz
# Source0-md5:	8c0248e1c53a2c595821acd8590ce858
URL:		http://gnotify.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel  >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNotify is a little daemon written in C using GTK. It provides (like
the KDE KNotify-system) a notification-service for
Gnome/XFce/FVWM/Fluxbox/Enlightenment and other
Desktop-Environments/WindowManagers.

%prep
%setup -q -n %{name}-%{version}
rm -rf {COPYING,INSTALL,mkinstalldirs}
cp /usr/share/automake/COPYING .
cp /usr/share/automake/INSTALL .

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_mandir}/man1
install -d $RPM_BUILD_ROOT/%{_sysconfdir}
install gnotify.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1
install gnotify.xml $RPM_BUILD_ROOT/%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%doc %{_docdir}/%{name}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*

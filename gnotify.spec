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
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

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

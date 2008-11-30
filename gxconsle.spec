#
Summary:	GTK console monitor
Name:		gxconsole
Version:	0.3.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/gxconsole/%{name}-%{version}.tar.gz
# Source0-md5:	caba3c6929ff5176c37991c94900f8cf
URL:		http://gxconsole.sourceforge.net/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	gtk+2-devel
#BuildRequires:	intltool
#BuildRequires:	libtool
#Patch0: %{name}-DESTDIR.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gxconsole is 100% gtk-based reading system console messages like
xconsole. It stays on Icon Tray,and it also notifies in arrivals the
new message. Also it can pop-up the window containing whole messages
when clicking its icon.


%prep
%setup -q -n %{name}

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
# if not running libtool or automake, but config.sub is too old:
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gxconsole
%{_desktopdir}/gxconsole.desktop

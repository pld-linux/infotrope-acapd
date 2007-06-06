#
Summary:	ACAP server
Summary(pl.UTF-8):	serwery ACAP
Name:		infotrope-acapd
Version:	0.2.1
Release:	1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://dave.cridland.net/acap/%{name}-%{version}.tar.gz
# Source0-md5:	d1bd34f5834401a75584805f73a66470
URL:		http://dave.cridland.net/acap/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an essentially fully conformant ACAP server. It's capable of
handling the entire ACAP specification. It does, however, store all
the data in memory. This turns out to work surprisingly well, and
usefully fast, but it probably wouldn't scale to enterprise level.
It's had virtually no testing apart from my own (relatively heavy) use
of it, so I wouldn't recommend using it in the enterprise just yet.

%prep
%setup -q

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
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)

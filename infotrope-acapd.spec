Summary:	ACAP server
Summary(pl.UTF-8):	Serwer ACAP
Name:		infotrope-acapd
Version:	0.2.1
Release:	1
License:	GPL v2+
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

%description -l pl.UTF-8
To jest zasadniczo w pełni zgodny serwer ACAP. Obsługuje pełną
specyfikację ACAP, jednak przechowuje dane w pamięci. Działa to
zaskakująco dobrze i szybko, ale prawdopodobnie nie skaluje się do
poziomu enterprise. Prawie nie był testowany poza własnym (dość
wymagającym) zastosowaniem autora.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
TODO

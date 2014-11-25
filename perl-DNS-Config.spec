#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	DNS
%define	pnam	Config
%include	/usr/lib/rpm/macros.perl
Summary:	DNS::Config - DNS Configuration
Summary(pl.UTF-8):	DNS::Config - konfiguracja DNS
Name:		perl-DNS-Config
Version:	0.66
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71309d67930fe356c860bbb96289c0d4
URL:		http://search.cpan.org/dist/DNS-Config/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A domain name service daemon configuration knows about the zone
information actively provided to the service users as well as lots of
other configuration data.

This class allows to represent this configuration data in a more or
less generic way. Another class, the file adaptor, then knows how to
write the information to a file in a daemon specific format.

%description -l pl.UTF-8
Konfiguracja demona usługi nazw domen (DNS) zawiera informacje o
strefach aktywnie dostarczanych użytkownikom usługi, a także wiele
innych danych konfiguracyjnych.

Ta klasa umożliwia reprezentowanie danych konfiguracyjnych w bardziej
lub mniej ogólny sposób. Inna klasa - adapter plików - ma informacje
dotyczące sposobu zapisu tych informacji w plikach w sposób właściwy
dla danego demona.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"%{pdir}::%{pnam}")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* README
%{perl_vendorlib}/DNS/*.pm
%{perl_vendorlib}/DNS/Config
%{_mandir}/man3/*

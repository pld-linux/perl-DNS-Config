#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DNS
%define	pnam	Config
Summary:	DNS::Config - DNS Configuration
Summary(pl):	DNS::Config - konfiguracja DNS
Name:		perl-DNS-Config
Version:	0.66
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71309d67930fe356c860bbb96289c0d4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A domain name service daemon configuration knows about the zone
information actively provided to the service users as well as lots of
other configuration data.

This class allows to represent this configuration data in a more or less
generic way. Another class, the file adaptor, then knows how to write
the information to a file in a daemon specific format.

# %description -l pl
# TODO

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

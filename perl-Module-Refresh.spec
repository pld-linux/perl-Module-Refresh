#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Refresh
Summary:	Module::Refresh - refresh %%INC files when updated on disk
Summary(pl.UTF-8):	Module::Refresh - odświeżanie plików %%INC po uaktualnieniu na dysku
Name:		perl-Module-Refresh
Version:	0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b077d06cab125aaff940d859945727f4
URL:		http://search.cpan.org/dist/Module-Refresh/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Temp >= 0.19
BuildRequires:	perl-Path-Class
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a generalization of the functionality provided by
Apache::StatINC and Apache::Reload. It's designed to make it easy to
do simple iterative development when working in a persistent
environment.

%description -l pl.UTF-8
Ten moduł jest uogólnieniem funkcji udostępnianych przez moduły
Apache::StatINC i Apache::Reload. Ma ułatwić proste programowanie
iteracyjne przy pracy w trwałym środowisku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Module/Refresh.pm
%{_mandir}/man3/Module::Refresh.3pm*

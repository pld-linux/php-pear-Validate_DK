%define		status		alpha
%define		pearname	Validate_DK
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Validation class for Denmark
Summary(pl.UTF-8):	%{pearname} - Klasa sprawdzająca poprawność dla Danii
Name:		php-pear-%{pearname}
Version:	0.2.0
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	e5b2db99b276ebfbe7e01a892358f81c
URL:		http://pear.php.net/package/Validate_DK/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
Obsoletes:	php-pear-Validate_DK-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for Denmark such as:
- Postal Code
- Social Security Number (CPR Nummer)
- Phone number
- Car Registration number

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Danii danych takich jak:
- kod pocztowy
- numer ubezpieczenia społecznego (CPR)
- numer telefonu
- numer rejestracyjny pojazdu

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{pearname}/LICENSE
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/DK.php

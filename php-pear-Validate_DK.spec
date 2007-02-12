%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	DK
%define		_status		alpha
%define		_pearname	Validate_DK

Summary:	%{_pearname} - Validation class for Denmark
Summary(pl.UTF-8):   %{_pearname} - Klasa sprawdzająca poprawność dla Danii
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	65a9d67ee6e6505b6bd0a7ef1458a7d7
URL:		http://pear.php.net/package/Validate_DK/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for Denmark such as:
- Postal Code
- Social Security Number (CPR Nummer)
- Phone number
- Car Registration number

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Danii danych takich jak:
- kod pocztowy
- numer ubezpieczenia społecznego (CPR)
- numer telefonu
- numer rejestracyjny pojazdu

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):   Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%doc docs/%{_pearname}/LICENSE
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/DK.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_DK

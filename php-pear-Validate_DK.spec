%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Validate_DK
Summary:	%{_pearname} - Validation class for Denmark
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Danii
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8eb2d0229bb5e0c4c797779cc567b408
URL:		http://pear.php.net/package/Validate_DK/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
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

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Danii danych takich jak:
- kod pocztowy
- numer ubezpieczenia społecznego (CPR)
- numer telefonu
- numer rejestracyjny pojazdu

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/data/Validate_DK

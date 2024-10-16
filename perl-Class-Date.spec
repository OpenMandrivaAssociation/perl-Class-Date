%define upstream_name	 Class-Date
%define upstream_version 1.1.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	Class for easy date and time manipulation

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl(UNIVERSAL::exports)
BuildRequires:	perl-devel


%description
This module is intended to provide a general-purpose date and datetime
type for perl. You have a Class::Date class for absolute date and
datetime, and have a Class::Date::Rel class for relative dates.

You can use "+", "-", "<" and ">" operators as with native perl data
types.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean 

%files
%doc Changes README
%{perl_vendorarch}/Class
%{perl_vendorarch}/auto/Class
%{_mandir}/*/*




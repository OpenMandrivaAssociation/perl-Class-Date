%define upstream_name	 Class-Date
%define upstream_version 1.1.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	Class for easy date and time manipulation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(UNIVERSAL::exports)
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Class
%{perl_vendorarch}/auto/Class
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.10-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.1.10-2
+ Revision: 680817
- mass rebuild

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.10-1mdv2011.0
+ Revision: 561044
- update to 1.1.10

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.9-7mdv2011.0
+ Revision: 555227
- rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.9-6mdv2010.1
+ Revision: 505427
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.9-5mdv2010.0
+ Revision: 430324
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.1.9-4mdv2009.0
+ Revision: 255899
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 1.1.9-2mdv2008.1
+ Revision: 151856
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.9-1mdv2007.0
- New release 1.1.9

* Fri Nov 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.8-1mdk
- new version
- spec cleanup
- rpmbuilupdate support
- fix directory ownership
- better summary
- %%mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.7-1mdk
- initial Mandriva package


%define upstream_name    Catalyst-Plugin-Authentication-Store-LDAP
%define abbrev_name      Catalyst-P-A-Store-LDAP
%define upstream_version 0.0602

Name:		perl-%{abbrev_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Catalyst - Authentication from an LDAP Directory
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Model::LDAP)
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Test::More)
BuildArch:	noarch
%rename	perl-%upstream_name

%description
This plugin uses Net::LDAP to let your application authenticate against an LDAP
directory. It has a pretty high degree of flexibility, given the wide variation
of LDAP directories and schemas from one system to another.

It authenticates users in two steps:

1) A search of the directory is performed, looking for a user object that
matches the username you pass. This is done with the bind credentials supplied
in the "binddn" and "bindpw" configuration options.

2) If that object is found, we then re-bind to the directory as that object.
Assuming this is successful, the user is Authenticated.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor << EOF

EOF

%make

%check
#make test

%install
%makeinstall_std

%files
%doc TODO Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.60.200-2mdv2011.0
+ Revision: 680727
- mass rebuild

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.200-1mdv2011.0
+ Revision: 398857
- adding missing buildrequires:
- fixing name
- update to 0.0602
- using %%perl_convert_version

* Wed Oct 01 2008 Oden Eriksson <oeriksson@mandriva.com> 0.04-8mdv2009.0
+ Revision: 290360
- don't run the borked test

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Buchan Milne <bgmilne@mandriva.org>
    - Allow disabling tests (which requires ldap access to ldap.openldap.org)

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-5mdv2008.0
+ Revision: 85930
- rebuild


* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 02:17:42 (54343)
- Rebuild, spec file cleanup

* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 02:14:37 (54335)
- import perl-Catalyst-P-A-Store-LDAP-0.04-3mdk

* Wed May 17 2006 Scott Karns <scottk@mandriva.org> 0.04-3mdk
- Updated BuildRequires
- Added source URL

* Fri Apr 14 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-2mdk
- Abbreviate rpm name to fit in the 64 char limit

* Thu Mar 23 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.04-1mdk
- 0.04

* Tue Mar 07 2006 Buchan Milne <bgmilne@mandriva.com> 0.03-1mdk
- Initial MDV RPM based on perl-Catalyst-Plugin-Authentication-LDAP


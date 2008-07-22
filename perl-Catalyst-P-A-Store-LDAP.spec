%define realname Catalyst-Plugin-Authentication-Store-LDAP
%define abbrevname Catalyst-P-A-Store-LDAP
%define name perl-%abbrevname
%define	modprefix Catalyst

%define version 0.04
%define release %mkrel 7

Summary:	Catalyst - Authentication from an LDAP Directory
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Test::More)
Provides:	perl-%realname
Obsoletes:	perl-%realname
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%if %{!?_without_test:1}%{?_without_test:0}
%__make test
%endif

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc TODO Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}




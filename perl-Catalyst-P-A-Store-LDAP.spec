%define upstream_name    Catalyst-Plugin-Authentication-Store-LDAP
%define abbrev_name      Catalyst-P-A-Store-LDAP
%define upstream_version 0.0602

Name:		perl%{abbrev_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Catalyst - Authentication from an LDAP Directory
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Test::More)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
Provides:	perl-%upstream_name
Obsoletes:	perl-%upstream_name

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc TODO Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*

%clean
rm -rf %{buildroot}




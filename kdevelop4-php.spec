%define betaver beta2

Summary: PHP plugin for kdevelop
Name: kdevelop4-php
Version: 0
Release: %mkrel -c %betaver 1
Source0: http://fr2.rpmfind.net/linux/KDE/unstable/kdevelop/3.9.96/src/kdevelop-php-%{betaver}.tar.bz2
License: GPLv2+
Group: Development/Other
Url: http://www.kdevelop.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: kdevplatform4-devel
Requires: kdevelop4

%description
This plugin adds PHP language support (including classview and code-completion)
to KDevelop.

%files
%defattr(-,root,root)
%_kde_bindir/php-parser
%_kde_libdir/kde4/kdevphplanguagesupport.so
%_kde_libdir/libkdev4phpcompletion.so
%_kde_libdir/libkdev4phpduchain.so
%_kde_libdir/libkdev4phpparser.so
%_kde_appsdir/kdevappwizard/templates/simple_phpapp.tar.bz2
%_kde_appsdir/kdevphpsupport/phpfunctions.php
%_kde_services/kdevphpsupport.desktop

#--------------------------------------------------------------------

%prep
%setup -qn kdevelop-php-%{betaver}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}

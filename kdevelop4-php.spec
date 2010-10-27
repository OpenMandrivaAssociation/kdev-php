%define git 20101027
Summary: PHP plugin for kdevelop
Name: kdevelop4-php
Version: 1.1
Release: %mkrel 1.git%{git}.1
Source0: http://fr2.rpmfind.net/linux/KDE/stable/kdevelop/1.0.0/src/kdevelop-php-%{version}-git%{git}.tar.bz2
Patch001: 0001-Add-the-text-x-php-mimetype-to-the-.desktop-file.patch
License: GPLv2+
Group: Development/Other
Url: http://www.kdevelop.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: kdevplatform4-devel >= 4:1.0.0
BuildRequires: kdevelop-pg-qt-devel
Requires: kdevelop4 >= 4:4.0.0

%description
This plugin adds PHP language support (including classview and code-completion)
to KDevelop.

%files -f kdevphp.lang
%defattr(-,root,root)
%_kde_libdir/kde4/kdevphplanguagesupport.so
%_kde_libdir/libkdev4phpcompletion.so
%_kde_libdir/libkdev4phpduchain.so
%_kde_libdir/libkdev4phpparser.so
%_kde_appsdir/kdevappwizard/templates/simple_phpapp.tar.bz2
%_kde_appsdir/kdevphpsupport/phpfunctions.php
%_kde_services/kdevphpsupport.desktop

#--------------------------------------------------------------------

%prep
%setup -qn kdevelop-php
%apply_patches

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang kdevphp

%clean
rm -rf %{buildroot}

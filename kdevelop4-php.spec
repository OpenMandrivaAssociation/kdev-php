%define kdevelop_ver 4.%(echo %{version} | cut -d. -f2,3)

Summary:	PHP plugin for kdevelop
Name:		kdevelop4-php
Version:	1.4.1
Release:	3
License:	GPLv2+
Group:		Development/Other
Url:		http://www.kdevelop.org
Source0:	http://fr2.rpmfind.net/linux/KDE/unstable/kdevelop/%{kdevelop_ver}/src/kdevelop-php-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	kdevplatform4-devel >= 4:%{version}
BuildRequires:	kdevelop-pg-qt-devel >= 0.9.82
Requires:	kdevelop4 >= 4:%{kdevelop_ver}

%description
This plugin adds PHP language support (including classview and code-completion)
to KDevelop.

%files -f kdevphp.lang
%{_kde_libdir}/kde4/kdevphplanguagesupport.so
%{_kde_libdir}/libkdev4phpcompletion.so
%{_kde_libdir}/libkdev4phpduchain.so
%{_kde_libdir}/libkdev4phpparser.so
%{_kde_appsdir}/kdevappwizard/templates/simple_phpapp.tar.bz2
%{_kde_appsdir}/kdevphpsupport/phpfunctions.php
%{_kde_services}/kdevphpsupport.desktop

#--------------------------------------------------------------------

%prep
%setup -qn kdevelop-php-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang kdevphp


%define kdevelop_ver 5.%(echo %{version} | cut -d. -f2,3)

Summary:	PHP plugin for kdevelop
Name:		kdev-php
Version:	5.0.3
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.kdevelop.org
Source0:	http://download.kde.org/stable/kdevelop/%{kdevelop_ver}/src/kdev-php-%{version}.tar.xz
BuildRequires:	kdevplatform-devel >= 4:%{version}
BuildRequires:	kdevelop-pg-qt-devel >= 0.9.82
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5KCMUtils)
Requires:	kdevelop >= 4:%{kdevelop_ver}

%description
This plugin adds PHP language support (including classview and code-completion)
to KDevelop.

%files -f kdevphp.lang
%{_libdir}/libkdevphpcompletion.so
%{_libdir}/libkdevphpduchain.so
%{_libdir}/libkdevphpparser.so
%{_libdir}/qt5/plugins/kdevplatform/25/*.so
%{_libdir}/qt5/plugins/kdevplatform/25/kcm/*.so
%{_datadir}/kdevappwizard/templates/simple_phpapp.tar.bz2
%{_datadir}/kdevphpsupport/phpfunctions.php
%{_datadir}/kdevphpsupport/phpunitdeclarations.php
%{_datadir}/kservices5/*.desktop

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5 -DBSDTAR=1
%ninja

%install
%ninja_install -C build

%find_lang kdevphp

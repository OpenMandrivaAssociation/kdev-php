Summary:	PHP plugin for kdevelop
Name:		kdev-php
Version:	25.08.2
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		https://www.kdevelop.org
Source0:	http://download.kde.org/%([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un)stable/release-service/%{version}/src/kdev-php-%{version}.tar.xz
BuildRequires:	kdevplatform-devel >= %{EVRD}
BuildRequires:	kdevelop-pg-qt-devel >= 0.9.82
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6ThreadWeaver)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6KCMUtils)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DBSDTAR:BOOL=ON
BuildOption:	-DBUILD_TESTING:BOOL=OFF
Requires:	kdevelop >= %{EVRD}

%description
This plugin adds PHP language support (including classview and code-completion)
to KDevelop.

%files -f %{name}.lang
%{_libdir}/libkdevphpcompletion.so
%{_libdir}/libkdevphpduchain.so
%{_libdir}/libkdevphpparser.so
%{_qtdir}/plugins/kdevplatform/*/*.so
%{_datadir}/kdevappwizard/templates/simple_phpapp.tar.bz2
%{_datadir}/kdevphpsupport/phpfunctions.php
%{_datadir}/kdevphpsupport/phpunitdeclarations.php
%{_datadir}/metainfo/*.xml
%{_datadir}/qlogging-categories6/kdevphpsupport.categories

#------------------------------------------------
%package devel
Summary:        Development files for kdevelop-php
Group:          Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description devel
Development files for kdevelop-php.

%files devel
%{_libdir}/cmake/KDevPHP
%{_includedir}/kdev-php

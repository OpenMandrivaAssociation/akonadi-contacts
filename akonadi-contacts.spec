Name:		akonadi-contacts
Epoch:		3
Version:	17.04.0
Release:	3
Summary:	Akonadi Contacts Integration
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/KDE
URL:		https://www.kde.org/
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Grantlee5)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	boost-devel
Conflicts:	kdepimlibs-core < 3:16.04.3-2
Obsoletes:	kdepimlibs-core < 3:17.04.0
Provides:	kdepimlibs-core = 3:17.04.0
Obsoletes:	akonadi-contact-data < 3:17.04.0
Conflicts:	akonadi-contact-data < 3:17.04.0
Provides:	akonadi-contact-data = 3:17.04.0
Obsoletes:	akonadi-social-utils-data < 3:17.04.0
Conflicts:	akonadi-social-utils-data < 3:16.04.3-2
Provides:	akonadi-social-utils-data = 3:17.04.0

%description
Akonadi Contacts Integration.

%files -f %{name}.lang
%{_datadir}/akonadicontact/
%{_datadir}/kf5/akonadi/contact/
%{_datadir}/kservices5/akonadi/contact/
%{_datadir}/kservices5/akonadicontact_actions.desktop
%{_datadir}/kservicetypes5/kaddressbookimprotocol.desktop
%{_qt5_plugindir}/kcm_akonadicontact_actions.so

#--------------------------------------------------------------------

%define major 5
%define libname %mklibname KF5AkonadiContact %{major}

%package -n %{libname}
Summary:      Akonadi Contacts Integration main library
Group:        System/Libraries

%description -n %{libname}
Akonadi Contacts Integration main library.

%files -n %{libname}
%{_libdir}/libKF5AkonadiContact.so.%{major}*

#--------------------------------------------------------------------

%define develname %mklibname KF5AkonadiContact -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{name} = %{EVRD}
Requires:       %{libname} = %{EVRD}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KF5/Akonadi/Contact/
%{_includedir}/KF5/akonadi/contact/
%{_includedir}/KF5/*_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5AkonadiContact/
%{_libdir}/qt5/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang akonadicontact5
%find_lang kcm_akonadicontact_actions
cat *.lang >%{name}.lang

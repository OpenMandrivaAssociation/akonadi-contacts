Name:		akonadi-contacts
Version:	16.08.2
Release:	1
Summary:	Akonadi Contacts Integration
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/KDE
URL:		https://www.kde.org/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz

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
BuildRequires:  boost-devel
Obsoletes:	kdepimlibs-core < 3:16.08.2

%description
Akonadi Contacts Integration.

%files
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
%{_qt5_prefix}/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

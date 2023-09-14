Name:		akonadi-contacts
Epoch:		3
Version:	23.08.1
Release:	1
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
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz

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
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KPim5GrantleeTheme)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Conflicts:	kdepimlibs-core < 3:16.04.3-2
Obsoletes:	akonadi-contact-data < 3:17.04.0
Conflicts:	akonadi-contact-data < 3:17.04.0
Provides:	akonadi-contact-data = 3:17.04.0
Obsoletes:	akonadi-social-utils-data < 3:17.04.0
Conflicts:	akonadi-social-utils-data < 3:16.04.3-2
Provides:	akonadi-social-utils-data = 3:17.04.0

%description
Akonadi Contacts Integration.

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/akonadi-contacts.categories
%{_datadir}/qlogging-categories5/akonadi-contacts.renamecategories
%{_libdir}/qt5/plugins/akonadi_serializer_addressee.so
%{_libdir}/qt5/plugins/akonadi_serializer_contactgroup.so
%{_datadir}/akonadi/plugins/serializer/akonadi_serializer_addressee.desktop
%{_datadir}/akonadi/plugins/serializer/akonadi_serializer_contactgroup.desktop
%{_datadir}/kf5/akonadi/contact/

#--------------------------------------------------------------------

%define major 5
%define oldlibname %mklibname KF5AkonadiContact 5
%define libname %mklibname KPim5AkonadiContact

%package -n %{libname}
Summary:      Akonadi Contacts Integration main library
Group:        System/Libraries
%rename %{oldlibname}

%description -n %{libname}
Akonadi Contacts Integration main library.

%files -n %{libname}
%{_libdir}/libKPim5AkonadiContact.so.%{major}*

#--------------------------------------------------------------------

%define major 5
%define oldeditorlibname %mklibname KF5ContactEditor 5
%define editorlibname %mklibname KPim5ContactEditor

%package -n %{editorlibname}
Summary:      Akonadi Contacts Integration editor library
Group:        System/Libraries
%rename %{oldeditorlibname}

%description -n %{editorlibname}
Akonadi Contacts Integration editor library.

%files -n %{editorlibname}
%{_libdir}/libKPim5ContactEditor.so.%{major}*

#--------------------------------------------------------------------

%define olddevelname %mklibname KF5AkonadiContact -d
%define develname %mklibname KPim5AkonadiContact -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{name} = %{EVRD}
Requires:       %{libname} = %{EVRD}
Requires:       %{editorlibname} = %{EVRD}
%rename %{olddevelname}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KPim5/AkonadiContact
%{_includedir}/KPim5/AkonadiContactEditor
%{_libdir}/*.so
%{_libdir}/cmake/KPim5AkonadiContact/
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/cmake/KPim5ContactEditor
%{_libdir}/cmake/KF5AkonadiContactEditor/
%doc %{_docdir}/qt5/*.{qch,tags}

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang akonadicontact5
%find_lang akonadicontact5-serializer
cat *.lang >%{name}.lang

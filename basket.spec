%define major 4
%define libname %mklibname %{name} %{major}

Name:           basket
Summary:        BasKet for KDE
Version:        1.80
Release:        %mkrel 1
URL:            http://basket.kde.org/
Source0:        http://basket.kde.org/downloads/%{name}-%{version}.tar.bz2
Group:          Office
BuildRoot:      %{_tmppath}/%{name}-buildroot
License:        GPLv2+
BuildRequires:  kdepim4-devel
BuildRequires:  kdepimlibs4-devel
BuildRequires:  qimageblitz-devel
BuildRequires:  desktop-file-utils
Requires:       kdebase4-runtime

%description
This application is mainly an all-purpose notes taker.  It provides several
baskets where to drop all sorts of  items: text, rich text, links, images,
sounds, files, colors, application launchers...

Objects can be edited, copied, dragged... So, you can arrange them as you want!

This application can be used to quickly drop all sorts of objects to free your
clutered desktop. It is also useful to collect information for a report. Those
data can be shared with co-workers by exporting baskets to HTML.

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_kde_bindir}/%{name}
%{_kde_appsdir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_configdir}/magic/%{name}.magic
%{_kde_datadir}/mimelnk/application/x-%{name}-archive.desktop
%{_kde_datadir}/mimelnk/application/x-%{name}-template.desktop
%{_kde_services}/*.desktop
%{_kde_iconsdir}/hicolor/*/*/*

#--------------------------------------------------------------------

%package -n %{libname}
Summary: Library files for %{name}
Group:   Office

%description -n %{libname}
Library files for %{name}

%files -n %{libname}
%{_kde_libdir}/libbasketcommon.so.4*
%{_kde_libdir}/kde4/basketthumbcreator.so
%{_kde_libdir}/kde4/kcm_basket.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%{find_lang} %name --with-html

# XDG Menu
desktop-file-install --vendor=""\
  --add-category="Utility" \
  --dir %{buildroot}%{_kde_datadir}/applications/kde4/ %{buildroot}%{_kde_datadir}/applications/kde4/%{name}.desktop

rm -f %{buildroot}%{_kde_libdir}/*.so

%clean
rm -rf %{buildroot}

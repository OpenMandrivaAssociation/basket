%define name           basket
%define longtitle      BasKet for KDE
%define version        1.81
%define release        %mkrel 1

Name:           %name
Summary:        %longtitle
Version:        %version
Release:        %release
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

conflicts:      %{_lib}%{name}4 < 1.80-2

%description
This application is mainly an all-purpose notes taker. 
It provide several baskets where to drop every sort of 
items: text, rich text, links, images, sounds, files, 
colors, application launcher...
Objects can be edited, copied, dragged... So, you can 
arrange them as you want !
This application can be used to quickly drop web objects 
(link, text, images...) or notes, as well as to free your 
clutered desktop (if any).
It is also useful to collect informations for a report. 
Those data can be shared with co-workers by exporting 
baskets to HTML.

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_kde_bindir}/%{name}
%{_kde_appsdir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_datadir}/config/magic/%{name}.magic
%{_kde_datadir}/mimelnk/application/x-%{name}-archive.desktop
%{_kde_datadir}/mimelnk/application/x-%{name}-template.desktop
%{_kde_datadir}/kde4/services/*.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_datadir}/kde4/services/kontact/basket_plugin.desktop
%{_kde_libdir}/kde4/basketthumbcreator.so
%{_kde_libdir}/kde4/kcm_basket.so
%{_kde_libdir}/kde4/kontact_basketplugin.so
%{_kde_libdir}/kde4/libbasketpart.so

#--------------------------------------------------------------------

%define basketcommon_major 4
%define libbasketcommon %mklibname basketcommon %{basketcommon_major}

%package -n %{libbasketcommon}
Summary:    Library files for %{name}
Group:      Office
Obsoletes:  %{_lib}%{name}4 < 1.80-2
Provides:   %{_lib}%{name}4 = %version-%release

%description -n %{libbasketcommon}
Library files for %{name}

%files -n %{libbasketcommon}
%{_kde_libdir}/libbasketcommon.so.%{basketcommon_major}*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_kde4 -DBUILD_KPARTS=1
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%{find_lang} %name --with-html


# XDG Menu
desktop-file-install --vendor=""\
  --add-category="KDE" \
  --add-category="Qt" \
  --add-category="Office" \
  --add-category="Utility" \
  --dir %{buildroot}%{_kde_datadir}/applications/kde4/ %{buildroot}%{_kde_datadir}/applications/kde4/%{name}.desktop

rm -f %buildroot%_kde_libdir/*.so

%check
for f in %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop ; do
     desktop-file-validate $f
done 

%clean
rm -rf %buildroot

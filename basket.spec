%define git 20081127

%define name           basket
%define longtitle      BasKet for KDE
# (cg) Note the version is a guess for now :s
%define version        1.1
%define release        %mkrel 0.1

%define major 4
%define libname %mklibname %{name} %{major}

Name:           %name
Summary:        %longtitle
Version:        %version
Release:        %release
URL:           	http://basket.kde.org/
Source0:        basket-%{git}.tar.lzma
Patch3:		basket-1.0-fix-crash.patch
Patch4:		basket-1.0.2.kontact-plugin.patch
Group:		Office
BuildRoot:      %{_tmppath}/%{name}-buildroot
License:	GPLv2+
BuildRequires:  kdepim4-devel
BuildRequires:  desktop-file-utils
Requires:	kdebase-progs >= 3.0

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
%{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/applications/kde4/%{name}.desktop
%{_datadir}/kde4/services/*.desktop
%{_iconsdir}/*/*/*/*


%package -n %{libname}
Summary: Library files for %{name}
Group:		Office

%description -n %{libname}
Library files for %{name}

%files -n %{libname}
%{_libdir}/libbasketcommon.so*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch3 -p1 -b .fix_crash
%patch4 -p0

%build
%cmake
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
  --dir %{buildroot}%{_datadir}/applications/kde4/ %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop

%clean
rm -rf %buildroot

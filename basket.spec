%define name           basket
%define longtitle      BasKet for KDE
%define version        1.0.3.1
%define release        %mkrel 1


Name:           %name
Summary:        %longtitle
Version:        %version
Release:        %release
URL:           	http://basket.kde.org/
Source0:        http://basket.kde.org/downloads/%name-%version.tar.gz
Patch2:         basket-1.0Beta3-fix-compile.patch 
Patch3:		basket-1.0-fix-crash.patch
Patch4:		basket-1.0.2.kontact-plugin.patch
Patch5: 	basket-1.0.2.fix-automake.patch
Group:		Office
BuildRoot:      %{_tmppath}/%{name}-buildroot
License:	GPLv2+
BuildRequires:  kdepim-devel
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

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache crystalsvg
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache crystalsvg
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_kde3_bindir}/basket
%_kde3_appsdir/%name
%_kde3_datadir/services/*.desktop
%_kde3_datadir/config/magic/*.magic
%_kde3_datadir/mimelnk/application/*.desktop
%{_kde3_iconsdir}/*/*/*/*
%_kde3_datadir/applications/kde/basket.desktop
%_kde3_datadir/services/kontact/*.desktop
%_kde3_datadir/apps/kontact/ksettingsdialog/*.setdlg
%_kde3_libdir/kde3/*
%_kde3_libdir/*.la
%_kde3_libdir/*.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch2 -p0
%patch3 -p1 -b .fix_crash
%patch4 -p0
%patch5 -p0

%build
make -f Makefile.cvs
%configure_kde3 --disable-final
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %name --with-html


# XDG Menu
desktop-file-install --vendor=""\
  --add-category="KDE" \
  --add-category="Qt" \
  --add-category="Office" \
  --add-category="Utility" \
  --dir $RPM_BUILD_ROOT%{_kde3_datadir}/applications/kde/ $RPM_BUILD_ROOT%{_kde3_datadir}/applications/kde/%{name}.desktop

%clean
rm -rf %buildroot

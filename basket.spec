%define name           basket
%define longtitle      BasKet for KDE
%define version        1.0.2
%define release        %mkrel 4


Name:           %name
Summary:        %longtitle
Version:        %version
Release:        %release
URL:           	http://basket.kde.org/
Source0:        %{name}-%{version}.tar.bz2
Patch2:         basket-1.0Beta3-fix-compile.patch 
Patch3:		basket-1.0-fix-crash.patch
Patch4:		basket-1.0.2.kontact-plugin.patch
Patch5: 	basket-1.0.2.fix-automake.patch

Source1:        cr16-app-basket.png
Source2:	cr32-app-basket.png
Source3:	cr48-app-basket.png
Group:		Office
BuildRoot:      %{_tmppath}/%{name}-buildroot
License:	GPL
BuildRequires:  kdelibs-devel
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
%{_bindir}/basket

%_datadir/apps/basket/basket_part.rc
%_datadir/apps/basket/images/tag_export_help.png
%_datadir/apps/basket/images/tag_export_on_every_lines_help.png
%_datadir/apps/kontact/ksettingsdialog/kontact_basketplugin.setdlg
%_datadir/apps/basket/welcome/Welcome_en_US.baskets
%_datadir/config/magic/basket.magic
%_datadir/services/basket_config_apps.desktop
%_datadir/services/basket_config_features.desktop
%_datadir/services/basket_config_general.desktop
%_datadir/services/basket_config_notes.desktop
%_datadir/services/basket_part.desktop
%_datadir/services/kontact/basket.desktop
%_datadir/services/basket_config_baskets.desktop
%_datadir/services/basket_config_new_notes.desktop
%_datadir/services/basket_config_notes_appearance.desktop
%_datadir/services/basketthumbcreator.desktop
%_datadir/mimelnk/application/x-basket-archive.desktop
%_datadir/mimelnk/application/x-basket-template.desktop

%{_iconsdir}/%{name}.png
%{_iconsdir}/crystalsvg/*/apps/*.png
%{_iconsdir}/crystalsvg/*/actions/*.png
%{_iconsdir}/crystalsvg/scalable/apps/*.svg
%{_iconsdir}/crystalsvg/*/mimetypes/*.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

%dir %{_datadir}/apps/%{name}
%{_datadir}/applnk/Utilities/%{name}.desktop
%{_datadir}/apps/%{name}/%{name}ui.rc
%{_datadir}/apps/%{name}/backgrounds
%{_datadir}/apps/%{name}/icons/crystalsvg/16x16/actions/*
%{_datadir}/apps/%{name}/images/insertion_help.png

%doc %{_docdir}/HTML/en/basket/*

%_libdir/kde3/kcm_basket.la
%_libdir/kde3/kcm_basket.so
%_libdir/kde3/libbasketpart.la
%_libdir/kde3/libbasketpart.so
%_libdir/kde3/libkontact_basket.la
%_libdir/kde3/libkontact_basket.so
%_libdir/libbasketcommon.la
%_libdir/libbasketcommon.so
%_libdir/kde3/basketthumbcreator.la
%_libdir/kde3/basketthumbcreator.so

%_datadir/apps/basket/welcome/*.baskets
%_datadir/services/kontact/basket_v4.desktop

#--------------------------------------------------------------------

%prep
rm -rf %buildroot

%setup -q -n %{name}-%{version}
%patch2 -p0
%patch3 -p1 -b .fix_crash
%patch4 -p0
%patch5 -p0

%build
make -f Makefile.cvs
%configure --disable-rpath \
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif	

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%{find_lang} %name


# XDG Menu
desktop-file-install --vendor="" \
  --add-category="KDE" \
  --add-category="Qt" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --add-category="Office" \
  --add-category="Utility" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/%{name}.desktop

#icons
install -d %buildroot/%{_iconsdir}
install -d %buildroot/%{_liconsdir}
install -d %buildroot/%{_miconsdir}
install -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
install -m644 %{SOURCE3} $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png


%clean
rm -rf %buildroot



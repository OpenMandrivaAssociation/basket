%define name           basket
%define longtitle      BasKet for KDE
%define version        1.81
%define release        2

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


%changelog
* Wed Dec 08 2010 John Balcaen <mikala@mandriva.org> 1.81-1mdv2011.0
+ Revision: 616260
- Update to 2.0 Beta2

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.80-4mdv2011.0
+ Revision: 610060
- rebuild

* Tue Apr 20 2010 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.80-3mdv2010.1
+ Revision: 536943
- Fix provides

* Sun Apr 18 2010 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.80-2mdv2010.1
+ Revision: 536520
- Fix typo in file list
- Add kontact support ( patch from Cedric Bortolussi) BUG:53697
- Fix conflicts
- Fix lib package name
- Only add libs files in a lib package
- Add %%check section
- Use basket changes from brancaleone for changing the package layout

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - new upstream release 1.80
    - clean spec and improve description

* Fri Dec 11 2009 Colin Guthrie <cguthrie@mandriva.org> 1.1-0.20091211.1mdv2010.1
+ Revision: 476420
- Latest snapshot
- Remove old patch (upstream kontact stuff removed)

* Wed Oct 14 2009 Colin Guthrie <cguthrie@mandriva.org> 1.1-0.20091014.1mdv2010.0
+ Revision: 457282
- Update to latest git snapshot
- Drop unneeded patch

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.1-0.20090302.2mdv2010.0
+ Revision: 436804
- rebuild

* Mon Mar 02 2009 Colin Guthrie <cguthrie@mandriva.org> 1.1-0.20090302.1mdv2009.1
+ Revision: 347458
- New snapshot

* Fri Jan 02 2009 Colin Guthrie <cguthrie@mandriva.org> 1.1-0.20090102.1mdv2009.1
+ Revision: 323310
- Update to latest snapshot

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 1.1-0.2mdv2009.1
+ Revision: 308551
- don't ship devel .so files

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - Use kde4 macros
      Fix Requires to require kde4 kdebase

* Thu Nov 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.1-0.1mdv2009.1
+ Revision: 307308
- Add missing build requires
- Git snapshot of KDE4 version of basket
- Remove patches that no longer apply

* Sat Jul 26 2008 Funda Wang <fwang@mandriva.org> 1.0.3.1-1mdv2009.0
+ Revision: 250123
- New version 1.0.3.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jan 29 2008 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.0.2-2mdv2008.1
+ Revision: 160000
- Fix automake patch
- Add patch5 to fix automake check
- Remove useless  condition
- Fix loading of baket on Kontact
  Fix BuildRequires

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 25 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 18357
- New version 1.0.2


* Mon Mar 19 2007 Laurent Montel <lmontel@mandriva.com> 1.0.1-1mdv2007.1
+ Revision: 146421
- 1.0.1
- 1.0

* Fri Feb 09 2007 Laurent Montel <lmontel@mandriva.com> 1.0-0.rc3.2mdv2007.1
+ Revision: 118519
- Fix crash
- 1.0rc3

  + Nicolas LÃ©cureuil <neoclust@mandriva.org>
    - Add lib package
    - New version -1.0Beta3
    - Fix menu
    - Reorganize file list

* Wed Oct 18 2006 Laurent Montel <lmontel@mandriva.com> 0.6.0-1mdv2007.1
+ Revision: 65805
- Fix spec file
- 0.6.0
  DONT UPLOAD IT !!!!!!!!!!!

* Sat Aug 05 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.6.0-1.beta2.3mdv2007.0
+ Revision: 52779
- Add missing source
- Increase release
- sync with cvs ( fix kontact crash ( ticket #24132))

* Thu Aug 03 2006 Laurent Montel <lmontel@mandriva.com> 0.6.0-1.beta2.2mdv2007.0
+ Revision: 42951
- Use xdg menu
- beta2

  + Nicolas LÃ©cureuil <neoclust@mandriva.org>
    - import basket-0.6.0-1.alpha2.1mdk

* Wed Apr 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.0-1.alpha2.1mdk
- Alpha 2  : Thanks jq for pointing me out this release

* Thu Jan 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.0-0.alpha1.2mdk
- Fix Build for x86_64

* Wed Jan 18 2006 Nicolas Lécureuil <neoclust@mandrake.org> 0.6.0-0.alpha1.1mdk
- 0.6.0 Alpha1

* Wed Jul 13 2005 Nicolas Lécureuil <neoclust@mandrake.org> 0.5.0-3mdk
- Fix File section

* Fri May 06 2005 Nicolas Lécureuil <neoclust@mandrake.org> 0.5.0-2mdk
- Fix BuildRequires 
- Fix Build For amd64

* Wed Apr 06 2005 Nicolas Lécureuil <neoclust@mandrake.org> 0.5.0-1mdk
- First release


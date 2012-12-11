%define name	wmMoonClock
%define version	1.27
%define release %mkrel 7

Name: 	 	%{name}
Summary: 	Docklet that shows lunar ephemeris to fairly high accuracy
Version: 	%{version}
Release: 	%{release}

Source0:	%{name}-%{version}.tar.bz2
Source1:	wmmoonclock_icon.png
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
License:	GPL
Group:		Graphical desktop/WindowMaker
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libx11-devel
BuildRequires:	libxpm-devel
BuildRequires:	libxext-devel
BuildRequires:	imagemagick

%description
wmMoonClock displays the lunar ephemeris with high accuracy. You can
define your local latitude and longitude to get precise results. And
even better you get a very nice moon icon that matches the current state
of the moon.

In order to get good results, you may have to find your geographical
coordinates, eg. from this site http://www.astro.com/atlas

%prep
%setup -q

%build
%{__cp} %{SOURCE1} .
cd Src
# copy icon to build dir
%make CFLAGS="%optflags %ldflags"
										
%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%_bindir
%{__mkdir} -p $RPM_BUILD_ROOT/%_mandir/man1
%{__cp} Src/%name $RPM_BUILD_ROOT/%_bindir/
%{__cp} Src/%name.1 $RPM_BUILD_ROOT/%_mandir/man1/

#menu
%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=wmMoonClock
Comment=Lunuar Ephemeris status docklet
Categories=System;Monitor;
EOF

#icons
%{__mkdir} -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 wmmoonclock_icon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
%{__mkdir} -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 wmmoonclock_icon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
%{__mkdir} -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 wmmoonclock_icon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

# the various states of the applet
%{__mkdir} -p $RPM_BUILD_ROOT/%_iconsdir/%name
%{__cp} Src/*xpm $RPM_BUILD_ROOT/%_iconsdir/%name/

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc BUGS COPYING
%doc %{_mandir}/*/*
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/%name/



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.27-7mdv2011.0
+ Revision: 634773
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.27-6mdv2010.0
+ Revision: 434891
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.27-5mdv2009.0
+ Revision: 262059
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.27-4mdv2009.0
+ Revision: 256206
- rebuild
- fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 1.27-2mdv2008.1
+ Revision: 135560
- fix directory creation
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import wmMoonClock


* Sun Dec 11 2005 Udo Rader <udo.rader@bestsolution.at> 1.27-2mdk
- adding libxpm-devel as BuildReq

* Thu Dec 01 2005 Udo Rader <udo.rader@bestsolution.at> 1.27-1mdk
- initial release

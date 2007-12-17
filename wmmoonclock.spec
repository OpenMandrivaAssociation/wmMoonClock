%define name	wmMoonClock
%define version	1.27
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Docklet that shows lunar ephemeris to fairly high accuracy
Version: 	%{version}
Release: 	%{release}

Source0:	%{name}-%{version}.tar.bz2
Source1:	wmmoonclock_icon.png
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
License:	GPL
Group:		Graphical desktop/WindowMaker
BuildRequires:	X11-devel ImageMagick libapm-devel libxpm-devel

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
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%_bindir
%{__mkdir} -p $RPM_BUILD_ROOT/%_mandir/man1
%{__cp} Src/%name $RPM_BUILD_ROOT/%_bindir/
%{__cp} Src/%name.1 $RPM_BUILD_ROOT/%_mandir/man1/

#menu
%{__mkdir} -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="wmMoonClock" longtitle="Lunuar Ephemeris status docklet" section="System/Monitoring"
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

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc BUGS COPYING
%doc %{_mandir}/*/*
%{_bindir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/%name/


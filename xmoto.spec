%define name xmoto
%define version 0.3.0
%define release %mkrel 1

Summary: A challenging 2D motocross platform game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/xmoto/%{name}-%{version}-src.tar.bz2
Source1: %{name}.png
# (blino) allow to override localedir
Patch1: xmoto-0.2.2-locale.patch
License: GPL
Group: Games/Arcade
Url: http://xmoto.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mesaglu-devel ode-devel SDL-devel SDL_mixer-devel SDL_ttf-devel
BuildRequires: curl-devel jpeg-devel png-devel bzip2-devel ImageMagick
BuildRequires: automake lua-devel sqlite3-devel
Requires: soundwrapper

%description
X-Moto is a challenging 2D motocross platform game, where physics play
an all important role in the gameplay. You need to control your bike
to its limit, if you want to have a chance finishing the more
difficult of the challenges.
First you'll try just to complete the levels, while later you'll
compete with yourself and others, racing against the clock.

%prep
%setup -q
%patch1 -p1 -b .locale

%build
automake
%configure \
  --bindir=%{_gamesbindir} \
  --datadir=%{_gamesdatadir} \
  --with-localesdir=%{_datadir}/locale
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall bindir=$RPM_BUILD_ROOT%{_gamesbindir} datadir=$RPM_BUILD_ROOT%{_gamesdatadir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=X-Moto
Comment=Motocross platform game
Exec=soundwrapper %_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

mkdir -p $RPM_BUILD_ROOT/{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
install %SOURCE1 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -scale 32 %SOURCE1 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -scale 16 %SOURCE1 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_mandir}/mang/*



Summary:	A challenging 2D motocross platform game
Name:		xmoto
Version:		0.5.10
Release:		2
License:		GPLv2+
Group:		Games/Arcade
Url:		http://xmoto.sourceforge.net/
Source0:		http://download.tuxfamily.org/xmoto/xmoto/%{version}/%{name}-%{version}-src.tar.gz
Source1:		%{name}.png
Patch0:		xmoto-0.5.9-Environment-cstlib.patch
Patch1:		xmoto-0.5.9-Environment-string.patch
Patch2:		xmoto-0.5.9-gcc4.7.patch
Patch3:		xmoto-0.5.9-helpers-log-include.patch
Patch4:		xmoto-0.5.9-helpers-text-includes.patch
Patch5:		xmoto-0.5.9-libpng15.patch
Patch6:		xmoto-0.5.9-xmargs-include.patch

BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ode)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng15)
BuildRequires:	bzip2-devel
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	bison
BuildRequires:	pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(libxml-2.0)


%description
X-Moto is a challenging 2D motocross platform game, where physics play
an all important role in the gameplay. You need to control your bike
to its limit, if you want to have a chance finishing the more
difficult of the challenges.
First you'll try just to complete the levels, while later you'll
compete with yourself and others, racing against the clock.

%prep
%setup -q
#individual file patch for better maintenance imported from MRB
%patch0 -p0 
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
#applied upstream
#patch5 -p0
%patch6 -p0

%build
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir} \
	--with-localesdir=%{_datadir}/locale \
	--disable-rpath \
	--enable-threads=pth \
	--with-renderer-openGl=1 \
	--with-unoptimized=0

%make

%install
%makeinstall bindir=%{buildroot}%{_gamesbindir} datadir=%{buildroot}%{_gamesdatadir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=X-Moto
Comment=Motocross platform game
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%find_lang %{name}


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*


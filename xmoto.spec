Summary:	A challenging 2D motocross platform game
Name:		xmoto
Version:	0.5.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Games/Arcade
Url:		http://xmoto.sourceforge.net/
Source0:	http://download.tuxfamily.org/xmoto/xmoto/%{version}/%{name}-%{version}-src.tar.gz
Source1:	%{name}.png
BuildRequires:	mesaglu-devel
BuildRequires:	ode-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_net-devel
BuildRequires:	curl-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	bzip2-devel
BuildRequires:	imagemagick
BuildRequires:	lua-devel
BuildRequires:	sqlite3-devel
BuildRequires:	bison
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
X-Moto is a challenging 2D motocross platform game, where physics play
an all important role in the gameplay. You need to control your bike
to its limit, if you want to have a chance finishing the more
difficult of the challenges.
First you'll try just to complete the levels, while later you'll
compete with yourself and others, racing against the clock.

%prep
%setup -q

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
rm -rf %{buildroot}
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

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*

Summary:	A GTK+2 based image viewer that supports xine and mplayer
Name:		gimageview
Version:	0.2.27
Release:	%mkrel 6
License:	GPLv2+
Group:		Graphics
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		https://www.homa.ne.jp/~ashie/gimageview/
Source0:	%{name}-%{version}.tar.bz2
Suggests:	mplayer
Obsoletes:	%{mklibname gimageview 0} <= %{version}-%{release}
Obsoletes:	%{mklibname gimageview 0 -d} <= %{version}-%{release}
BuildRequires:	gtk+2-devel
BuildRequires:	librsvg-devel
BuildRequires:	libwmf-devel
BuildRequires:	libxine-devel

%description
GImageView is a GTK+2-based image viewer.
It supports tabbed browsing, thumbnail table views, directory tree views,
drag and drop, reading thumbnail cache of other famous image viewers,
and flexible user interface. Also it supports xine and mplayer, so you can
play movies/music. 

%prep
rm -rf %{buildroot}
%setup -q

%build
%configure2_5x --with-gtk2 --with-xine --enable-mplayer --disable-splash --disable-rpath
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall}
rm -rf %{buildroot}%{_datadir}/gnome

# menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=GImageView
Comment=Image viewer and browser
Exec=%{_bindir}/gimv 
Icon=graphics_section
Terminal=false
Type=Application
StartupNotify=true
MimeType=image/bmp;image/gif;image/jpeg;image/jpg;image/pjpeg;image/png;image/tiff;image/x-bmp;image/x-gray;image/x-icb;image/x-ico;image/x-png;image/x-portable-anymap;image/x-portable-bitmap;image/x-portable-graymap;image/x-portable-pixmap;image/x-psd;image/x-xbitmap;image/x-xpixmap;image/x-pcx;image/svg+xml;image/vnd.wap.wbmp;
Categories=GTK;AudioVideo;Graphics;2DGraphics;Viewer
EOF

%find_lang %{name}

%if %mdkversion < 200900
%post 
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog HACKING NEWS README TODO 
%{_bindir}/gimv
%{_datadir}/pixmaps/gimv.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/%{name}
%{_libdir}/%{name}


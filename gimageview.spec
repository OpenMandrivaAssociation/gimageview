%define name     gimageview
%define version  0.2.27
%define release  %mkrel 2

%define libname_orig %mklibname %{name}
%define libname %{libname_orig}0

Summary: A GTK+2 based image viewer that supports xine and mplayer
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Graphics
URL: http://www.homa.ne.jp/~ashie/gimageview/
Source0: %{name}-%{version}.tar.bz2
Patch1:	fix_autogen.patch.bz2
Requires: mplayer %libname
BuildRequires: gtk+2-devel librsvg-devel libwmf-devel libxine-devel 

%description
GImageView is a GTK+2 based image viewer.
It supports tabbed browsing, thumbnail table views, directory tree views,
drag and drop, reading thumbnail cache of other famous image viewers,
and flexible user interface. Also it supports xine and mplayer. So you can
play movies/music. 


%package -n %{libname}
Summary:	Gimageview library
Group:		Graphics
Provides:	%{libname_orig} = %{version}-%{release}

%description -n %{libname}
gimageview library.

%package -n %{libname}-devel
Summary:	Headers of gimageview for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}

%description -n %{libname}-devel
Headers of %{name} for development.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%patch1 -p0

%build

sh autogen.sh
%configure --with-gtk2 --with-xine --enable-mplayer --disable-splash
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{makeinstall}

# menu
mkdir -p %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}): \
 command="%{_bindir}/gimv" \
 icon="graphics_section.png" \
 title="Gimagview" \
 longtitle="A browser for graphics files" \
 needs="x11" \
 section="Multimedia/Graphics"
EOF

%find_lang %{name}

%post 
%update_menus

%postun
%clean_menus

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-, root, root)
%doc %{_docdir}/%{name}
%{_bindir}/gimv
%{_datadir}/pixmaps/gimv.png
%{_datadir}/gnome/apps/Graphics/gimageview.desktop
%{_datadir}/%{name}/gtkrc
%{_datadir}/%{name}/mplayerrc
%{_datadir}/%{name}/pixmaps/default/*.xpm
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps/
%dir %{_datadir}/%{name}/pixmaps/default/
%_menudir/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{name}/*/*.so

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{name}/*/*.la



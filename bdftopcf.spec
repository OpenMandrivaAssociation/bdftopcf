Summary:	Convert X font from Bitmap Distribution Format to Portable Compiled Format
Name:		bdftopcf
Version:	1.1
Release:	4
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org/
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(xfont)
BuildRequires:	pkgconfig(xorg-macros)

%description
Bdftopcf converts X fonts from Bitmap Distribution Format
to Portable Compiled Format.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*

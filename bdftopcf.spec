Summary:	Convert X font from Bitmap Distribution Format to Portable Compiled Format
Name:		bdftopcf
Version:	1.0.4
Release:	7
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
%setup -q

%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*


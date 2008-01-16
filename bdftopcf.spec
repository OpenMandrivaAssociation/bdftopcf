Name: bdftopcf
Version: 1.0.1
Release: %mkrel 3
Summary: Convert X font from Bitmap Distribution Format to Portable Compiled Format
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libxfont-devel	>= 1.3.1

%description
Bdftopcf converts X fonts from Bitmap Distribution Format to Portable Compiled Format.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*

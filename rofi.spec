Name:           rofi
Version:        
Release:        1
Summary:        A window switcher, run dialog and dmenu replacement
License:        MIT
Group:          System/GUI/Other
Url:            https://github.com/DaveDavenport/%{name}
Source:         https://github.com/DaveDavenport/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  cppcheck
BuildRequires:  flex >= 2.5.39
BuildRequires:  librsvg2-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-xrm-devel
Requires:       xdg-utils

%description
rofi is a popup window switcher roughly based on "superswitcher",
requiring only xlib and pango. This version started off as a clone of
simpleswitcher, the version from Sean Pringle. Rofi developed extra
features, like a run dialog, SSH launcher and can act as a drop-in
dmenu replacement.

%package devel
Summary:        Development files for rofi
Group:          Development/Libraries/C and C++

%description devel
Development files and headers for rofi.

%prep
%setup -q

%build
%configure --disable-check
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc Changelog README.md
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%dir %{_datadir}/rofi/
%{_datadir}/rofi/themes/
%{_mandir}/man*/*

%files devel
%{_includedir}/rofi/
%{_libdir}/pkgconfig/rofi.pc

%changelog
*Thu Jul 16 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Thu Jul 16 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Thu Jul 16 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Thu Jul 16 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Thu Jul 16 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Thu Jul 16 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Thu Jul 16 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Thu Jul 16 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Thu Jul 16 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Wed Jul 15 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Tue Jul 14 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Tue Jul 14 2020 Brenton Horne <brentonhorne77@gmail.com> - 1.5.4-1
- New upstream version 1.5.4.
*Mon Jul 01 2019 Brenton Horne <brentonhorne77@gmail.com> - -1
- New upstream version .
*Mon Jun 24 2019 Brenton Horne <brentonhorne77@gmail.com> - -1
- New upstream version .
*Sun Dec 30 2018 Brenton Horne <brentonhorne77@gmail.com> - download-1
- New upstream version download.
* Mon Oct 15 2018 Brenton Horne <brentonhorne77@gmail.com> - download-2
- Adding gcc as a build dependency, apparently it is not installed for 
  F29/Rawhide as a dependency of other build dependencies.
* Mon Oct 15 2018 Brenton Horne <brentonhorne77@gmail.com> - download-1
- Initial commit to git repository, with the spec file taken from revision 3 of
  the OBS repository. This spec file is largely taken from openSUSE's.

Name:		task-wm5sync-common
Version:	1.0
Release:	%{mkrel 6}
Summary:	Metapackage for connecting to Windows Mobile 5+ devices
Group:		Communications
License:	GPLv2+
Requires:	synce-hal
Requires:	sync-engine
Requires:	synce-opensync-plugin
Suggests:	libopensync-plugin-file
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package for connecting with Windows Mobile 5
and later devices. It depends on all packages necessary for setting
up a basic connection to the device. It is not recommended that you
install this package directly, but rather that you install
task-wm5sync-gnome or task-wm5sync-kde, depending on your preferred
desktop environment.

%package -n task-wm5sync-kde
Summary:	KDE metapackage for connecting to Windows Mobile 5+
Group:		Communications
Requires:	task-wm5sync-common
Requires:	libopensync-plugin-kdepim
Requires:	kdepim-kitchensync
Requires:	synce-kpm
Suggests:	synce-kio-rapip

%description -n task-wm5sync-kde
This package is a meta-package for connecting with Windows Mobile 5
and later devices. It depends on all packages necessary for setting
up a basic connection to the device and packages that are useful for
synchronizing with KDE applications. It also depends on a package that
will allow you to access the filesystem on your Windows Mobile device
from KDE applications like Konqueror. This package is mainly intended
for use with KDE 3, as synchronization with KDE 4's PIM applications
is not yet possible. If you wish to use as much functionality as is
currently available in KDE 4, install this package with urpmi's
--no-suggests parameter, and then install the kde4-kio-rapip package.

%package -n task-wm5sync-gnome
Summary:	GNOME metapackage for connecting to Windows Mobile 5+
Group:		Communications
Requires:	task-wm5sync-common
Requires:	libopensync-plugin-evolution2
Requires:	multisync-gui
Requires:	synce-trayicon
Suggests:	synce-gvfs

%description -n task-wm5sync-gnome
This package is a meta-package for connecting with Windows Mobile 5
and later devices. It depends on all packages necessary for setting
up a basic connection to the device and packages that are useful for
synchronizing with GNOME applications. It also depends on a package
that will allow you to access the filesystem on your Windows Mobile
device from any GVFS-compatible application (most GNOME applications).

%files

%files -n task-wm5sync-kde

%files -n task-wm5sync-gnome


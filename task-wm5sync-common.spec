Name:		task-wm5sync-common
Version:	1.0
Release:	%{mkrel 3}
Summary:	Metapackage for connecting to Windows Mobile 5+ devices
Group:		Communications
License:	GPLv2+
Requires:	synce
Requires:	sync-engine
Requires:	odccm
Requires:	libopensync-plugin-synce
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

%description -n task-wm5sync-kde
This package is a meta-package for connecting with Windows Mobile 5
and later devices. It depends on all packages necessary for setting
up a basic connection to the device and packages that are useful for
synchronizing with KDE applications.

%package -n task-wm5sync-gnome
Summary:	GNOME metapackage for connecting to Windows Mobile 5+
Group:		Communications
Requires:	task-wm5sync-common
Requires:	libopensync-plugin-evolution2
Requires:	multisync-gui
Suggests:	synce-kpm

%description -n task-wm5sync-gnome
This package is a meta-package for connecting with Windows Mobile 5
and later devices. It depends on all packages necessary for setting
up a basic connection to the device and packages that are useful for
synchronizing with GNOME applications. At present it also suggests the
synce-kpm package, even though this is a Qt-based application, as it is
clearly the best available application for graphically configuring
partnerships and installing / removing software on these devices.

%files

%files -n task-wm5sync-kde

%files -n task-wm5sync-gnome


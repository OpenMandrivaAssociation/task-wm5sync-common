Name:		task-wm5sync-common
Version:	1.0
Release:	%{mkrel 7}
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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-7mdv2010.0
+ Revision: 434278
- rebuild

* Thu Sep 04 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-6mdv2009.0
+ Revision: 280240
- we can now use trayicon not kpm for GNOME, and drop the explanation in desc
- clarify in KDE package description that it's meant for KDE 3
- add dependencies on VFS support packages - synce-vfs and synce-kio-rapip

* Tue Jun 03 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-4mdv2009.0
+ Revision: 214448
- adjust requires for the new synce-hal era

* Thu Mar 13 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-3mdv2008.1
+ Revision: 187645
- adjust requires for both kde and gnome packages (graphical sync tool for GNOME!)
- build all three wm5sync task packages from this .src.rpm

* Wed Mar 12 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-1mdv2008.1
+ Revision: 187242
- remove stray lines
- import task-wm5sync-common



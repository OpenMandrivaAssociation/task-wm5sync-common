%define version 1.0
%define release %mkrel 1

Name:		task-wm5sync-common
Version:	1.0
Release:	%{mkrel 1}
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

%files


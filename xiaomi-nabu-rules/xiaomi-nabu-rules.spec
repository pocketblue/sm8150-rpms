Name:           xiaomi-nabu-rules
Version:        1
Release:        0%{?dist}
Summary:        some rules for xiaomi pad 5
License:        GPL-3.0-or-later
BuildArch:      noarch
Source1:        99-libinput-calibration-matrix.rules
BuildRequires:  systemd-rpm-macros
Requires:       systemd-udev

%description
%{summary}

%install
install -D -m 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-libinput-calibration-matrix.rules

%files
%{_udevrulesdir}/99-libinput-calibration-matrix.rules

%changelog
%autochangelog

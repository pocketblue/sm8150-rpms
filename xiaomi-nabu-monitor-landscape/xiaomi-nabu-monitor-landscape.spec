Name:           xiaomi-nabu-monitor-landscape
Version:        1
Release:        0%{?dist}
Summary:        rotate monitor on xiaomi pad 5 to landscape by default
License:        CC0-1.0
BuildArch:      noarch
Source1:        monitors.xml

%description
%{summary}

%install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/monitors.xml

%files
%config(noreplace) %{_sysconfdir}/xdg/monitors.xml

%changelog
%autochangelog

Name:           oob3sum
Version:        0.2.0
Release:        1%{?dist}
Summary:        Blistering BLAKE3 tree hasher achieving multi-gigabyte per second throughput.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oob3sum
Source0:        oob3sum-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oob3sum is a sovereign, capability-bounded BLAKE3 HASHER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oob3sum
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oob3sum-uninstall

%files
/usr/bin/oob3sum
/usr/bin/oob3sum-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign BLAKE3 tree hasher and verification engine

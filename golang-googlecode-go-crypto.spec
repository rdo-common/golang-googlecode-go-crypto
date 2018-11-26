# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         golang
%global repo            crypto
# https://github.com/golang/crypto
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/crypto
%global commit          3d3f9f413869b949e48070b5bc593aa22cc2b8f2
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global x_name          golang-golangorg-crypto

%global devel_main      %{x_name}-devel

Name:           golang-googlecode-go-crypto
Version:        0
Release:        0.14.20181125git%{shortcommit}%{?dist}
Summary:        Supplementary Go cryptography libraries
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}


%if 0%{?with_devel}
%package -n %{x_name}-devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(golang.org/x/sys/cpu)
BuildRequires: golang(golang.org/x/sys/unix)
%endif

Requires:      golang(golang.org/x/sys/cpu)
Requires:      golang(golang.org/x/sys/unix)

Provides:      golang(%{import_path}/acme) = %{version}-%{release}
Provides:      golang(%{import_path}/acme/autocert) = %{version}-%{release}
Provides:      golang(%{import_path}/argon2) = %{version}-%{release}
Provides:      golang(%{import_path}/bcrypt) = %{version}-%{release}
Provides:      golang(%{import_path}/blake2b) = %{version}-%{release}
Provides:      golang(%{import_path}/blake2s) = %{version}-%{release}
Provides:      golang(%{import_path}/blowfish) = %{version}-%{release}
Provides:      golang(%{import_path}/bn256) = %{version}-%{release}
Provides:      golang(%{import_path}/cast5) = %{version}-%{release}
Provides:      golang(%{import_path}/chacha20poly1305) = %{version}-%{release}
Provides:      golang(%{import_path}/cryptobyte) = %{version}-%{release}
Provides:      golang(%{import_path}/cryptobyte/asn1) = %{version}-%{release}
Provides:      golang(%{import_path}/curve25519) = %{version}-%{release}
Provides:      golang(%{import_path}/ed25519) = %{version}-%{release}
Provides:      golang(%{import_path}/hkdf) = %{version}-%{release}
Provides:      golang(%{import_path}/md4) = %{version}-%{release}
Provides:      golang(%{import_path}/nacl/auth) = %{version}-%{release}
Provides:      golang(%{import_path}/nacl/box) = %{version}-%{release}
Provides:      golang(%{import_path}/nacl/secretbox) = %{version}-%{release}
Provides:      golang(%{import_path}/nacl/sign) = %{version}-%{release}
Provides:      golang(%{import_path}/ocsp) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/armor) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/clearsign) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/elgamal) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/errors) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/packet) = %{version}-%{release}
Provides:      golang(%{import_path}/openpgp/s2k) = %{version}-%{release}
Provides:      golang(%{import_path}/otr) = %{version}-%{release}
Provides:      golang(%{import_path}/pbkdf2) = %{version}-%{release}
Provides:      golang(%{import_path}/pkcs12) = %{version}-%{release}
Provides:      golang(%{import_path}/poly1305) = %{version}-%{release}
Provides:      golang(%{import_path}/ripemd160) = %{version}-%{release}
Provides:      golang(%{import_path}/salsa20) = %{version}-%{release}
Provides:      golang(%{import_path}/salsa20/salsa) = %{version}-%{release}
Provides:      golang(%{import_path}/scrypt) = %{version}-%{release}
Provides:      golang(%{import_path}/sha3) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/agent) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/knownhosts) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/terminal) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/test) = %{version}-%{release}
Provides:      golang(%{import_path}/ssh/testdata) = %{version}-%{release}
Provides:      golang(%{import_path}/tea) = %{version}-%{release}
Provides:      golang(%{import_path}/twofish) = %{version}-%{release}
Provides:      golang(%{import_path}/xtea) = %{version}-%{release}
Provides:      golang(%{import_path}/xts) = %{version}-%{release}

%description -n %{x_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif


%if 0%{?with_unit_test}
%package unit-test-devel
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{x_name}-devel = %{version}-%{release}

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif


%prep
%setup -q -n %{repo}-%{commit}


%build


%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
for file in ./sha3/testdata/keccakKats.json.deflate; do
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/sha3/testdata
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif


%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# No dependency directories so far

export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/acme
%gotest %{import_path}/acme/autocert
%gotest %{import_path}/argon2
%gotest %{import_path}/bcrypt
%gotest %{import_path}/blake2b
%gotest %{import_path}/blake2s
%gotest %{import_path}/blowfish
%gotest %{import_path}/bn256
%gotest %{import_path}/cast5
%gotest %{import_path}/chacha20poly1305
%gotest %{import_path}/cryptobyte
%gotest %{import_path}/curve25519
%gotest %{import_path}/ed25519
%gotest %{import_path}/hkdf
%gotest %{import_path}/internal/chacha20
%gotest %{import_path}/internal/subtle
%gotest %{import_path}/md4
%gotest %{import_path}/nacl/auth
%gotest %{import_path}/nacl/box
%gotest %{import_path}/nacl/secretbox
%gotest %{import_path}/nacl/sign
%gotest %{import_path}/ocsp
%gotest %{import_path}/openpgp
%gotest %{import_path}/openpgp/armor
%gotest %{import_path}/openpgp/clearsign
%gotest %{import_path}/openpgp/elgamal
%gotest %{import_path}/openpgp/packet
%gotest %{import_path}/openpgp/s2k
%gotest %{import_path}/otr
%gotest %{import_path}/pbkdf2
%gotest %{import_path}/pkcs12
%gotest %{import_path}/pkcs12/internal/rc2
%gotest %{import_path}/poly1305
%gotest %{import_path}/ripemd160
%gotest %{import_path}/salsa20
%gotest %{import_path}/salsa20/salsa
%gotest %{import_path}/scrypt
%gotest %{import_path}/sha3
%gotest %{import_path}/ssh
%gotest %{import_path}/ssh/agent
%gotest %{import_path}/ssh/knownhosts
%gotest %{import_path}/ssh/terminal
%gotest %{import_path}/ssh/test
%gotest %{import_path}/tea
%gotest %{import_path}/twofish
%gotest %{import_path}/xtea
%gotest %{import_path}/xts
%endif


%if 0%{?with_devel}
%files -n %{x_name}-devel -f devel.file-list
%license LICENSE PATENTS
%doc CONTRIBUTING.md README.md AUTHORS CONTRIBUTORS
%dir %{gopath}/src/%{import_path}
%endif


%if 0%{?with_unit_test}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE PATENTS
%doc CONTRIBUTING.md README.md AUTHORS CONTRIBUTORS
%endif

%changelog
* Sun Nov 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.14.20181125git3d3f9f4
- Bump to upstream 3d3f9f413869b949e48070b5bc593aa22cc2b8f2

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git81372b2
- Bump to upstream 81372b2fc2f10bef2a7f338da115c315a56b2726
  related: #1231618

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.gitc10c31b
- Polish the spec file
  related: #1231618

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.gitc10c31b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.gitc10c31b
- Bump to upstream c10c31b5e94b6f7a0283272dc2bb27163dcea24b
  related: #1231618

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.gitc57d4a7
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitc57d4a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.gitc57d4a7
- Fix sed for import path
  related: #1231618

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitc57d4a7
- Choose the correct devel subpackage
  related: #1231618

* Wed Aug 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitc57d4a7
- Update spec file to spec-2.0
  related: #1231618

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitc57d4a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git%{shortcommit}
- Repository has moved to github.com/golang/crypto, updating spec file accordingly
  resolves: #1231618

* Sun Dec 14 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.hg69e2a90ed92d
- Correct Source0 URL
- Correct paths for golang.org/x/crypto/*

* Thu Dec 04 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.hg69e2a90ed92d
- First package for Fedora
  resolves: #1148704

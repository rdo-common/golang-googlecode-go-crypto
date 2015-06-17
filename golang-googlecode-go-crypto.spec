%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         golang
%global repo            crypto
# https://github.com/golang/crypto
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          c57d4a71915a248dbad846d60825145062b4c18e
%global shortcommit      %(r=%{commit}; echo ${r:0:7})

%global gc_provider        google
%global gc_provider_sub    code
%global gc_provider_tld    com
%global gc_project         p
%global gc_repo            crypto
# https://code.google.com/p/crypto
%global gc_import_path     %{gc_provider_sub}.%{gc_provider}.%{gc_provider_tld}/%{gc_project}/go.%{gc_repo}
%global gc_rev             69e2a90ed92d03812364aeb947b7068dc42e561e
%global gc_shortrev        %(r=%{rev}; echo ${r:0:12})

%global x_provider      golang
%global x_provider_tld  org
%global x_repo          crypto
%global x_import_path   %{x_provider}.%{x_provider_tld}/x/%{x_repo}
%global x_name          golang-%{x_provider}%{x_provider_tld}-%{repo}

Name:           golang-%{gc_provider}%{gc_provider_sub}-go-%{gc_repo}
Version:        0
Release:        0.4.git%{shortcommit}%{?dist}
Summary:        Supplementary Go cryptography libraries
License:        BSD
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Summary:        %{summary}
Provides: golang(%{gc_import_path}/bcrypt) = %{version}-%{release}
Provides: golang(%{gc_import_path}/blowfish) = %{version}-%{release}
Provides: golang(%{gc_import_path}/bn256) = %{version}-%{release}
Provides: golang(%{gc_import_path}/cast5) = %{version}-%{release}
Provides: golang(%{gc_import_path}/curve25519) = %{version}-%{release}
Provides: golang(%{gc_import_path}/hkdf) = %{version}-%{release}
Provides: golang(%{gc_import_path}/md4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/nacl/box) = %{version}-%{release}
Provides: golang(%{gc_import_path}/nacl/secretbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/ocsp) = %{version}-%{release}
Provides: golang(%{gc_import_path}/openpgp) = %{version}-%{release}
Provides: golang(%{gc_import_path}/openpgp/armor) = %{version}-%{release}
Provides: golang(%{gc_import_path}/openpgp/clearsign) = %{version}-%{release}
Provides: golang(%{gc_import_path}/openpgp/elgamal) = %{version}-%{release}
Provides: golang(%{gc_import_path}/openpgp/errors) = %{version}-%{release}
Provides: golang(%{gc_import_path}/openpgp/packet) = %{version}-%{release}
Provides: golang(%{gc_import_path}/openpgp/s2k) = %{version}-%{release}
Provides: golang(%{gc_import_path}/otr) = %{version}-%{release}
Provides: golang(%{gc_import_path}/pbkdf2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/poly1305) = %{version}-%{release}
Provides: golang(%{gc_import_path}/ripemd160) = %{version}-%{release}
Provides: golang(%{gc_import_path}/salsa20) = %{version}-%{release}
Provides: golang(%{gc_import_path}/salsa20/salsa) = %{version}-%{release}
Provides: golang(%{gc_import_path}/scrypt) = %{version}-%{release}
Provides: golang(%{gc_import_path}/sha3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/ssh) = %{version}-%{release}
Provides: golang(%{gc_import_path}/ssh/agent) = %{version}-%{release}
Provides: golang(%{gc_import_path}/ssh/terminal) = %{version}-%{release}
Provides: golang(%{gc_import_path}/ssh/test) = %{version}-%{release}
Provides: golang(%{gc_import_path}/ssh/testdata) = %{version}-%{release}
Provides: golang(%{gc_import_path}/twofish) = %{version}-%{release}
Provides: golang(%{gc_import_path}/xtea) = %{version}-%{release}
Provides: golang(%{gc_import_path}/xts) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go crypto libraries with code.google.com/p/ imports.

%package -n %{x_name}-devel
BuildRequires:  golang >= 1.2.1-3
Summary:        %{summary}
Provides: golang(%{x_import_path}/bcrypt) = %{version}-%{release}
Provides: golang(%{x_import_path}/blowfish) = %{version}-%{release}
Provides: golang(%{x_import_path}/bn256) = %{version}-%{release}
Provides: golang(%{x_import_path}/cast5) = %{version}-%{release}
Provides: golang(%{x_import_path}/curve25519) = %{version}-%{release}
Provides: golang(%{x_import_path}/hkdf) = %{version}-%{release}
Provides: golang(%{x_import_path}/md4) = %{version}-%{release}
Provides: golang(%{x_import_path}/nacl/box) = %{version}-%{release}
Provides: golang(%{x_import_path}/nacl/secretbox) = %{version}-%{release}
Provides: golang(%{x_import_path}/ocsp) = %{version}-%{release}
Provides: golang(%{x_import_path}/openpgp) = %{version}-%{release}
Provides: golang(%{x_import_path}/openpgp/armor) = %{version}-%{release}
Provides: golang(%{x_import_path}/openpgp/clearsign) = %{version}-%{release}
Provides: golang(%{x_import_path}/openpgp/elgamal) = %{version}-%{release}
Provides: golang(%{x_import_path}/openpgp/errors) = %{version}-%{release}
Provides: golang(%{x_import_path}/openpgp/packet) = %{version}-%{release}
Provides: golang(%{x_import_path}/openpgp/s2k) = %{version}-%{release}
Provides: golang(%{x_import_path}/otr) = %{version}-%{release}
Provides: golang(%{x_import_path}/pbkdf2) = %{version}-%{release}
Provides: golang(%{x_import_path}/poly1305) = %{version}-%{release}
Provides: golang(%{x_import_path}/ripemd160) = %{version}-%{release}
Provides: golang(%{x_import_path}/salsa20) = %{version}-%{release}
Provides: golang(%{x_import_path}/salsa20/salsa) = %{version}-%{release}
Provides: golang(%{x_import_path}/scrypt) = %{version}-%{release}
Provides: golang(%{x_import_path}/sha3) = %{version}-%{release}
Provides: golang(%{x_import_path}/ssh) = %{version}-%{release}
Provides: golang(%{x_import_path}/ssh/agent) = %{version}-%{release}
Provides: golang(%{x_import_path}/ssh/terminal) = %{version}-%{release}
Provides: golang(%{x_import_path}/ssh/test) = %{version}-%{release}
Provides: golang(%{x_import_path}/ssh/testdata) = %{version}-%{release}
Provides: golang(%{x_import_path}/twofish) = %{version}-%{release}
Provides: golang(%{x_import_path}/xtea) = %{version}-%{release}
Provides: golang(%{x_import_path}/xts) = %{version}-%{release}

%description -n %{x_name}-devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go crypto libraries with golang.org/x/ imports.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}%{gopath}/src/%{gc_import_path}/
install -d -p %{buildroot}%{gopath}/src/%{x_import_path}/
for dir in */ ; do
    cp -rpav $dir %{buildroot}%{gopath}/src/%{gc_import_path}/
    cp -rpav $dir %{buildroot}%{gopath}/src/%{x_import_path}/
done

cd %{buildroot}/%{gopath}/src/%{gc_import_path}/
# from https://groups.google.com/forum/#!topic/golang-nuts/eD8dh3T9yyA, first post
sed -i 's/"golang\.org\/x\//"code\.google\.com\/p\/go\./g' \
        $(find . -name '*.go')

%check
export GOPATH=%{buildroot}%{gopath}:%{gopath}
go test %{x_import_path}/bcrypt
go test %{x_import_path}/blowfish
go test %{x_import_path}/bn256
go test %{x_import_path}/cast5
go test %{x_import_path}/curve25519
go test %{x_import_path}/hkdf
go test %{x_import_path}/md4
go test %{x_import_path}/nacl/box
go test %{x_import_path}/nacl/secretbox
# ocsp/ocsp.go:161: undefined: elliptic.P224
#go test %{x_import_path}/ocsp
go test %{x_import_path}/openpgp
go test %{x_import_path}/openpgp/armor
go test %{x_import_path}/openpgp/clearsign
go test %{x_import_path}/openpgp/elgamal
go test %{x_import_path}/openpgp/packet
go test %{x_import_path}/openpgp/s2k
go test %{x_import_path}/otr
go test %{x_import_path}/pbkdf2
go test %{x_import_path}/poly1305
go test %{x_import_path}/ripemd160
go test %{x_import_path}/salsa20
go test %{x_import_path}/salsa20/salsa
go test %{x_import_path}/scrypt
go test %{x_import_path}/sha3
# fails on ssh/keys_test.go:55: undefined: elliptic.P224
#go test %{x_import_path}/ssh
go test %{x_import_path}/ssh/agent
go test %{x_import_path}/ssh/terminal
go test %{x_import_path}/ssh/test
go test %{x_import_path}/twofish
go test %{x_import_path}/xtea
go test %{x_import_path}/xts

%files devel
%doc LICENSE README
%{gopath}/src/%{gc_import_path}

%files -n %{x_name}-devel
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%{gopath}/src/%{x_import_path}

%changelog
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


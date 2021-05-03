#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : exa
Version  : 0.10.1
Release  : 1
URL      : file:///aot/build/clearlinux/packages/exa/exa-v0.10.1.tar.gz
Source0  : file:///aot/build/clearlinux/packages/exa/exa-v0.10.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: exa-bin = %{version}-%{release}
Requires: exa-data = %{version}-%{release}
Requires: exa-man = %{version}-%{release}
BuildRequires : asciidoctor
BuildRequires : asciidoctor-bin
BuildRequires : asciidoctor-dev
BuildRequires : autoconf-archive-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : cargo-edit
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-go
BuildRequires : gcc-go-lib
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : git
BuildRequires : glibc
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : googletest-dev
BuildRequires : grep
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : just
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libxml2-dev
BuildRequires : llvm
BuildRequires : llvm-bin
BuildRequires : llvm-data
BuildRequires : llvm-dev
BuildRequires : llvm-lib
BuildRequires : llvm-libexec
BuildRequires : llvm-man
BuildRequires : llvm-staticdev
BuildRequires : ncurses-dev
BuildRequires : ninja
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : pandoc
BuildRequires : pandocfilters
BuildRequires : ruby
BuildRequires : rustc
BuildRequires : rustc-bin
BuildRequires : rustc-data
BuildRequires : rustc-dev
BuildRequires : rustc-staticdev
BuildRequires : termcolor
BuildRequires : time
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<div align="center">
<h1>exa</h1>
[exa](https://the.exa.website/) is a modern replacement for _ls_.

%package bin
Summary: bin components for the exa package.
Group: Binaries
Requires: exa-data = %{version}-%{release}

%description bin
bin components for the exa package.


%package data
Summary: data components for the exa package.
Group: Data

%description data
data components for the exa package.


%package man
Summary: man components for the exa package.
Group: Default

%description man
man components for the exa package.


%prep
%setup -q -n exa
cd %{_builddir}/exa
export CARGO_NET_GIT_FETCH_WITH_CLI=true
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export CARGO_HTTP_CAINFO=/var/cache/ca-certs/anchors/ca-certificates.crt
cargo update --verbose
## cargo_update content
cargo upgrade sysinfo
## cargo_update end
cargo fetch --verbose

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
mkdir -p $HOME/.cargo
printf "[build]\nrustflags = [\"-Ctarget-cpu=native\", \"-Ztune-cpu=native\", \"-Cprefer-dynamic=no\", \"-Copt-level=3\", \"-Clto=fat\", \"-Clinker-plugin-lto\", \"-Cembed-bitcode=yes\", \"-Clinker=clang\", \"-Clink-arg=-flto\", \"-Clink-arg=-fuse-ld=lld\", \"-Clink-arg=-Wl,--lto-O3\", \"-Clink-arg=-Wl,-O2\", \"-Clink-arg=-Wl,--hash-style=gnu\", \"-Clink-arg=-Wl,--enable-new-dtags\", \"-Clink-arg=-Wl,--build-id=sha1\", \"-Clink-arg=-fno-stack-protector\", \"-Clink-arg=-Wl,--as-needed\", \"-Clink-arg=-O3\", \"-Clink-arg=-march=native\", \"-Clink-arg=-mtune=native\", \"-Clink-arg=-falign-functions=32\", \"-Clink-arg=-fasynchronous-unwind-tables\", \"-Clink-arg=-funroll-loops\", \"-Clink-arg=-fvisibility-inlines-hidden\", \"-Clink-arg=-static-libstdc++\", \"-Clink-arg=-march=native\", \"-Clink-arg=-static-libgcc\", \"-Clink-arg=-pthread\", \"-Clink-arg=-lpthread\", \"-Clink-arg=-L.\"]\n[net]\ngit-fetch-with-cli = true\n[profile.release]\nopt-level = 3\nlto = \"fat\"\n" > $HOME/.cargo/config.toml
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
unset LDFLAGS
export CARGO_NET_GIT_FETCH_WITH_CLI=true
export CARGO_PROFILE_RELEASE_LTO=fat
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_LINKER=clang
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export CARGO_HTTP_CAINFO=/var/cache/ca-certs/anchors/ca-certificates.crt
export CARGO_TARGET_DIR=target

%install
mkdir -p $HOME/.cargo
printf "[build]\nrustflags = [\"-Ctarget-cpu=native\", \"-Ztune-cpu=native\", \"-Cprefer-dynamic=no\", \"-Copt-level=3\", \"-Clto=fat\", \"-Clinker-plugin-lto\", \"-Cembed-bitcode=yes\", \"-Clinker=clang\", \"-Clink-arg=-flto\", \"-Clink-arg=-fuse-ld=lld\", \"-Clink-arg=-Wl,--lto-O3\", \"-Clink-arg=-Wl,-O2\", \"-Clink-arg=-Wl,--hash-style=gnu\", \"-Clink-arg=-Wl,--enable-new-dtags\", \"-Clink-arg=-Wl,--build-id=sha1\", \"-Clink-arg=-fno-stack-protector\", \"-Clink-arg=-Wl,--as-needed\", \"-Clink-arg=-O3\", \"-Clink-arg=-march=native\", \"-Clink-arg=-mtune=native\", \"-Clink-arg=-falign-functions=32\", \"-Clink-arg=-fasynchronous-unwind-tables\", \"-Clink-arg=-funroll-loops\", \"-Clink-arg=-fvisibility-inlines-hidden\", \"-Clink-arg=-static-libstdc++\", \"-Clink-arg=-march=native\", \"-Clink-arg=-static-libgcc\", \"-Clink-arg=-pthread\", \"-Clink-arg=-lpthread\", \"-Clink-arg=-L.\"]\n[net]\ngit-fetch-with-cli = true\n[profile.release]\nopt-level = 3\nlto = \"fat\"\n" > $HOME/.cargo/config.toml
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
unset LDFLAGS
export CARGO_NET_GIT_FETCH_WITH_CLI=true
export CARGO_PROFILE_RELEASE_LTO=fat
export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
export CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_LINKER=clang
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export CARGO_HTTP_CAINFO=/var/cache/ca-certs/anchors/ca-certificates.crt
export CARGO_TARGET_DIR=target
cargo install %{?_smp_mflags} --all-features --offline --no-track --target x86_64-unknown-linux-gnu --verbose --path . --target-dir target --root %{buildroot}/usr/
## install_append content
just man
## install_append end
## Cargo install assets
install -dm 0755 %{buildroot}/usr/share/bash-completion/completions/
install -m0644 /builddir/build/BUILD/exa/completions/completions.bash %{buildroot}/usr/share/bash-completion/completions/exa
install -dm 0755 %{buildroot}/usr/share/fish/completions/
install -m0644 /builddir/build/BUILD/exa/completions/completions.fish %{buildroot}/usr/share/fish/completions/exa.fish
install -dm 0755 %{buildroot}/usr/share/zsh/site-functions/
install -m0644 /builddir/build/BUILD/exa/completions/completions.zsh %{buildroot}/usr/share/zsh/site-functions/_exa
install -dm 0755 %{buildroot}/usr/share/man/man1/
install -m0644 /builddir/build/BUILD/exa/target/man/exa.1 %{buildroot}/usr/share/man/man1/exa.1
install -dm 0755 %{buildroot}/usr/share/man/man5/
install -m0644 /builddir/build/BUILD/exa/target/man/exa_colors.5 %{buildroot}/usr/share/man/man5/exa_colors.5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/exa

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/exa
/usr/share/fish/completions/exa.fish
/usr/share/zsh/site-functions/_exa

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/exa.1
/usr/share/man/man5/exa_colors.5

FROM ubuntu:20.04
LABEL maintainer="opensource@rerun.io"
# Remember to update the version in publish.sh
# TODO(jleibs) use this version in the publish.sh script and below in the CACHE_KEY
LABEL version="0.9.1"
LABEL description="Docker image used for the CI of https://github.com/rerun-io/rerun"

# Install the ubuntu package dependencies
# This mirrors scripts/setup.sh
ENV DEBIAN_FRONTEND=noninteractive
RUN set -eux; \
    apt-get update; \
    apt-get install -y ca-certificates lsb-release wget; \
    wget https://apache.jfrog.io/artifactory/arrow/ubuntu/apache-arrow-apt-source-latest-focal.deb; \
    apt-get install -y ./apache-arrow-apt-source-latest-focal.deb; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    libarrow-dev \
    build-essential \
    clang-format \
    cmake \
    curl \
    git \
    libatk-bridge2.0 \
    libfontconfig1-dev \
    libfreetype6-dev \
    libglib2.0-dev \
    libgtk-3-dev \
    libssl-dev \
    libxcb-render0-dev \
    libxcb-shape0-dev \
    libxcb-xfixes0-dev \
    libxkbcommon-dev \
    lsb-release \
    python3-pip \
    sudo; \
    rm -rf /var/lib/apt/lists/*;

# Need a more recent pip for manylinux packages to work properly
RUN python3 -m pip install -U pip

# We need a more modern patchelf than ships on ubuntu-20.04
RUN curl -L https://github.com/NixOS/patchelf/releases/download/0.17.2/patchelf-0.17.2-x86_64.tar.gz | tar -xz ./bin/patchelf

# TODO(andreas): Update cargo-deny below when updating rust version to 1.70.0 or above!
ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:$PATH \
    RUST_VERSION=1.72.1 \
    RUSTUP_VERSION=1.26.0

# Install Rust
# Borrowed from: https://github.com/rust-lang/docker-rust/blob/a8a2a9d/1.71.0/bookworm/Dockerfile
RUN set -eux; \
    rustArch='x86_64-unknown-linux-gnu'; \
    rustupSha256='0b2f6c8f85a3d02fde2efc0ced4657869d73fccfce59defb4e8d29233116e6db'; \
    url="https://static.rust-lang.org/rustup/archive/${RUSTUP_VERSION}/${rustArch}/rustup-init"; \
    wget "$url"; \
    echo "${rustupSha256} *rustup-init" | sha256sum -c -; \
    chmod +x rustup-init; \
    ./rustup-init -y --no-modify-path --profile default --default-toolchain $RUST_VERSION --default-host ${rustArch}; \
    rm rustup-init; \
    chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \
    rustup --version; \
    cargo --version; \
    rustc --version;

# Install some cargo tools we know we'll always need
# We can't do this until after we've installed rust / cargo above
# Latest cargo-deny requires a rust update!
RUN cargo install cargo-deny@0.13.9
RUN cargo install cargo-cranky
RUN cargo install cargo-benchcmp

# Install the python build dependencies
ADD rerun_py/requirements-build.txt requirements-build.txt
RUN pip install -r requirements-build.txt

# Install tools from setup_web.sh
ADD scripts/setup_web.sh setup_web.sh
# Installing binaryen is going to cause this script to fail, but that's ok -- we install it manually
RUN ./setup_web.sh || true
# Note: We need a more modern binaryen than ships on ubuntu-20.4, so we pull it from github
RUN curl -L https://github.com/WebAssembly/binaryen/releases/download/version_112/binaryen-version_112-x86_64-linux.tar.gz | tar xzk --strip-components 1

# Increment this to invalidate cache
ENV CACHE_KEY=rerun_docker_v0.9.1

# See: https://github.com/actions/runner-images/issues/6775#issuecomment-1410270956
RUN git config --system --add safe.directory '*'


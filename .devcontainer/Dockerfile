FROM node:20-slim AS builder

WORKDIR /tmp

RUN apt-get update -qq          \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends    \
        ca-certificates         \
        wget                    \
    && npm install -g vsce      \
    && wget https://github.com/ghdl/ghdl-language-server/archive/c37639859f4c663f1f8c77ef2c24d0ef3265e3b1.tar.gz -O /tmp/ghdl-ls.tar.gz \
    && tar -xzf /tmp/ghdl-ls.tar.gz --strip-components=1 ghdl-language-server-c37639859f4c663f1f8c77ef2c24d0ef3265e3b1/vscode-client

WORKDIR /tmp/vscode-client

RUN npm install && vsce package


FROM hdlc/ghdl:yosys AS base

RUN apt-get update -qq              \
    && apt-get upgrade -y           \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends    \
        ca-certificates             \
        git                         \
        libglib2.0-0                \
        libmpc-dev                  \
        libpython3-all-dev          \
        libtcmalloc-minimal4        \
        locales                     \
        make                        \
        npm                         \
        python3                     \
        python3-pip                 \
        sudo                        \
        tar                         \
        wget                        \
        xauth                       \
        xvfb                        \
        xxd                         \
    && apt-get autoclean            \
    && apt-get clean                \
    && apt-get autoremove -y        \
    && rm -r /var/lib/apt/lists/*   \
    && npm install -g netlistsvg

WORKDIR /tmp

# Download and extract GHDL tarball, then copy the files from the lib directory to /lib
RUN wget https://github.com/ghdl/ghdl/releases/download/nightly/ghdl-gha-ubuntu-22.04-mcode.tgz -O /tmp/ghdl.tgz    \
    && mkdir -p /tmp/ghdl                   \
    && tar -xzf /tmp/ghdl.tgz -C /tmp/ghdl  \
    && cp -r /tmp/ghdl/lib/* /lib/          \
    && rm -rf /tmp/ghdl /tmp/ghdl.tgz

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

ENV QUARTUS_PATH=/opt/intelFPGA
ENV QUARTUS_ROOTDIR=${QUARTUS_PATH}/quartus
ENV SOPC_KIT_NIOS2=${QUARTUS_PATH}/nios2eds
ENV RISCV_PATH=/opt/riscv
ENV PATH=${QUARTUS_ROOTDIR}/bin/:${QUARTUS_ROOTDIR}/linux64/gnu/:${QUARTUS_ROOTDIR}/sopc_builder/bin/:$PATH
ENV PATH=${SOPC_KIT_NIOS2}/:${SOPC_KIT_NIOS2}/bin/:${SOPC_KIT_NIOS2}/bin/gnu/H-x86_64-pc-linux-gnu/bin/:${SOPC_KIT_NIOS2}/sdk2/bin/:$PATH
ENV PATH=${RISCV_PATH}/bin/:$PATH

VOLUME /build

# Intel CDN URL
ARG INTEL_CDN="https://downloads.intel.com/akdlm/software/acdsinst"

# Add Quartus installation files
# ADD ${INTEL_CDN}/23.1std/991/ib_installers/cyclone-23.1std.0.991.qdz                .
# ADD ${INTEL_CDN}/23.1std/991/ib_installers/cyclone10lp-23.1std.0.991.qdz            .
ADD ${INTEL_CDN}/23.1std/991/ib_installers/cyclonev-23.1std.0.991.qdz               .
# ADD ${INTEL_CDN}/23.1std/991/ib_installers/max10-23.1std.0.991.qdz                  .
ADD ${INTEL_CDN}/23.1std/991/ib_installers/QuartusLiteSetup-23.1std.0.991-linux.run .

# Fix file permissions and install Quartus Prime Lite
RUN chmod a+x QuartusLiteSetup-23.1std.0.991-linux.run                                                          \
    && ./QuartusLiteSetup-23.1std.0.991-linux.run --mode unattended --accept_eula 1 --installdir /opt/intelFPGA \
    && rm -rf /opt/intelFPGA/uninstall/                                                                         \
    && rm -rf /tmp/*

ADD https://github.com/FelixLuciano/riscv-gnu-toolchain/releases/download/rv32i-240427/rv32i-unknown-elf-gnu-toolchain.tar.gz .
RUN mkdir /opt/riscv                                                    \
    && tar -xzf rv32i-unknown-elf-gnu-toolchain.tar.gz -C /opt/riscv/   \
    && rm -rf /tmp/*

COPY --from=builder /tmp/vscode-client/*.vsix /tmp

RUN echo 'export PS1="\n\e[92m\e[1m\u@\h\e[0m \e[94m\w\n \e[92m\e[1m$\e[0m\e[0m\e[39m\e[49m "' >> ~/.bashrc

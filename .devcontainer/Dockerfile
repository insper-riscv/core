################################################################################
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE
# SPDX-FileCopyrightText: (c) 2022, Marcus Andrade
################################################################################

FROM ubuntu:jammy

ENV DEBIAN_FRONTEND=noninteractive

# Quartus JTAG entrypoint
RUN { \
		echo '#!/bin/sh -e';                                             \
		echo '';                                                         \
		echo 'if [ -n "$GITHUB_TOKEN" ] ; then';                         \
		echo '    gh auth setup-git';                                    \
		echo 'fi';                                                       \
		echo '';                                                         \
		echo 'if [ -n "$JTAG_SERVER" -a -n "$JTAG_PASSWD" ] ; then';     \
		echo '    jtagconfig --addserver "$JTAG_SERVER" "$JTAG_PASSWD"'; \
		echo 'fi';                                                       \
		echo '';                                                         \
		echo 'exec "$@"';                                                \
		echo '';                                                         \
	} | tee /usr/bin/quartus-entrypoint && chmod a+x /usr/bin/quartus-entrypoint

# Add i386 to enable the installation of multiarch binaries (x86-32)
RUN dpkg --add-architecture i386

# Update the image OS
RUN apt-get update                          && \
    apt-get upgrade -y                      && \
    apt-get install -y --no-install-recommends \
                       bc                      \
                       ca-certificates         \
                       curl                    \
                       expect                  \
                       file                    \
                       git                     \
                       iputils-ping            \
                       jq                      \
                       less                    \
                       lib32ncurses5-dev       \
                       lib32z1                 \
                       libc6:i386              \
                       libfontconfig1          \
                       libglib2.0-0            \
                       liblzma-dev             \
                       libncurses5:i386        \
                       libqt5xml5              \
                       libsm6                  \
                       libsm6:i386             \
                       libssl-dev              \
                       libstdc++6:i386         \
                       libtcmalloc-minimal4    \
                       libxext6:i386           \
                       libxft2:i386            \
                       libxrender1             \
                       libzmq3-dev             \
                       locales                 \
                       make                    \
                       net-tools               \
                       openjdk-8-jdk           \
                       pkg-config              \
                       python3-pip             \
                       rsync                   \
                       sed                     \
                       squashfs-tools          \
                       sudo                    \
                       tar                     \
                       tcl                     \
                       tree                    \
                       udev                    \
                       unixodbc-dev            \
                       unzip                   \
                       usbutils                \
                       wget                    \
                       xauth                   \
                       xvfb                    \
                       xz-utils             && \
    rm -r /var/lib/apt/lists/*

# Set System Locales
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

# Change the working directory
# WORKDIR /tmp

# Copy libpng, Github CLI and Changelog generator
# ARG GH_VERSION="2.14.2"
# ARG CHGLOG_VERSION="0.15.1"
# ADD libs/libpng12-0_1.2.54-1ubuntu1.1_amd64.deb .
# ADD libs/libpng12-0_1.2.54-1ubuntu1.1_i386.deb .
# ADD https://github.com/cli/cli/releases/download/v${GH_VERSION}/gh_${GH_VERSION}_linux_amd64.deb .
# ADD https://github.com/git-chglog/git-chglog/releases/download/v${CHGLOG_VERSION}/git-chglog_${CHGLOG_VERSION}_linux_amd64.tar.gz .

# Install libpng, Github CLI and Changelog generator
# RUN dpkg -i libpng12-0_1.2.54-1ubuntu1.1_amd64.deb \
#             libpng12-0_1.2.54-1ubuntu1.1_i386.deb  \
#             gh_${GH_VERSION}_linux_amd64.deb

# RUN tar -zxf git-chglog_${CHGLOG_VERSION}_linux_amd64.tar.gz && \
#     chmod a+x git-chglog                                     && \
#     mv git-chglog /usr/bin/git-chglog                        && \
#     rm -rf  /tmp/*

# Set main Quartus variables
ENV QUARTUS_PATH=/opt/intelFPGA

# Set Quartus environment variables
ENV QUARTUS_ROOTDIR=${QUARTUS_PATH}/quartus
ENV SOPC_KIT_NIOS2=${QUARTUS_PATH}/nios2eds
ENV MODELSIM_ROOTDIR=${QUARTUS_PATH}/modelsim_ase
ENV PATH=${QUARTUS_ROOTDIR}/bin/:${QUARTUS_ROOTDIR}/linux64/gnu/:${QUARTUS_ROOTDIR}/sopc_builder/bin/:$PATH
ENV PATH=${SOPC_KIT_NIOS2}/:${SOPC_KIT_NIOS2}/bin/:${SOPC_KIT_NIOS2}/bin/gnu/H-x86_64-pc-linux-gnu/bin/:${SOPC_KIT_NIOS2}/sdk2/bin/:$PATH
ENV PATH=${MODELSIM_ROOTDIR}/bin/:$PATH

# Where we will store our data
VOLUME /build

# Quartus uses the current working directory
WORKDIR /build

# Expose default JTAG server port
EXPOSE 1309/tcp
EXPOSE 1309/udp

# Metadata Params
ARG BUILD_DATE
ARG BUILD_VERSION

# Metadata
LABEL \
    org.opencontainers.image.vendor="Raetro.org"                                      \
    org.opencontainers.image.title="raetro/quartus"                                   \
    org.opencontainers.image.description="Base OS for Quartus Prime Synthesis Engine" \
    org.opencontainers.image.authors="sigs+fpga@raetro.org"                           \
    org.opencontainers.image.url="https://github.com/raetro/sdk-docker-fpga"          \
    org.opencontainers.image.source="https://github.com/raetro/sdk-docker-fpga.git"   \
    org.opencontainers.image.created=$BUILD_DATE                                      \
    org.opencontainers.image.version=$BUILD_VERSION

ENTRYPOINT ["quartus-entrypoint"]

CMD ["/bin/bash"]

################################################################################
# SPDX-License-Identifier: MIT
# SPDX-FileType: SOURCE
# SPDX-FileCopyrightText: (c) 2022, Marcus Andrade
################################################################################

# Install Quartus on a separated layer of the Docker image to shrink the image size.
# FROM raetro/quartus:base as install

# Change the working directory
WORKDIR /tmp

# Intel CDN URL
ARG INTEL_CDN="https://downloads.intel.com/akdlm/software/acdsinst"

# Add Quartus installation files
# ADD ${INTEL_CDN}/23.1std/991/ib_installers/cyclone-23.1std.0.991.qdz                .
# ADD ${INTEL_CDN}/23.1std/991/ib_installers/cyclone10lp-23.1std.0.991.qdz            .
ADD ${INTEL_CDN}/23.1std/991/ib_installers/cyclonev-23.1std.0.991.qdz               .
# ADD ${INTEL_CDN}/23.1std/991/ib_installers/max10-23.1std.0.991.qdz           
ADD ${INTEL_CDN}/23.1std/991/ib_installers/QuartusLiteSetup-23.1std.0.991-linux.run .
ADD ${INTEL_CDN}/20.1std.1/720/ib_installers/ModelSimSetup-20.1.1.720-linux.run     .

# Fix file permissions
RUN chmod a+x QuartusLiteSetup-23.1std.0.991-linux.run                                                        && \
    ./QuartusLiteSetup-23.1std.0.991-linux.run --mode unattended --accept_eula 1 --installdir /opt/intelFPGA  && \
    chmod a+x ModelSimSetup-20.1.1.720-linux.run                                                              && \
    ./ModelSimSetup-20.1.1.720-linux.run --mode unattended --accept_eula 1 --installdir /opt/intelFPGA        && \
    rm -rf /opt/intelFPGA/uninstall/

################################################################################

# Create clean distribution image
# FROM raetro/quartus:base

# Copy out Quartus instalation files to the image
# COPY --from=install /opt/intelFPGA/ /opt/intelFPGA/

# Load the library from the host system.
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4

# Metadata Params
ARG BUILD_DATE
ARG BUILD_VERSION

# Metadata
LABEL \
    org.opencontainers.image.vendor="Raetro.org"                                     \
    org.opencontainers.image.title="raetro/quartus"                                  \
    org.opencontainers.image.description="Intel Quartus Prime Synthesis Engine"      \
    org.opencontainers.image.authors="sigs+fpga@raetro.org"                          \
    org.opencontainers.image.url="https://github.com/raetro/sdk-docker-fpga"         \
    org.opencontainers.image.source="https://github.com/raetro/sdk-docker-fpga.git"  \
    org.opencontainers.image.created=$BUILD_DATE                                     \
    org.opencontainers.image.version=$BUILD_VERSION

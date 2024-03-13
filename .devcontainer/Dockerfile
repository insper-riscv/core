FROM hdlc/ghdl:yosys

RUN apt-get update -qq              \
    && apt-get upgrade -y           \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends    \
        ca-certificates             \
        git                         \
        libglib2.0-0                \
        libpython3-all-dev          \
        libtcmalloc-minimal4        \
        locales                     \
        make                        \
        npm                         \
        python3                     \
        python3-pip                 \
        sudo                        \
        tar                         \
        xauth                       \
        xvfb                        \
    && apt-get autoclean            \
    && apt-get clean                \
    && apt-get autoremove -y        \
    && rm -r /var/lib/apt/lists/*   \
    && npm install -g netlistsvg

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

ENV QUARTUS_PATH=/opt/intelFPGA
ENV QUARTUS_ROOTDIR=${QUARTUS_PATH}/quartus
ENV SOPC_KIT_NIOS2=${QUARTUS_PATH}/nios2eds
ENV PATH=${QUARTUS_ROOTDIR}/bin/:${QUARTUS_ROOTDIR}/linux64/gnu/:${QUARTUS_ROOTDIR}/sopc_builder/bin/:$PATH
ENV PATH=${SOPC_KIT_NIOS2}/:${SOPC_KIT_NIOS2}/bin/:${SOPC_KIT_NIOS2}/bin/gnu/H-x86_64-pc-linux-gnu/bin/:${SOPC_KIT_NIOS2}/sdk2/bin/:$PATH

VOLUME /build

WORKDIR /tmp

# Intel CDN URL
ARG INTEL_CDN="https://downloads.intel.com/akdlm/software/acdsinst"

# Add Quartus installation files
# ADD ${INTEL_CDN}/23.1std/991/ib_installers/cyclone-23.1std.0.991.qdz                .
# ADD ${INTEL_CDN}/23.1std/991/ib_installers/cyclone10lp-23.1std.0.991.qdz            .
ADD ${INTEL_CDN}/23.1std/991/ib_installers/cyclonev-23.1std.0.991.qdz               .
# ADD ${INTEL_CDN}/23.1std/991/ib_installers/max10-23.1std.0.991.qdz                  .
ADD ${INTEL_CDN}/23.1std/991/ib_installers/QuartusLiteSetup-23.1std.0.991-linux.run .

# Fix file permissions and install Quartus Prime Lite
RUN chmod a+x QuartusLiteSetup-23.1std.0.991-linux.run                                                        && \
    ./QuartusLiteSetup-23.1std.0.991-linux.run --mode unattended --accept_eula 1 --installdir /opt/intelFPGA  && \
    rm -rf /opt/intelFPGA/uninstall/                                                                          && \
    rm -rf /tmp/*

RUN echo 'export PS1="\n\e[92m\e[1m\u@\h\e[0m \e[94m\w\n \e[92m\e[1m$\e[0m\e[0m\e[39m\e[49m "' >> ~/.bashrc

FROM ubuntu:22.04 AS intel

ARG INTEL_CDN="https://downloads.intel.com/akdlm/software/acdsinst/23.1std/991/ib_installers"

VOLUME /opt/intel

WORKDIR /tmp

# - Intel® Quartus® Prime Lite installer
ADD ${INTEL_CDN}/QuartusLiteSetup-23.1std.0.991-linux.run .

# - Cyclone® IV device support
# ADD ${INTEL_CDN}/cyclone-23.1std.0.991.qdz .

# - Cyclone® 10 LP device support
# ADD ${INTEL_CDN}/cyclone10lp-23.1std.0.991.qdz .

# - Cyclone® V device support
ADD ${INTEL_CDN}/cyclonev-23.1std.0.991.qdz .

# - MAX® 10 FPGA device support
# ADD ${INTEL_CDN}/max10-23.1std.0.991.qdz .

RUN chmod a+x QuartusLiteSetup-23.1std.0.991-linux.run  \
    && ./QuartusLiteSetup-23.1std.0.991-linux.run       \
        --mode unattended                               \
        --accept_eula 1                                 \
        --installdir /opt/intel                         \
    && rm -rf /tmp/*


FROM ubuntu:22.04 AS runtime

ARG OSS_CAD_SUITE_URL="https://github.com/YosysHQ/oss-cad-suite-build/releases/download/2025-02-03/oss-cad-suite-linux-x64-20250203.tgz"
ARG DENO_URL="https://dl.deno.land/release/v2.1.9/deno-x86_64-unknown-linux-gnu.zip"
ARG PS1_FORMAT="\\n\\e[0m\\e[1m\\w\\n\\e[92m\\$\\e[0m\\e[39m\\e[49m "

VOLUME /root/.vscode /opt/intel /opt/oss-design-suite

ENV INTEL_PATH=/opt/intel
ENV QUARTUS_ROOTDIR=${INTEL_PATH}/quartus
ENV SOPC_KIT_NIOS2=${INTEL_PATH}/nios2eds
ENV OSS_CAD_SUITE_PATH=/opt/oss-cad-suite
ENV DENO_PATH=/root/.deno
ENV PATH=${QUARTUS_ROOTDIR}/bin/:${QUARTUS_ROOTDIR}/linux64/gnu/:${QUARTUS_ROOTDIR}/sopc_builder/bin/:$PATH
ENV PATH=${SOPC_KIT_NIOS2}/:${SOPC_KIT_NIOS2}/bin/:${SOPC_KIT_NIOS2}/bin/gnu/H-x86_64-pc-linux-gnu/bin/:${SOPC_KIT_NIOS2}/sdk2/bin/:$PATH
ENV PATH=${OSS_CAD_SUITE_PATH}/bin/:${OSS_CAD_SUITE_PATH}/py3bin/:$PATH
ENV PATH=${DENO_PATH}/bin/:$PATH

ADD $OSS_CAD_SUITE_URL    /tmp/oss-cad-suite.tgz
ADD $DENO_URL             /tmp/deno.zip

RUN apt-get update -qq                                  \
    && apt-get upgrade -y                               \
    && DEBIAN_FRONTEND=noninteractive apt-get install   \
        -y --no-install-recommends                      \
        git                                             \
        libdbus-1-3                                     \
        libfontconfig1                                  \
        libglib2.0-0                                    \
        locales                                         \
        unzip                                           \
        zlib1g-dev                                      \
    && apt-get autoclean                                \
    && apt-get clean                                    \
    && apt-get autoremove -y                            \
    && rm -r /var/lib/apt/lists/*                       \
    && locale-gen en_US.UTF-8                           \
    && update-locale LANG=en_US.UTF-8                   \
    && echo 'export PS1="'$PS1_FORMAT'"' >> ~/.bashrc

RUN tar -xzf /tmp/oss-cad-suite.tgz  -C /opt/        \
    && ${OSS_CAD_SUITE_PATH}/py3bin/pip3 install    \
        -q -U --force-reinstall --no-cache-dir      \
        cocotb[bus]                                 \
        edalize                                     \
        pytest                                      \
        pytest-check                                \
        vunit_hdl                                   \
        wavedrom                                    \
    && mkdir ${DENO_PATH}                           \
    && unzip /tmp/deno.zip -d ${DENO_PATH}/bin/     \
    && ${DENO_PATH}/bin/deno install                \
        -q -g --allow-all --no-prompt               \
        npm:netlistsvg

#!/bin/bash
# Copyright 2024 The MathWorks, Inc.

# Example invocation:
# subprocess.call(["bash", "/mathworks/devel/sandbox/prabhakk/cit/jupyter/tljh/the-littlest-jupyterhub/tljh_matlab/install-matlab.sh"],
#                     env={"MATLAB_RELEASE":"R2024a", "MATLAB_PRODUCT_LIST":"MATLAB Simulink"})

# Set the default release to R2024a.
MATLAB_RELEASE="${MATLAB_RELEASE:-"R2024a"}"
# Uppercase first letter
MATLAB_RELEASE=${MATLAB_RELEASE^}

# Set the default product list to only install MATLAB.
MATLAB_PRODUCT_LIST="${MATLAB_PRODUCT_LIST:-"MATLAB"}"

MATLAB_INSTALL_DESTINATION="${MATLAB_INSTALL_DESTINATION:-"/opt/matlab/${MATLAB_RELEASE}"}"

echo "Installing..."
echo "MATLAB_RELEASE: $MATLAB_RELEASE"
echo "MATLAB_PRODUCT_LIST: $MATLAB_PRODUCT_LIST"
echo "MATLAB_INSTALL_DESTINATION: $MATLAB_INSTALL_DESTINATION"

# Run mpm to install MATLAB in the target location and delete the mpm installation afterwards
wget -q https://www.mathworks.com/mpm/glnxa64/mpm && \
chmod +x mpm && \
./mpm install \
--release=${MATLAB_RELEASE} \
--destination=${MATLAB_INSTALL_DESTINATION} \
--products ${MATLAB_PRODUCT_LIST} && \
rm -f mpm /tmp/mathworks_root.log && \
ln -s ${MATLAB_INSTALL_DESTINATION}/bin/matlab /usr/local/bin/matlab
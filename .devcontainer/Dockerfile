# Starting from the MCR dev container image for Node.js (Node 18).
FROM mcr.microsoft.com/devcontainers/typescript-node


# Set the Helmfile version
ARG HELMFILE_VERSION=v0.169.2

# [Optional] Install additional OS packages if needed
# Install required tools and dependencies
RUN apt-get update && apt-get install -y \
    fish \
    curl \
    git \
    build-essential \
    python3-pip \
    tmux \
    fzf \
    apt-transport-https \
    gnupg2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && \
    mv kubectl /usr/local/bin/

# Install Helm
RUN curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install k3d
RUN wget -q -O - https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash

# Download and install Helmfile
RUN curl -sSL "https://github.com/helmfile/helmfile/releases/download/${HELMFILE_VERSION}/helmfile_${HELMFILE_VERSION#v}_linux_amd64.tar.gz" \
    -o /tmp/helmfile.tar.gz \
    && tar -xzf /tmp/helmfile.tar.gz -C /usr/local/bin \
    && rm /tmp/helmfile.tar.gz

# # Download Neovim based on platform
RUN curl -LO https://github.com/neovim/neovim/releases/download/v0.10.2/nvim-linux64.tar.gz && \
    tar xzvf nvim-linux64.tar.gz && \
    mv nvim-linux64 /usr/local/nvim && \
    ln -s /usr/local/nvim/bin/nvim /usr/bin/nvim && \
    rm nvim-linux64.tar.gz; 
# 
WORKDIR /workspace

# Set fish as the default shell for the vscode user
RUN chsh -s /usr/bin/fish node



# Expose port 3000 for Next.js
EXPOSE 3000
# Expose port 8000 for FastApi
EXPOSE 8000

USER node
# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh 
# Add /home/vscode/.local/bin to the PATH
ENV PATH="/home/node/.local/bin:${PATH}"
ENV NEXT_PUBLIC_API_URL=http://localhost:8000/api

# Install LazyVim
RUN git clone https://github.com/LazyVim/starter ~/.config/nvim && \
    nvim --headless "+Lazy sync" +qa

# Set Neovim as the default editor
ENV EDITOR=nvim
ENV PATH="$PATH:/usr/bin"
WORKDIR /workspace
ENV UV_LINK_MODE=copy 






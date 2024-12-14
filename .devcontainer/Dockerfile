# Starting from the MCR dev container image for Node.js (Node 18).
FROM mcr.microsoft.com/devcontainers/typescript-node

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
    && apt-get clean && rm -rf /var/lib/apt/lists/*
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


# Install LazyVim
RUN git clone https://github.com/LazyVim/starter ~/.config/nvim && \
    nvim --headless "+Lazy sync" +qa

# Set Neovim as the default editor
ENV EDITOR=nvim
ENV PATH="$PATH:/usr/bin"
WORKDIR /workspace
ENV UV_LINK_MODE=copy 





